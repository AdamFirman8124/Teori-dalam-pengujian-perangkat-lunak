

# Generated at 2022-06-13 06:10:08.357429
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
    )

    assert main() == 0

# Generated at 2022-06-13 06:10:16.024159
# Unit test for function main
def test_main():
    from ansible.module_utils.ansible_release import __version__ as ansible_version
    from ansible.module_utils.six.moves import StringIO

    # Get text for a file
    with open(__file__, 'r') as test_file:
        file_text = test_file.read()

    # Set up test case
    module = AnsibleModule(
        argument_spec=dict(
        src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    # Save stdout
    stdout_old = sys.stdout
    sys.stdout = StringIO()

# Generated at 2022-06-13 06:10:25.404961
# Unit test for function main
def test_main():
    # Test when source file does not exist
    class TestAnsibleModule(object):
        def __init__(self, params):
            self.fail_json = fake_fail_json
            self.params = params
    class FakeException(Exception):
        def __init__(self, errno):
            self.errno = errno
    def fake_open(source, mode):
        raise FakeException(errno.ENOENT)
    def fake_fail_json(msg, **kwargs):
        assert "file not found: /tmp/does-not-exist" in msg
    src = "/tmp/abcdefgh"
    module = TestAnsibleModule({'src': src})
    open_org = os.open
    os.open = fake_open

# Generated at 2022-06-13 06:10:37.899925
# Unit test for function main
def test_main():
    # Test Empty Values
    # Empty Source
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = ""

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source

# Generated at 2022-06-13 06:10:41.915033
# Unit test for function main
def test_main():
    # file not found
    assert main.__name__ == 'main'



# Generated at 2022-06-13 06:10:52.510314
# Unit test for function main
def test_main():
    src_path = "/tmp/test_slurp"
    with open(src_path, 'wb') as fh:
        fh.write("Hello world")
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module.params['src'] = src_path
    data = main()
    assert (data['content'] == "SGVsbG8gd29ybGQ=")
    assert (data['source'] == src_path)
    assert (data['encoding'] == "base64")
    os.remove(src_path)

# Generated at 2022-06-13 06:10:59.488201
# Unit test for function main
def test_main():
    path = os.path.join(os.path.dirname(__file__), 'ansible.cfg')
    test_module = AnsibleModule({'src': path})
    test_module_args = {'src': path}

    # Test for successful run
    with open(path, 'rb') as path_handle:
        truth = {
            'content': base64.b64encode(path_handle.read()),
            'source': path,
            'encoding': 'base64',
        }

    with open(path, 'rb') as path_handle:
        main_result = main()
        assert main_result == test_module.exit_json(**truth)

# Generated at 2022-06-13 06:11:00.180505
# Unit test for function main
def test_main():
   pass

# Generated at 2022-06-13 06:11:10.087963
# Unit test for function main
def test_main():
    source_content = "2179"
    source = "/path/to/file"
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module.params['src'] = source
    try:
        with open(os.path.dirname(os.path.abspath(__file__)) + "/" + source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source

# Generated at 2022-06-13 06:11:21.707357
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        )
    )
    module.exit_json = exit_json
    module.params = { 'src': '/tmp/test_file.txt' }
    source = '/tmp/test_file.txt'
    open(source, 'a').close()
    with open('/tmp/test_file.txt', 'w') as source_fh:
        source_fh.write('Test file')
        source_fh.close()
    main()
    os.remove('/tmp/test_file.txt')

# Generated at 2022-06-13 06:11:41.288781
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source

# Generated at 2022-06-13 06:11:48.743673
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source

# Generated at 2022-06-13 06:11:57.022267
# Unit test for function main
def test_main():
    # Setup
    os.mknod('/tmp/source-file')
    os.mknod('/tmp/target-file')

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module.params['src'] = '/tmp/source-file'

    data = b'\nWelcome\n'

    with open('/tmp/source-file', 'wb') as file:
        file.write(data)

    # Execute
    main()

    # Assertions
    assert module.exit_args['content'] == to_native(base64.b64encode(data), errors='surrogate_then_replace')

# Generated at 2022-06-13 06:11:59.295552
# Unit test for function main
def test_main():
    try:
        main()
    except Exception as e:
        assert False, "Unhandled exception in function main: %s" % e

# Generated at 2022-06-13 06:12:01.214431
# Unit test for function main
def test_main():
    import pytest

    with pytest.raises(Exception) as excinfo:
        main()

# Generated at 2022-06-13 06:12:10.004612
# Unit test for function main
def test_main():
    # Create temp test file
    tmp_file = "/tmp/test_file.txt"
    f = open(tmp_file, "w")
    f.write("This is a test string\n")
    f.close()
    # Create module
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = tmp_file
    # Run function main
    main()
    # Remove temp test file
    os.remove(tmp_file)

# Generated at 2022-06-13 06:12:11.662394
# Unit test for function main
def test_main():
    src = open('/proc/mounts')
    source = src.read()
    data = base64.b64encode(source)
    print(data)


# Generated at 2022-06-13 06:12:19.939085
# Unit test for function main
def test_main():
    mock_input = {
        'src': 'test.txt',
        'check_mode': False,
        'ansible_check_mode': False,
    }

    with open('test.txt', 'w') as test_txt:
        test_txt.write('test stuff')

    test_module = AnsibleModule(mock_input)
    result = main()
    os.remove('test.txt')
    assert result == { 'ansible_check_mode': False,
                       'content': 'dGVzdCBzdHVmZg==',
                       'changed': False,
                       'encoding': 'base64',
                       'source': 'test.txt',
                       'warnings': [],
                     }

# Generated at 2022-06-13 06:12:22.498783
# Unit test for function main
def test_main():
    print("test_main")

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 06:12:33.982136
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source

# Generated at 2022-06-13 06:12:50.997947
# Unit test for function main
def test_main():
    s_file = open('test_file', 'w')
    s_file.write('test')
    s_file.close()

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='str', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = 'test_file'

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s"

# Generated at 2022-06-13 06:13:04.629876
# Unit test for function main
def test_main():
    # Test if no exception occurs
    try:
        main()
    except Exception as e:
        assert False, "unexpected exception raised: " + repr(e)
    # Test if all return fields are present in the return json
    required_fields = ["content", "source", "encoding"]
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    try:
        result = module.exit_json()
    except Exception as e:
        assert False, "unexpected exception raised: " + repr(e)

    for field in required_fields:
        assert field in result, "missing field " + field + " in return json"

# Generated at 2022-06-13 06:13:14.900879
# Unit test for function main
def test_main():
    global source_content
    import mock

    src_file = 'myfile'

    # make this fake file is a module
    path = 'ansible.builtin.slurp'
    source_content = 'mycontent'
    mock_module = mock.Mock()
    mock_module.params = dict(
        src=src_file,
    )

    mock_module.fail_json = mock.Mock()
    mock_module.exit_json = mock.Mock()
    mock_os = mock.Mock()
    mock_os.path.exists = mock.Mock(return_value=True)
    mock_os.access = mock.Mock(return_value=True)
    mock_os.path.isfile = mock.Mock(return_value=True)
    mock_os.path.isd

# Generated at 2022-06-13 06:13:26.448862
# Unit test for function main
def test_main():
    # This is how you'd normally run the module, but since this isn't a normal
    # module, this doesn't work. Instead, if you want to run this module
    # as a unit test, then we need to create our own AnsibleModule object and
    # pass it to main().

    # If no args were provided, we can't guess what you wanted to do
    #args = {}
    #module = AnsibleModule(argument_spec=args)
    #main()

    # Or in this case, we can just create an AnsibleModule object and pass in
    # the parameters.
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 06:13:27.953749
# Unit test for function main
def test_main():
    print("Testing main")
    # Pass
    print("TODO")

# Generated at 2022-06-13 06:13:37.820586
# Unit test for function main
def test_main():
    # Test case when file size is 0 byte
    source = 'ansible_test'
    try:
        with open(source, 'w+') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source
        elif e.errno == errno.EISDIR:
            msg = "source is a directory and must be a file: %s" % source

# Generated at 2022-06-13 06:13:50.052037
# Unit test for function main
def test_main():
    import json
    from ansible.module_utils.common.text.converters import to_bytes

    result = main()
    output = json.loads(result[0]['_ansible_verbose_always'])
    assert 'invocation' in output
    assert 'module_name' in output
    assert 'module_args' in output
    assert output['module_name'] == 'ansible.builtin.slurp'
    assert 'ANSIBLE_MODULE_ARGS' in os.environ

    args = to_bytes(os.environ['ANSIBLE_MODULE_ARGS'])
    output = json.loads(args)
    assert output['src'] == './test_main.py'

# Generated at 2022-06-13 06:13:58.492563
# Unit test for function main
def test_main():
    with open('/tmp/file.txt', 'w') as f:
        f.write('Test')
    source = '/tmp/file.txt'
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module.params['src'] = source
    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        print(e)
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source

# Generated at 2022-06-13 06:14:09.131291
# Unit test for function main
def test_main():
    import os
    import tempfile
    import shutil

    tmpdir = tempfile.mkdtemp()
    with open(os.path.join(tmpdir, "foo"), "wb") as f:
        f.write(b"foo\n")

    m = AnsibleModule(argument_spec={'src': {'type': 'path', 'required': True, 'aliases': ['path']}},
                      supports_check_mode=True)
    cwd = os.getcwd()
    os.chdir(tmpdir)
    results = main()
    os.chdir(cwd)

    shutil.rmtree(tmpdir)

    assert results['content'] == "Zm9vCg=="
    assert results['source'] == "foo"
    assert results['encoding'] == "base64"

# Generated at 2022-06-13 06:14:19.176123
# Unit test for function main
def test_main():
    src = "test.txt"
    with open(src, "w") as f:
        f.write("Hello World")

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source

# Generated at 2022-06-13 06:14:53.626102
# Unit test for function main
def test_main():
    src_file = os.path.join(os.path.dirname(__file__), 'files', 'slurp.txt')
    module = AnsibleModule(argument_spec=dict(
        src=dict(type='path', required=True, aliases=['path']),
    ))
    module.params['src'] = src_file

    try:
        import json
    except:
        import simplejson as json

    f = open(src_file, 'rb')
    source_content = f.read()
    f.close()

    data = base64.b64encode(source_content)
    expected_result = dict(changed=False, content=data, encoding='base64', source=src_file)

    global_result = dict()
    global_result['failed'] = False

# Generated at 2022-06-13 06:14:55.141629
# Unit test for function main
def test_main():
    pass

# end of main()

# Generated at 2022-06-13 06:14:58.394819
# Unit test for function main
def test_main():
    os.path.exists("/etc/passwd")
    assert os.path.exists("/etc/passwd") == False

# Generated at 2022-06-13 06:15:11.627520
# Unit test for function main
def test_main():
    # import pudb; pudb.set_trace()
    test_mod = AnsibleModule(argument_spec={
        'src': {'required': True, 'type': 'str'}
    })
    test_mod.check_mode = False
    test_mod.params['src'] = '/etc/hosts'
    test_mod.exit_json = exit_json
    test_mod.fail_json = fail_json
    test_mod.run_command = run_command
    test_mod.run_command.return_value = ('p0', '', 0)
    test_mod.run_command.return_value = ('bin', '', 0)
    assert 'content' in main()
    assert main()['content'] == 'bin'


# Generated at 2022-06-13 06:15:12.159366
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 06:15:20.329666
# Unit test for function main
def test_main():

    # Given
    import tempfile
    import textwrap
    import logging
    import os

    source_file = tempfile.NamedTemporaryFile(delete=False)
    source_file.write(b"this is source text")
    source_file.close()

    # When
    if os.path.isfile(source_file.name):
        logging.debug("source file {0} exists...".format(source_file.name))
    else:
        logging.debug("source file {0} doesn't exist...".format(source_file.name))

    with open(source_file.name, 'rb') as source_fh:
        source_content = source_fh.read()

    data = base64.b64encode(source_content)

    # Then

# Generated at 2022-06-13 06:15:27.705694
# Unit test for function main
def test_main():
    test_args = dict(
        src='/var/run/sshd.pid',
    )

    # pylint: disable=protected-access,unused-variable
    with pytest.raises(AnsibleExitJson) as exc:
        main()
    assert not exc.value.args[0]['changed']
    assert exc.value.args[0]['encoding'] == 'base64'
    assert exc.value.args[0]['content'] == base64.b64encode('2179\n')
    assert exc.value.args[0]['source'] == '/var/run/sshd.pid'
    # pylint: enable=protected-access,unused-variable

# Generated at 2022-06-13 06:15:37.710723
# Unit test for function main
def test_main():
    test_dict = dict(
        src='/proc/mounts'
    )
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module.params = test_dict
    source = module.params['src']

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source

# Generated at 2022-06-13 06:15:44.139833
# Unit test for function main
def test_main():
    import argparse
    import sys
    import StringIO
    import json
    import mock

    # Test with a nonexistent file
    with mock.patch('os.path.exists', return_value=False):
        with mock.patch('os.path.isdir', return_value=False):
            with mock.patch('os.access', return_value=True):
                with mock.patch('os.open', return_value=-1):
                    with open(os.devnull, 'w') as fd_null:
                        with mock.patch('os.dup', return_value=fd_null.fileno()):
                            sys.stdout = StringIO.StringIO()
                            main()
                            result = json.loads(sys.stdout.getvalue())
                            assert 'msg' in result
                            assert result['failed']

# Generated at 2022-06-13 06:15:51.570978
# Unit test for function main
def test_main():
    import unittest

    class SlurpUnitTest(unittest.TestCase):
        @mock.patch('ansible.module_utils.basic.AnsibleModule')
        def test_slurp(self, mock_AnsibleModule):
            main()
            self.assertTrue(mock_AnsibleModule.called)

    unittest.main()

# Generated at 2022-06-13 06:16:53.480772
# Unit test for function main
def test_main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source

# Generated at 2022-06-13 06:17:02.041807
# Unit test for function main
def test_main():
    # import pdb; pdb.set_trace()
    module_args = {"src":"/etc/os-release"}
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path'])
        ),
        supports_check_mode=True,
    )

    module.params = module_args
    result = main()
    assert result['source'] == "/etc/os-release"
    assert result['encoding'] == "base64"

