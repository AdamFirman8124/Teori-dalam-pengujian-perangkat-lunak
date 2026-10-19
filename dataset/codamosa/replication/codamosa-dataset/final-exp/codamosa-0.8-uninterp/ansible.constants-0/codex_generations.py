

# Generated at 2022-06-22 11:19:25.479783
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq_constant = _DeprecatedSequenceConstant([1, 2, 3], "Warning", "version 1.0")
    assert len(seq_constant) == 3
    seq_constant = _DeprecatedSequenceConstant(range(1, 10), "Warning", "version 1.0")
    assert len(seq_constant) == 9


# Generated at 2022-06-22 11:19:35.092314
# Unit test for function set_constant
def test_set_constant():

    # Test for the real constants
    for key, value in config.data.get_settings():
        if value is not None:
            if isinstance(value, set):
                assert key in globals()
                assert isinstance(globals()[key], set)
                assert globals()[key] == ensure_type(value, set)
            else:
                assert key in globals()
                assert globals()[key] == ensure_type(value, type(globals()[key]))

    # Test for the deprecated constants
    # Test for the deprecated parameters that are still in the code
    # Test the values
    assert isinstance(ACTION_DEBUG, _DeprecatedSequenceConstant)
    assert ACTION_DEBUG[0] == 'debug'

# Generated at 2022-06-22 11:19:38.781020
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    test_array = _DeprecatedSequenceConstant([1, 2, 3], 'test message', 'test version')
    assert test_array[2] == 3


# Generated at 2022-06-22 11:19:44.854971
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_deprecated = _DeprecatedSequenceConstant(['test'], 'test_warning', '2.9')
    assert len(test_deprecated) == 1
    assert test_deprecated[0] == 'test'
    test_deprecated.__len__()
    test_deprecated.__getitem__(0)

# Generated at 2022-06-22 11:19:46.919558
# Unit test for function set_constant
def test_set_constant():
    export = {}
    set_constant('A', 'foo', export=export)
    assert export['A'] == 'foo'

# Generated at 2022-06-22 11:19:52.166541
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    deprecated_sequence_constant = _DeprecatedSequenceConstant(['127.0.0.1', 'localhost', '::1'], 'Test message', '1.1')
    assert deprecated_sequence_constant[1] == 'localhost'
    assert deprecated_sequence_constant[2] == '::1'

# Generated at 2022-06-22 11:19:57.358812
# Unit test for function set_constant
def test_set_constant():
    set_constant('foo', 'bar')
    assert 'bar' == foo
    set_constant('foo', 'baz', vars())  # And remove it when we're done
    assert 'baz' == globals()['foo']



# Generated at 2022-06-22 11:19:59.855252
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    dsc = _DeprecatedSequenceConstant([], 'test warning message', '2.9')
    assert dsc[0] == []



# Generated at 2022-06-22 11:20:03.175143
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # test case for _DeprecatedSequenceConstant class
    test_ob = _DeprecatedSequenceConstant(['test1', 'test2'], 'message', 'version')
    assert test_ob[0] == 'test1'

# Generated at 2022-06-22 11:20:07.857931
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    old_value = (1, 2, 3)
    message = 'This is a test message'
    version = '2.8'
    test_constant = _DeprecatedSequenceConstant(old_value, message, version)
    assert len(test_constant) == len(old_value)
    assert test_constant[1] == old_value[1]


# Generated at 2022-06-22 11:20:17.095139
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    seq = _DeprecatedSequenceConstant(
        [1, 2, 3],
        'foo',
        'bar')
    # Call __len__ method
    assert len(seq) == 3
    # Call __getitem__ method
    assert seq[0] == 1

# Generated at 2022-06-22 11:20:20.726339
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    value = ['a', 'b', 'c']
    msg = 'Pls remove this'
    version = '2.9.0'
    sequence_constant = _DeprecatedSequenceConstant(value, msg, version)
    assert sequence_constant[1] == 'b'

# Generated at 2022-06-22 11:20:29.692229
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    def call_test(value, msg, version):
        assert len(_DeprecatedSequenceConstant(value, msg, version)) == len(value)
    data = (
        (['a', 'b', 1], 'test deprecated message', '2.7'),
        ({'a': 1, 'b': 2}, 'test deprecated message', '2.7'),
        ('abc', 'test deprecated message', '2.7'),
    )
    for value, msg, version in data:
        yield call_test, value, msg, version


# test method __getitem__ of class _DeprecatedSequenceConstant

