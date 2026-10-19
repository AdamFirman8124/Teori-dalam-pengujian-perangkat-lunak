

# Generated at 2022-06-13 06:10:06.523387
# Unit test for function main
def test_main():
    with open("../unit/files/slurp-basic", "r") as read_file:
        contents = read_file.read()
    with patch('ansible.slurp.open', mock_open(read_data=contents), create=True) as m:
        with patch.object(os.path, 'isfile', return_value=True):
            main()
            assert m.called

# Generated at 2022-06-13 06:10:10.077980
# Unit test for function main
def test_main():
    res = main()
    assert res['content'] == 'MjE3OQo='
    assert res['source'] == '/var/run/sshd.pid'
    assert res['encoding'] == 'base64'

# Generated at 2022-06-13 06:10:15.841895
# Unit test for function main
def test_main():
    test_data = {
        'src': 'test_file'
    }
    # This test is written for the Python 2.7 implementation of base64.b64encode().
    test_answer = 'aGVsbG8gdGhlcmUK'
    test_return = {
        'changed': False,
        'content': test_answer,
        'encoding': 'base64',
        'source': 'test_file'
    }
    module = AnsibleModule(argument_spec=dict())
    module.params = test_data
    res = main()
    assert res == test_return

# Generated at 2022-06-13 06:10:22.013691
# Unit test for function main
def test_main():
  testVars = {
    'src': '/tmp/mysrcfile'
  }
  testArgs = {
    'src': '/tmp/mysrcfile'
  }
  with AnsibleModule(argument_spec=testArgs) as module:
    module.params = testVars
    result = main()
    assert result['content'], 'Base64 encoded file'
    assert result['source'], 'Actual path of file slurped'
    assert result['encoding'], 'Type of encoding used for file'

# Generated at 2022-06-13 06:10:24.696918
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    with open('/etc/group', 'rb') as source_fh:
        source_content = source_fh.read()
    data = base64.b64encode(source_content)

    module.exit_json(content=data, source="", encoding='base64')

# Generated at 2022-06-13 06:10:37.223570
# Unit test for function main
def test_main():
    import json
    import tempfile

    data = 'Test text'
    fd, path = tempfile.mkstemp(text=True)
    with open(path, 'w') as fh:
        fh.write(data)

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        check_invalid_arguments=False,
        supports_check_mode=True,
    )
    module.params['src'] = path
    module.exit_json = mock_exit_json

    main()

    assert results['content'] == data.encode('base64').strip()
    assert results['source'] == path
    assert os.stat(path).st_mode & 0o7777 != 0o0777
   

# Generated at 2022-06-13 06:10:41.941555
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

# Generated at 2022-06-13 06:10:53.851093
# Unit test for function main
def test_main():
    import json
    import sys

    if not os.path.exists('/usr/bin/python2'):
        print('WARNING: Python 2 is required for this unit test')
        sys.exit(0)

    simple_file = '/tmp/test_slurp'
    with open(simple_file, 'w') as test_fh:
        test_fh.write('Hi')

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = '/tmp/test_slurp'

    args = '{"src": "/tmp/test_slurp"}'

# Generated at 2022-06-13 06:11:05.670125
# Unit test for function main
def test_main():
    # Slurp module unit tests
    from ansible.modules import slurp


# Generated at 2022-06-13 06:11:14.500888
# Unit test for function main
def test_main():
    def setup_module(module):
        module.params = {'src':'test_main.py'}
        module.exit_json = lambda result: result
        module.fail_json = lambda msg: msg

    def teardown_module(module):
        pass

    test_module = AnsibleModule(argument_spec={})
    setattr(test_module, '_ansible_module', AnsibleModule)
    test_module.setup_module = setup_module
    test_module.teardown_module = teardown_module
    test_main()

# Generated at 2022-06-13 06:11:24.624258
# Unit test for function main
def test_main():
    my_args = dict(path='/var/run/sshd.pid')
    result = main(my_args)

    assert result[0] == 'MjE3OQo='
    assert result[1] == '/var/run/sshd.pid'
    assert result[2] == 'base64'

# Generated at 2022-06-13 06:11:29.948532
# Unit test for function main
def test_main():
    src = '/etc/init.d/nfs-kernel-server'
    module = AnsibleModule({
        'src': src
    })
    main()
    assert module.params['src'] == src
    assert module.params['path'] == src

# Generated at 2022-06-13 06:11:40.171580
# Unit test for function main
def test_main():
    import os
    import tempfile

    # Create a file to test with
    (fd, src) = tempfile.mkstemp(text=True)
    os.close(fd)

    with open(src, "w") as source_fh:
        source_fh.write("This is a test")

    # Create a module
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path'])
        ),
        supports_check_mode=True,
    )

    # Set params
    module.params['src'] = src

    # Run the module
    module.main()

    # Clean up
    os.remove(src)