# Generated at 2022-06-13 06:17:05.953497
# Unit test for function main
def test_main():
    # (module_args, tmpdir, module_name, object_hook, fixup_module_defaults,
    #  return_value, tmp_path, my_output)
    #import pytest
    #pytest.main(['test_slurp.py'])

    # Test invalid paths
    module_args = dict(src='/invalid/path')
    module_name = 'ansible.builtin.slurp'
    module_args['_ansible_module_name'] = module_name
    module = AnsibleModule(module_args)

    assert module.params['src'] == '/invalid/path'

# Generated at 2022-06-13 06:17:12.029243
# Unit test for function main
def test_main():
    b64data='U29tZSBlbmNvZGVkIGJ1ZmZlci4='
    b64data_decoded='Some encoded buffer.'

    # If directory, src=dir fails
    m = AnsibleModule(dict(src=dict(required=True, type='path', aliases=['path'])))
    m.params['src']=__file__
    main()
    assert m.exit_json['content'] == 'U2VjcmV0IGRhdGEh'
    assert base64.b64decode(m.exit_json['content']) == b'data!'

# Generated at 2022-06-13 06:17:17.718854
# Unit test for function main
def test_main():
    ''' Test the main function '''
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = "Hello World"
    test_str = module.params['src']
    assert source in test_str