# Generated at 2022-06-22 11:20:42.247549
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # construct a _DeprecatedSequenceConstant object
    mock_name = 'test_deprecated'
    mock_msg = 'test_msg'
    mock_version = 'test_version'
    mock_value = [1, 2, 3, 4]
    dsc = _DeprecatedSequenceConstant(mock_value, mock_msg, mock_version)

    # test __len__
    assert len(dsc) == len(mock_value)

    # test __getitem__
    assert dsc[0] == mock_value[0]
    assert dsc[1] == mock_value[1]
    assert dsc[2] == mock_value[2]
    assert dsc[3] == mock_value[3]


# Generated at 2022-06-22 11:20:51.825338
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    assert len(_DeprecatedSequenceConstant(tuple(), 'a', 'b')) == 0
    assert len(_DeprecatedSequenceConstant((1, ), 'a', 'b')) == 1
    assert len(_DeprecatedSequenceConstant([], 'a', 'b')) == 0
    assert len(_DeprecatedSequenceConstant([1], 'a', 'b')) == 1
    assert len(_DeprecatedSequenceConstant(list(), 'a', 'b')) == 0
    assert len(_DeprecatedSequenceConstant(list([1]), 'a', 'b')) == 1


# Generated at 2022-06-22 11:20:57.713266
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    _DeprecatedSequenceConstant(value=('foo', ), msg='msg', version='version')


# FIXME: remove once play_context mangling is removed
# Unfortunately, we must initialize here, so that the
# module caching works correctly. :(
for key in MAGIC_VARIABLE_MAPPING:
    # we want the actual variable names, not aliases
    set_constant(key, MAGIC_VARIABLE_MAPPING[key][0])

# Generated at 2022-06-22 11:21:05.379511
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    deprecated_msg = "Deprecated"
    deprecated_version = "2.12"
    deprecated_obj = _DeprecatedSequenceConstant(['a', 'b', 'c'], deprecated_msg, deprecated_version)

    assert len(deprecated_obj) == 3
    assert isinstance(deprecated_obj, Sequence)
    assert deprecated_obj[0] == 'a'
    assert deprecated_obj[1] == 'b'
    assert deprecated_obj[2] == 'c'

# Generated at 2022-06-22 11:21:07.510650
# Unit test for function set_constant
def test_set_constant():
    set_constant('bogus', 'fake', export=globals())
    assert globals()['bogus'] == 'fake'

# Generated at 2022-06-22 11:21:19.533212
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = 'msg'
    version = 'version'
    value = [1, 2, 3]
    obj = _DeprecatedSequenceConstant(value, msg, version)
    assert len(obj) == 3, 'Sequence length of _DeprecatedSequenceConstant object is not equal to 3, instead it is %s.' % len(obj)
    assert obj[0] == 1, 'First item of sequence of _DeprecatedSequenceConstant is not equal to 1, instead it is %s' % obj[0]
    assert obj[1] == 2, 'Second item of sequence of _DeprecatedSequenceConstant is not equal to 2, instead it is %s' % obj[1]
    assert obj[2] == 3, 'Third item of sequence of _DeprecatedSequenceConstant is not equal to 3, instead it is %s' % obj

# Generated at 2022-06-22 11:21:22.089043
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    a = _DeprecatedSequenceConstant([1, 2, '3'], 'foo', 'bar')
    assert len(a) == 3



# Generated at 2022-06-22 11:21:33.894416
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    # Test for _DeprecatedSequenceConstant.__len__
    # Unit test for method __len__ of class _DeprecatedSequenceConstant
    # Make sure the __len__() of _DeprecatedSequenceConstant
    # returns the correct length.
    #
    # Basic test.
    sequence = list(range(10))
    dsc = _DeprecatedSequenceConstant(sequence, msg='', version='')
    assert len(dsc) == 10

    # Test with different length.
    sequence = list(range(100))
    dsc = _DeprecatedSequenceConstant(sequence, msg='', version='')
    assert len(dsc) == 100


# Generated at 2022-06-22 11:21:37.914076
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    constant = _DeprecatedSequenceConstant(['test', 'test'], 'test msg', 'test version')
    assert len(constant) == 2
    assert constant[0] == 'test'
    assert constant[1] == 'test'