# Generated at 2022-06-13 06:11:44.692817
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    # Tests
    # module.warn("test")
    # module.exit_json(changed=True, meta=module.params)
    # module.fail_json(msg="test")

# Generated at 2022-06-13 06:11:45.161802
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 06:11:45.606358
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 06:11:46.063219
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 06:11:52.071365
# Unit test for function main
def test_main():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils._text import to_text

    file_path = "/tmp/ansible_slurp_test"
    file_contents = to_bytes('hello world')

    mod = AnsibleModule(
        argument_spec={
            'src': {'required': True, 'aliases': ['path'], 'type': 'path'}
        },
        supports_check_mode=True,
    )

    with open(file_path, 'wb') as test_file:
        test_file.write(file_contents)


# Generated at 2022-06-13 06:11:58.187028
# Unit test for function main
def test_main():
    file = open('testfile.txt','w')
    file.write('hello')
    file.close()
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module.params['src'] = 'testfile.txt'
    os.remove('testfile.txt')
    assert module.params['src'] == 'testfile.txt'
    actionable = True

# Generated at 2022-06-13 06:12:09.595721
# Unit test for function main
def test_main():
    # Test no change when the file exists
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module.params['src'] = os.path.join('test', 'data', 'hello.txt')
    source = module.params['src']


# Generated at 2022-06-13 06:12:23.429843
# Unit test for function main
def test_main():
    # Dummy function call to main()
    main()

# Generated at 2022-06-13 06:12:25.243699
# Unit test for function main
def test_main():
    # empty
    assert main() is None


# Generated at 2022-06-13 06:12:31.311123
# Unit test for function main
def test_main():
    module = AnsibleModule({})
    path = "/etc/exports"
    try:
        with open(path, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % path
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % path
        elif e.errno == errno.EISDIR:
            msg = "source is a directory and must be a file: %s" % path
        else:
            msg = "unable to slurp file: %s" % to_native(e, errors='surrogate_then_replace')


# Generated at 2022-06-13 06:12:44.041804
# Unit test for function main
def test_main():
    args = dict(
        src=dict(type='path', required=True, aliases=['path'])
    )

    import pytest
    @pytest.mark.parametrize("source", [
        "/etc/hosts"
    ])
    def test_data(source):
        args['src'] = source
        with AnsibleModule(argument_spec=args) as module:
            with open(source, 'rb') as myfile:
                expected_result = base64.b64encode(myfile.read())
            module.exit_json(content=expected_result, source=source, encoding='base64')
        assert "Success" == "Success"


# Generated at 2022-06-13 06:12:54.907070
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path'])
        ),
        supports_check_mode=True
    )
    module.params['src'] = __file__
    source_content = open(module.params['src'], 'rb').read()

    source = '/home/me/data/test.txt'
    os.mkdir('/home/me/data')
    open(source, 'wb').write(source_content)

    try:
        module.params['src'] = source
        main()
        assert False
    except SystemExit:
        assert True

    assert module.exit_json.called
    assert module.exit_json.call_args[0][0]['content']

    os.remove(source)
    os

# Generated at 2022-06-13 06:13:06.714765
# Unit test for function main
def test_main():
    # We only test command-line usage here, because the module API is much
    # more complex and would need mocking of e.g. file objects to test.

    # Test basic usage
    module = AnsibleModule(
        argspec=dict(src=dict(type='path', required=True, aliases=['path'])))
    setattr(module, '_ansible_sys_executable', '/usr/bin/python')
    setattr(module, '_ansible_sys_argv', ['/usr/bin/python', module._name])
    setattr(module, '_ansible_testing_name', 'slurp')
    setattr(module, '_ansible_sys_stdout', 'stdout')
    setattr(module, '_ansible_sys_stdin', 'stdin')

# Generated at 2022-06-13 06:13:18.966015
# Unit test for function main
def test_main():
  # Test empty source path
  source = ''
  exception_raised = False
  exception_message = ''
  try:
    with open(source, 'rb') as source_fh:
        source_content = source_fh.read()
  except (IOError, OSError) as e:
    exception_raised = True
    exception_message = e
  assert(exception_raised == True)
  assert(exception_message.errno == errno.ENOENT)
  assert(exception_message.strerror == 'No such file or directory')
  assert(exception_message.filename == source)

  # Test unreadable file
  source = '/root/newfile.txt'
  open(source, 'a').close()
  os.chmod(source, 0o000)

# Generated at 2022-06-13 06:13:19.596663
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 06:13:27.625409
# Unit test for function main
def test_main():
    module_args = dict(
        src="/var/run/sshd.pid"
        )
    # this creates a pseudo-module so we can get the arguments
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module_args = module.params
    source = module_args['src']
    # this is the place to check exit codes
    assert source == "/var/run/sshd.pid"
    with open(source, 'r') as source_fh:
        assert source_fh.read() == '2179\n'