# Generated at 2022-06-13 06:17:28.233962
# Unit test for function main
def test_main():
    with open('tests/testdata/testfile.bin', 'rb') as tf:
        testdata = tf.read()

    module_args = dict(src='tests/testdata/testfile.bin')
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module._load_params()
    module.params = module_args

    main()

    assert module.params['src'] == 'tests/testdata/testfile.bin'
    assert module.params['encoding'] == 'base64'
    assert module.params['source'] == 'tests/testdata/testfile.bin'
    assert base64.b64decode(module.params['content']) == testdata

# Generated at 2022-06-13 06:17:29.882737
# Unit test for function main
def test_main():
    # Ensure that the function main exits with AnsibleModule.exit_json
    # when it successfully runs.
    assert True == True

# Generated at 2022-06-13 06:17:40.236644
# Unit test for function main
def test_main():
    # In this test we are trying to read a file /tmp/test_a.txt
    # The content of this file is 2179. So the base64 encoded content
    # should be MjE3OQo=
    source = '/tmp/test_a.txt'

    with open(source, 'w') as source_fh:
        source_fh.write('2179\n')

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    source = module.params['src']


# Generated at 2022-06-13 06:17:47.124716
# Unit test for function main
def test_main():
    src = os.path.abspath(__file__)
    with open(src, 'rb') as f:
        contents = f.read()
        b64_contents = base64.b64encode(contents)
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module.params['src'] = src
    main()
    assert module.exit_json_called is True
    assert module.fail_json_called is False
    assert module.exit_json_args['content'] == b64_contents
    assert module.exit_json_args['source'] == src
    assert module.exit_json_args['encoding'] == 'base64'

# Generated at 2022-06-13 06:17:57.557933
# Unit test for function main
def test_main():
    import sys
    import os
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.ansible_release import __version__

    module_args = dict(
        src='/etc/passwd',
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    source = module.params['src']
    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source