# Generated at 2022-06-22 11:21:46.540392
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Create a function to return the test result
    def count():
        # Create a function to return the test result
        def count():
            # Create an instance of _DeprecatedSequenceConstant
            _deprecated_sequence_constant = _DeprecatedSequenceConstant(['hello'], 'msg', 'version')
            # Execute _deprecated_sequence_constant.__getitem__('hello')
            _deprecated_sequence_constant.__getitem__('hello')
        # Execute the function count
        count()
    # Execute the function count
    count()



# Generated at 2022-06-22 11:21:49.529686
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    c = _DeprecatedSequenceConstant('1', 'msg', 'version')
    assert len(c) == 1



# Generated at 2022-06-22 11:21:56.776481
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    # Test method __getitem__ on a _DeprecatedSequenceConstant
    # object with message and version
    target = ['a', 'b', 'c']
    msg = 'Test message'
    version = 'Test version'

    sequence = _DeprecatedSequenceConstant(target, msg, version)
    expected = 'Test message, to be removed in Test version'

    assert to_text(sequence[1]) == to_text(target[1])
    assert version in to_text(sequence[1])
    assert msg in to_text(sequence[1])

# Generated at 2022-06-22 11:22:00.534225
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    depr_list = _DeprecatedSequenceConstant((1, 2, 3), 'test msg', 'v2.11')
    assert len(depr_list) == 3
    for i, num in enumerate(depr_list):
        assert num == i + 1

# Generated at 2022-06-22 11:22:09.999823
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    empty_list_constant = _DeprecatedSequenceConstant([], 'msg', 'version')
    len_empty_list_constant = len(empty_list_constant)
    assert len_empty_list_constant == 0, "length of empty list constant is not equal 0"

    non_empty_list_constant = _DeprecatedSequenceConstant([1, 2, 3], 'msg', 'version')
    len_non_empty_list_constant = len(non_empty_list_constant)
    assert len_non_empty_list_constant == 3, "length of non empty list constant is not equal 3"



# Generated at 2022-06-22 11:22:11.996525
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    test_sequence = _DeprecatedSequenceConstant([1, 2, 3], 'test_msg', 'test_version')
    assert len(test_sequence) == 3

# Generated at 2022-06-22 11:22:19.649363
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    def mock_deprecated(msg, version):
        return msg, version
    from ansible.module_utils.six import PY3
    if PY3:
        _deprecated = mock_deprecated
    dsc = _DeprecatedSequenceConstant(['ansible'], 'msg', 'version')
    assert dsc[0] == 'ansible'
    assert dsc._msg == 'msg'
    assert dsc._version == 'version'
    assert dsc[0] == 'ansible'

# Generated at 2022-06-22 11:22:22.832125
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    c = _DeprecatedSequenceConstant([1,2,3], 'msg', 'version')
    assert c[0] == 1
    assert c[2] == 3

# Generated at 2022-06-22 11:22:31.944883
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    constant = _DeprecatedSequenceConstant([2, 3, 4], 'test_msg', 'test_version')
    assert len(constant) == 3
    assert constant == [2, 3, 4]


# Generated at 2022-06-22 11:22:39.592279
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    try:
        from ansible.utils.display import Display
        import sys
        import io
        capturedOutput = io.StringIO()           # Create StringIO object
        sys.stdout = capturedOutput
        test_instance = _DeprecatedSequenceConstant([1, 2, 3], 'This is deprecated', '2.5')
        print(len(test_instance))             # Should print 3
        sys.stdout = sys.__stdout__
        assert len(capturedOutput.getvalue()) > 0
        assert capturedOutput.getvalue().endswith('to be removed in 2.5\n')
    except Exception:
        pass
    return

# Generated at 2022-06-22 11:22:40.409033
# Unit test for function set_constant
def test_set_constant():
    dict = set_constant("FOO", "BAR")
    assert dict["FOO"] == "BAR"

# Generated at 2022-06-22 11:22:45.293583
# Unit test for function set_constant
def test_set_constant():
    '''This function allows us to test constants and settings
    with the 'assert' function from the unittest module.
    '''
    settings = set()
    for name, value in vars().items():
        settings.add(name)
        settings.add(value)
    settings.remove('test_set_constant')
    return settings

# Generated at 2022-06-22 11:22:48.259546
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    d = _DeprecatedSequenceConstant((1,2,3), 'no longer supported', '2.9')
    assert len(d) == 3


# Generated at 2022-06-22 11:22:49.875593
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert(isinstance(_DeprecatedSequenceConstant([1, 2], 'abc', '1.0'), Sequence))