# Unit tests for function main

# Generated at 2022-06-13 06:13:37.591903
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']

    # Test when source exists
    source = '/etc/hosts'
    os.path.exists.return_value = True
    module.exit_json = MagicMock()
    main()
    module.exit_json.assert_called_with()
    assert module.exit_json.call_args[0][0]['source'] == source
    assert module.exit_json.call_args[0][0]['encoding'] == 'base64'

    # Test when source does not exist
    source = '/etc/does/not/exist'
    os.path.ex

# Generated at 2022-06-13 06:14:09.974734
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']

    with open(source, 'rb') as source_fh:
        source_content = source_fh.read()
    data = base64.b64encode(source_content)

    assert module.exit_json(content=data, source=source, encoding='base64')

# Generated at 2022-06-13 06:14:15.421276
# Unit test for function main
def test_main():
    test_fpath = os.path.realpath(__file__)
    base_fpath = os.path.realpath(os.path.join(test_fpath, '..'))
    module_path = os.path.join(base_fpath, 'slurp.py')
    assert main() == module_path

# Generated at 2022-06-13 06:14:22.238281
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={'src': {'type': 'path', 'required': True, 'aliases': ['path']}, },
                           supports_check_mode=True)
    module.exit_json = exit_json
    module.fail_json = fail_json

    # Test with a file containing 'hello world', base64 encoded.
    test_command = 'echo aGVsbG8gd29ybGQK | base64 -d > /tmp/helloworld'
    rc, stdout, stderr = module.run_command(test_command)
    assert rc == 0

    from ansible.module_utils.slurp import main

    main()
    try:
        os.remove('/tmp/helloworld')
    except IOError:
        pass

# Generated at 2022-06-13 06:14:33.341455
# Unit test for function main
def test_main():
    module_name = "slurp"
    # Get ansible_module_slurp_path set by the test
    module_path = os.environ.get('ansible_module_' + module_name + '_path')
    # Parse module options
    source = "foo"
    module = AnsibleModule(argument_spec={
        "src": {"type": "path", "required": True, "aliases": ["path"]}},
        check_invalid_arguments=False,
        bypass_checks=False,
        no_log=False,
        run_once=False,
        supports_check_mode=True,
        mutually_exclusive=[])
    module.params.update(dict(src=source))
    # Create mock data for the result
    data = "QQ=="
    source = "foo"

# Generated at 2022-06-13 06:14:43.929698
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    my_arguments = dict(src='./my_file')
    my_module = basic.AnsibleModule(argument_spec=my_arguments)
    my_module.params = my_arguments
    my_module.check_mode = True
    my_module.no_log = True

    assert not my_module.fail_when_changed()

    from ansible.module_utils.common.text.converters import to_bytes

    my_content = b'blah123'

    with open(my_module.params['src'], 'wb') as my_file:
        my_file.write(my_content)

    main()

    assert b64decode(my_module.params['src']) == my_content

# Generated at 2022-06-13 06:14:53.558792
# Unit test for function main
def test_main():
    os.environ['ANSIBLE_UNIT_TESTING'] = 'True'
    test_source = 'test_hosts'
    src_path = ('/Users/jmccalpin/ansible/test/integration/targets/'
                + test_source)
    test_module = AnsibleModule(argument_spec={'src': {'required': True,
                                                       'type': 'path',
                                                       'aliases': ['path']}})
    test_module.params = {'src': src_path}
    assert test_module.params['src'] == src_path
    with open(src_path, 'rb') as source_fh:
        test_source_content = source_fh.read()
    test_content = base64.b64encode(test_source_content)


# Generated at 2022-06-13 06:14:57.478037
# Unit test for function main
def test_main():
    (result, out, err) = module.run_command(['slurp', 'src=/var/run/sshd.pid'])
    assert result == 0

# Generated at 2022-06-13 06:15:06.695177
# Unit test for function main
def test_main():
    source = "/var/run/sshd.pid"
    module = AnsibleModule("slurp", {"src":source})
    module.warn = lambda x: print("Fake Module Warning: %s" % x)
    module.check_mode = False
    main()
    assert module.params["src"] == source
    assert module.params["encoding"] == "base64"
    assert module.params["changed"] is False
    assert module.params["msg"] == ""
    assert module.params["failed"] is False

# Generated at 2022-06-13 06:15:15.731911
# Unit test for function main
def test_main():
    # Success case 1
    global __file__
    __file__ = "./slurp.py"
    with open("slurp_test_data.txt", "r") as f:
        n = f.read()
    n = n.rstrip("\r\n")
    n = n.encode("utf-8")
    b = base64.b64encode(n)
    with open("slurp_test_data.txt", "rb") as f:
        b2 = base64.b64encode(f.read())

    assert b == b2

    os.remove("slurp_test_data.txt")