# Generated at 2022-06-22 11:22:55.295065
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    dsc = _DeprecatedSequenceConstant((), None, None)
    assert len(dsc) == 0
    dsc = _DeprecatedSequenceConstant((1, 2, 3), None, None)
    assert len(dsc) == 3


# Generated at 2022-06-22 11:23:02.419299
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    res = _DeprecatedSequenceConstant(['a', 'b', 'c'], 'test message', '1.0')
    assert len(res) == 3, "len(res) is not 3"
    assert res[1] == 'b', "res[1] is not 'b'"
    assert res[0] == 'a', "res[0] is not 'a'"
    assert res[2] == 'c', "res[2] is not 'c'"

# Generated at 2022-06-22 11:23:05.264600
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    value = ['value', 'value']
    msg = 'message'
    version = '1.0'
    deprecated_sequence_constant = _DeprecatedSequenceConstant(value, msg, version)
    assert len(deprecated_sequence_constant) == len(value)



# Generated at 2022-06-22 11:23:09.127099
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_val = _DeprecatedSequenceConstant(['apple', 'orange', 'grape'], 'This is a test', '2.9')
    assert len(test_val) == 3
    assert test_val[1] == 'orange'

# Generated at 2022-06-22 11:23:25.839599
# Unit test for function set_constant
def test_set_constant():
    set_constant('test', 'value')
    assert test == 'value'

    set_constant('test_three', (1, 2, 3))
    assert test_three == (1, 2, 3)

    set_constant('test_four', True)
    assert test_four is True

# Generated at 2022-06-22 11:23:36.608943
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    dsc = _DeprecatedSequenceConstant(list(range(10)), 'hello world', '1.1.1')
    assert len(dsc) == 10
    assert dsc[0] == 0
    assert dsc[-1] == 9
    assert dsc[-2] == 8
    assert dsc[1:3] == [1, 2]
    assert dsc[3:] == [3, 4, 5, 6, 7, 8, 9]
    assert dsc[:7] == [0, 1, 2, 3, 4, 5, 6]
    assert dsc[::2] == [0, 2, 4, 6, 8]
    assert dsc[1::2] == [1, 3, 5, 7, 9]

# Generated at 2022-06-22 11:23:38.790182
# Unit test for function set_constant
def test_set_constant():
    EXPORT_DICT = {}
    set_constant('roles_path', 'foo', export=EXPORT_DICT)
    assert EXPORT_DICT['roles_path'] == 'foo'

# Generated at 2022-06-22 11:23:43.673684
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    constant = _DeprecatedSequenceConstant([1, 2, 3], 'message', 'version')
    assert(len(constant) == 3)
    assert(constant[1] == 2)

if __name__ == '__main__':
    # Unit test for constructor of class _DeprecatedSequenceConstant
    test__DeprecatedSequenceConstant()

# Generated at 2022-06-22 11:23:46.808203
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    d = _DeprecatedSequenceConstant((0, 1, 2), 'Warning message', '2.0')
    assert d[0] == 0
    assert d[1] == 1
    assert d[2] == 2



# Generated at 2022-06-22 11:23:56.668832
# Unit test for function set_constant
def test_set_constant():
    from tempfile import mkdtemp
    from os.path import join, isdir, isfile
    import shutil

    config_file = 'ansible.cfg'
    config_dir = mkdtemp()
    config_path = join(config_dir, config_file)

    with open(config_path, 'w') as f:
        f.write('[ssh_connection]\n')
        f.write('ssh_args = -o ControlMaster=auto -o ControlPersist=60s\n')
        f.write('control_path = %(directory)s/%%r@%%h-%%p\n')
        f.write('control_path_dir = ~/.ansible/cp\n')
        f.write('pipelining = False\n')

    config = ConfigManager(config_path)

# Generated at 2022-06-22 11:24:00.918360
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    seq_constant = _DeprecatedSequenceConstant([], 'msg', 'version')
    assert isinstance(seq_constant, _DeprecatedSequenceConstant)

    assert str(seq_constant) == '<_DeprecatedSequenceConstant(msg, version)>'

# Generated at 2022-06-22 11:24:04.260103
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    value = [0, 1, 2]
    msg = "this is a msg"
    version = "0.0.1"
    dsc = _DeprecatedSequenceConstant(value, msg, version)
    assert len(value) == len(dsc)
    return True

# Generated at 2022-06-22 11:24:09.374341
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    seq1 = _DeprecatedSequenceConstant(['foo', 'bar'], 'test msg', '2.2')
    seq2 = _DeprecatedSequenceConstant(['foo', 'bar'], 'test msg', '2.2')
    assert seq1[0] == seq2[0]
    assert seq1[1] == seq2[1]


# Generated at 2022-06-22 11:24:13.672193
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    instance = _DeprecatedSequenceConstant(value=[1, 2, 3],
                                           msg="msg",
                                           version="0")
    assert instance[1] == 2


# Generated at 2022-06-22 11:25:22.344796
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    test_const = _DeprecatedSequenceConstant([1, 2], 'msg', 'version1')
    assert len(test_const) == 2
    assert test_const[0] == 1
    assert test_const[1] == 2

# Generated at 2022-06-22 11:25:28.141508
# Unit test for function set_constant
def test_set_constant():
    test_vars = {}
    test_constant = 'TEST_CONSTANT'
    test_value = 'TEST_VALUE'

    set_constant(test_constant, test_value, test_vars)

    assert test_constant in test_vars
    assert test_vars.get(test_constant) == test_value


# Generated at 2022-06-22 11:25:32.199488
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    seq_const = _DeprecatedSequenceConstant((1, 2, 3), msg="test", version="2.0")
    assert seq_const[0] == 1
    assert seq_const[1] == 2


# Generated at 2022-06-22 11:25:34.769961
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    msg = "This is a deprecated message!"
    version = "V2.10"
    value = [msg, version]
    _DeprecatedSequenceConstant(value, msg, version)

# Generated at 2022-06-22 11:25:43.239919
# Unit test for function set_constant
def test_set_constant():
    import os
    import sys
    import tempfile
    from tempfile import NamedTemporaryFile

    from ansible.compat.tests import unittest

    from ansible.config.manager import ConfigManager, ensure_type

    # setup temp file
    tmp = NamedTemporaryFile()
    config_template = """
[defaults]
foo = {{ ansible_tmpdir }}
bar = {{ ansible_test_var }}
baz = false
boo = yes
bop = {{ ansible_test_var }}
"""
    tmp.write(config_template)
    tmp.flush()

    # create options
    defaults = {'ansible_tmpdir': tempfile.gettempdir(),
                'ansible_test_var': 'my_test_var'}

    # create ConfigManager
    config = ConfigManager()

    # read

# Generated at 2022-06-22 11:25:46.848859
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    seq = (1, 2, 3)
    constant = _DeprecatedSequenceConstant(seq, 'a warning', '2.5')
    assert len(constant) == len(seq)

# Generated at 2022-06-22 11:25:50.789450
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    value = list('foo')
    msg = 'Use of deprecated option'
    version = '1.0'
    dsc = _DeprecatedSequenceConstant(value, msg, version)
    assert dsc[0] == 'f'
    return True

# Generated at 2022-06-22 11:25:56.480496
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    def create_value():
        return [set(), set()]

    def create_msg():
        return ''

    def create_version():
        return '1.0.0'

    def test_with_value(value):
        msg = create_msg()
        version = create_version()

        d = _DeprecatedSequenceConstant(value, msg, version)
        assert len(d) == len(value)

    test_with_value(create_value())

# Generated at 2022-06-22 11:26:05.582289
# Unit test for function set_constant
def test_set_constant():
    assert ALLOWED_INTERNAL_ADDRESSES == '127.0.0.1'

ANSIBLE_DIRECTORY = config.get_config_value('DEFAULT', 'ANSIBLE_DIRECTORY')
DEFAULT_MODULE_PATH = config.get_config_value('DEFAULT', 'DEFAULT_MODULE_PATH')
DEFAULT_ROLES_PATH = config.get_config_value('DEFAULT', 'DEFAULT_ROLES_PATH')
DEFAULT_PLAYBOOK_PATH = config.get_config_value('DEFAULT', 'DEFAULT_PLAYBOOK_PATH')
CACHE_PLUGIN_CONNECTION = config.get_config_value('cache', 'CACHE_PLUGIN_CONNECTION')

# Generated at 2022-06-22 11:26:15.251582
# Unit test for function set_constant
def test_set_constant():
    # Testing for name checking
    for name in ('foo_name', 'foo_48name', 'foo_name48', 'foo48'):
        set_constant(name, 1)
    try:
        set_constant('foo-name', 1)
    except NameError as e:
        assert "global name" in str(e)
    try:
        set_constant('foo name', 1)
    except NameError as e:
        assert "global name" in str(e)
    try:
        set_constant('123foo', 1)
    except NameError as e:
        assert "global name" in str(e)
    try:
        set_constant('foo$name', 1)
    except NameError as e:
        assert "global name" in str(e)