# vim: expandtab tabstop=4

# Generated at 2022-06-13 06:15:22.683742
# Unit test for function main
def test_main():
    args = dict(
        src='/var/run/sshd.pid',
    )
    result = dict(
        content='MjE3OQo=',
        encoding='base64',
        source='/var/run/sshd.pid',
    )
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    with open(args['src'], 'rb') as source_fh:
        source_content = source_fh.read()
    data = base64.b64encode(source_content)
    result['content'] = data
    module.exit_json(**result)

# AnsibleModule Test

# Generated at 2022-06-13 06:16:27.614097
# Unit test for function main
def test_main():
    module_mock = AnsibleModule({'src': '/testdir/file.txt'})

    source = "/testdir/file.txt"

    source_content = b'0123456789'

    read_fh_mock = mock.mock_open(read_data=source_content)

    with mock.patch('ansible.module_utils.basic.AnsibleModule', module_mock), mock.patch('io.open', read_fh_mock):
        main()

    assert module_mock.exit_json.called is True
    assert module_mock.fail_json.called is False

# Generated at 2022-06-13 06:16:29.560450
# Unit test for function main
def test_main():
    # source is a directory and must be a file
    assert main() == dict(content="MjE3OQo=", source="/var/run/sshd.pid", encoding="base64")

# Generated at 2022-06-13 06:16:35.230683
# Unit test for function main
def test_main():

    import tempfile

    class FakeModule:
        def __init__(self, source, content, exit_json=True):
            self.params = {
                'src': source,
            }
            self.exit_json = exit_json
            self.exit_json_args = {
                'content': content,
                'source': source,
                'encoding': "base64",
            }

        def fail_json(self, args):
            self.exit_json = False
            self.exit_json_args = args

    # create a temporary file
    source = tempfile.mktemp()
    with open(source, "w") as source_fh:
        source_fh.write("Hello World!")

    # make sure the contents are slurped correctly

# Generated at 2022-06-13 06:16:46.606144
# Unit test for function main
def test_main():

    os.unlink("/tmp/test_fetch")
    with open("/tmp/test_slurp", "w") as fd:
        fd.write("testing123")
    module = AnsibleModule(argument_spec=dict(src=dict(type='path', required=True)))
    result = dict(changed=False, content='', encoding='', source='/tmp/test_slurp')
    module.exit_json(content=result['content'], source=result['source'], encoding=result['encoding'])
    assert result['content'] == "dGVzdGluZzEyMw=="

# vim: set et ts=4 sw=4 :

# Generated at 2022-06-13 06:16:54.046459
# Unit test for function main
def test_main():
    try:
        with open('/tmp/foo.txt') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source
        elif e.errno == errno.EISDIR:
            msg = "source is a directory and must be a file: %s" % source
        else:
            msg = "unable to slurp file: %s" % to_native(e, errors='surrogate_then_replace')

        module.fail_json(msg)

    data = base64.b

# Generated at 2022-06-13 06:17:05.495285
# Unit test for function main
def test_main():

    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins

    open_mock = mock.mock_open(read_data=b"this is a test")
    open_mock.side_effect = [IOError, mock.mock_open().return_value]

    if six.PY3:
        builtin_string = 'builtins'
    else:
        builtin_string = '__builtin__'

    with mock.patch(builtin_string + '.open', open_mock):
        rc = main()
        assert rc['changed']

    with mock.patch(builtin_string + '.open', open_mock):
        rc = main()
        assert rc['changed']

# Generated at 2022-06-13 06:17:13.137950
# Unit test for function main
def test_main():
    src = './test.txt'

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
        check_invalid_arguments=False
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

# Generated at 2022-06-13 06:17:13.726239
# Unit test for function main
def test_main():
    assert False

# Unit test

# Generated at 2022-06-13 06:17:16.321614
# Unit test for function main
def test_main():
    '''replicate behaviour of function main'''

    class FAKE_DEF_PARAMS():
        '''Fake definition of params'''
        content = 'test'
        source = 'test'
        encoding = 'test'
        fail_json = ''
        exit_json = ''

    module = FAKE_DEF_PARAMS()
    source = 'test module'

    main()

# Generated at 2022-06-13 06:17:28.062602
# Unit test for function main
def test_main():
    import tempfile

    # Test successful slurp
    with tempfile.NamedTemporaryFile() as f:
        f.write('test')
        f.flush()
        result = main({'src': f.name})
        assert base64.b64decode(result['content']) == b'test'
        assert result['source'] == f.name
        assert result['encoding'] == 'base64'
        assert result['changed'] is False

    # Test file not found
    try:
        main({'src': 'doesnotexist'})
        assert False, "unreachable code"
    except SystemExit as e:
        assert e.code == 1
        assert 'file not found' in e.args[0]

    # Test directory