# Generated at 2022-06-22 11:27:26.865180
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    x = _DeprecatedSequenceConstant(value=('a', 'b'), msg="deprecated", version='1.0')
    assert len(x) == 2
    assert x[0] == 'a'
    assert x[1] == 'b'

# Generated at 2022-06-22 11:27:34.658959
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():

    # Check that method returns the length of the value.
    assert len(_DeprecatedSequenceConstant(('a', 'b'), 'msg', 'version')) == 2

    # Check that method returns the length of the value.
    assert len(_DeprecatedSequenceConstant(('a', 'b', 'c', 'd', 'e'), 'msg', 'version')) == 5

    # Check that method returns the length of the value.
    assert len(_DeprecatedSequenceConstant(('a', ), 'msg', 'version')) == 1

    # Check that method returns the length of the value.
    assert len(_DeprecatedSequenceConstant(('a', 'b', 'c'), 'msg', 'version')) == 3



# Generated at 2022-06-22 11:27:39.044287
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    def _test():
        c = _DeprecatedSequenceConstant([1, 2, 3], 'This is a test!', '2.6')
        assert len(c) == 3
        assert c[0] == 1

    # just make sure it does not raise an exception
    _test()



# Generated at 2022-06-22 11:27:47.534401
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    # Value is a single string
    value1 = 'a single string'
    msg1 = 'Unittest'
    version1 = '2.8'
    expected1 = {'_value': value1, '_msg': msg1, '_version': version1}
    d1 = _DeprecatedSequenceConstant(value1, msg1, version1)
    actual1 = vars(d1)
    assert actual1 == expected1, \
        'Value is a single string. Expected: %s. Actual: %s.' % (expected1, actual1)

    # Value is a list
    value2 = ['a string inside a list']
    msg2 = 'Unittest'
    version2 = '2.8'

# Generated at 2022-06-22 11:27:53.078369
# Unit test for function set_constant
def test_set_constant():
    import tempfile
    from ansible.config.manager import ConfigManager
    cm = ConfigManager(['/dev/null'], defaults=None, COLLECTIONS_PATHS=[tempfile.gettempdir()])
    set_constant('FOO', 'foo', cm.data.get_section_settings('defaults'))
    assert cm.data.get_setting('FOO').value == 'foo'

# Generated at 2022-06-22 11:27:57.345229
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    msg = 'Warning: a message'
    version = '1.0'
    input_value = ['a', 'b', 'c']
    expected_result = 'b'

    seq = _DeprecatedSequenceConstant(input_value, msg, version)

    result = seq[1]
    assert result == expected_result

# Generated at 2022-06-22 11:27:59.056889
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    assert _DeprecatedSequenceConstant([1, 2, 3], "msg", "version")[1] == 2

# Generated at 2022-06-22 11:28:01.856598
# Unit test for constructor of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant():
    assert len(_DeprecatedSequenceConstant([1, 2, 3], 'msg', '1.2')) == 3
    assert _DeprecatedSequenceConstant([1, 2, 3], 'msg', '1.2')[1] == 2

# Generated at 2022-06-22 11:28:09.036685
# Unit test for method __getitem__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___getitem__():
    import sys
    class FakeStderr:
        def __init__(self):
            self.output = ''

        def write(self, msg):
            self.output += msg

    fake_stderr = FakeStderr()
    original_stderr = sys.stderr
    sys.stderr = fake_stderr
    try:
        constant = _DeprecatedSequenceConstant([1, 2, 3], 'fake message', '1.0')
        first = constant[0]
        second = constant[1]
        third = constant[2]
    finally:
        # restore sys.stderr
        sys.stderr = original_stderr

    assert first == 1
    assert second == 2
    assert third == 3

    assert fake_stderr.output.count("fake message") == 3

# Generated at 2022-06-22 11:28:14.440689
# Unit test for method __len__ of class _DeprecatedSequenceConstant
def test__DeprecatedSequenceConstant___len__():
    msg = "msg"
    version = "1.2.3"
    sequence = [1, 2, 3]
    deprecated_sequence = _DeprecatedSequenceConstant(sequence, msg, version)
    assert msg == deprecated_sequence._msg
    assert version == deprecated_sequence._version
    assert sequence == deprecated_sequence._value
    assert len(sequence) == len(deprecated_sequence)