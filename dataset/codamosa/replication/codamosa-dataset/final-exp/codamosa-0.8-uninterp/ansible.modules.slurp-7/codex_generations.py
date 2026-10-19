

# Generated at 2022-06-13 06:10:07.714661
# Unit test for function main
def test_main():
    # We want to fail if we try to read a file that doesn't exist
    def run_slurp(source, fails=True):
        args = dict(src=source)
        res = main(args)
        return res
    assert run_slurp('/nonexistentfile')['failed'] is True
    assert run_slurp('/etc/hostname')['changed'] is False

# Generated at 2022-06-13 06:10:15.723628
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path'])
        )
    )
    source = "./test_file"
    try:
        with open(source, 'w') as source_fh:
            source_content = source_fh.write("this is test file")
    except IOError:
        module.fail_json(msg="file not found: %s" % source)


# Generated at 2022-06-13 06:10:24.916685
# Unit test for function main
def test_main():
    test_args = ['/tmp/test.txt']
    with open('/tmp/test.txt', 'w') as test_fh:
        test_fh.write('Test')
    test_module = AnsibleModule(argument_spec={
            'src': dict(type='path', required=True, aliases=['path']),
        }, supports_check_mode=True)
    test_module.params = {'src': test_args[0]}
    result = main()
    assert len(result) == 3
    assert base64.b64decode(result['content']) == b'Test'
    assert result['source'] == test_args[0]
    assert result['encoding'] == 'base64'
    os.remove(test_args[0])

# Generated at 2022-06-13 06:10:37.459955
# Unit test for function main
def test_main():
    import os
    import json

    current_path = os.path.dirname(os.path.realpath(__file__))
    example_file = open(current_path + '/fetch_examples')
    example_json = json.load(example_file)
    example_file.close()

    example_data = example_json[0]
    source_file = example_data['source']

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path'])
        )
    )

    module.params['src'] = source_file

    # Test the function returns the same as the example.
    example_return_data = example_data
    main()
    assert module.exit_json == example_return_data

# Generated at 2022-06-13 06:10:43.377140
# Unit test for function main
def test_main():
    src = 'tests/test_data/slurp.pid'
    src_data = '21799'
    module.params['src'] = src
    try:
        with open(src, 'r') as src_fh:
            src_data = src_fh.read()
    except IOError as e:
        raise

    data = base64.b64encode(src_data)

    try:
        with open('tests/test_data/slurp_fetch.pid', 'w') as slurp_fetch_fh:
            slurp_fetch_fh.write(data)
    except IOError as e:
        raise

# Generated at 2022-06-13 06:10:54.592383
# Unit test for function main
def test_main():
    print(os.path.dirname(os.path.abspath(__file__)))
    print(os.path.abspath(__file__))
    print(__file__)
    print(os.path.basename(__file__))
    print(os.path.normpath(__file__))
    print(os.path.normpath('/path'))
    print(os.path.split(__file__))
    print(os.path.split(os.path.normpath(__file__)))
    print(os.path.split(os.path.abspath(__file__)))
    print(os.path.splitext(__file__))
    print(os.path.splitext('/path/to/file.ext'))

# Generated at 2022-06-13 06:11:06.280796
# Unit test for function main
def test_main():
    import os
    import tempfile
    import ansible.module_utils.basic
    import ansible.module_utils.common.text.converters
    import ansible.module_utils.common.text.converters

    os_path_exists_orig = os.path.exists
    os_remove_orig = os.remove


# Generated at 2022-06-13 06:11:18.437837
# Unit test for function main
def test_main():
    """
    {
        'src': '/var/run/sshd.pid',
    }
    """
    # Update the following code with the module's return information
    module_return_info = {
        'content': 'base64 encoded text',
        'encoding': 'base64',
        'source': '/var/run/sshd.pid',
    }

    module_values_dict = {
        'src': '/var/run/sshd.pid',
    }

    mock_ansible_module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    def mock_open(self, filename, mode):
        self.filename = filename
        self.mode = mode



# Generated at 2022-06-13 06:11:28.815369
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

# Generated at 2022-06-13 06:11:40.482989
# Unit test for function main
def test_main():
    test_args = {
        u'src': u'/var/run/sshd.pid',
    }
    test_result = {
        u'changed': False,
        u'content': u'MjE3OQo=',
        u'encoding': u'base64'
    }

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module.exit_json = mock_exit_json
    module.fail_json = mock_fail_json
    module.params = test_args
    result = main()
    assert(result==test_result)


# Generated at 2022-06-13 06:12:01.686803
# Unit test for function main
def test_main():
    # Test b64encoding of a file
    with open('/tmp/slurp_test_file', 'w+b') as tmp_file:
        tmp_file.write(b'foobar')
    assert main([to_native('/tmp/slurp_test_file')])['encoding'] == 'base64'
    os.remove('/tmp/slurp_test_file')
    # Test that a directory doesn't work
    assert main(['/tmp'])['failed']

# Generated at 2022-06-13 06:12:05.235500
# Unit test for function main
def test_main():
    module=AnsibleModule({
        'src': './tests/files/config.ini'
    }, check_exc=False)
    main()
    assert module._result.get('content')

# Generated at 2022-06-13 06:12:14.624078
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    result = {
        "changed": False,
        "encoding": 'base64',
        "source": '/etc/hosts',
    }
    # Test case 1
    if module.params['src'] == '/etc/hosts':
        if os.path.exists(module.params['src']):
            if os.access(module.params['src'], os.R_OK):
                if not os.path.isdir(module.params['src']):
                    with open(module.params['src'], 'rb') as source_fh:
                        source_content = source_fh.read()


# Generated at 2022-06-13 06:12:20.355907
# Unit test for function main
def test_main():
    module = AnsibleModule({'src': 'data/test_slurp', 'CHECKMODE': True}, check_mode=True)
    module.exit_json = exit_json
    source = 'data/test_slurp'
    try:
        with open(source, 'r') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source
        elif e.errno == errno.EISDIR:
            msg = "source is a directory and must be a file: %s" % source

# Generated at 2022-06-13 06:12:27.209063
# Unit test for function main
def test_main():
    source = 'tests/fixtures/hello_world.txt'
    source_size = os.path.getsize(source)

    # Size of base64 data == ceil((8*10) / 6) == ceil(80 / 6)
    # if you can't follow, do the math and let's see if you're
    # still with me :)
    assert source_size <= (ceil(80 / 6) * 3)

# Generated at 2022-06-13 06:12:36.970388
# Unit test for function main
def test_main():
  from ansible.module_utils.basic import AnsibleModule
  from ansible.module_utils.common.text.converters import to_native

  source = "test_module.py"

  try:
    with open(source, 'rb') as source_fh:
        source_content = source_fh.read()
  except (IOError, OSError) as e:
    if e.errno == errno.ENOENT:
        msg = "file not found: %s" % source
    elif e.errno == errno.EACCES:
        msg = "file is not readable: %s" % source
    elif e.errno == errno.EISDIR:
        msg = "source is a directory and must be a file: %s" % source

# Generated at 2022-06-13 06:12:44.805199
# Unit test for function main
def test_main():
    # NOTE
    # test_ansible_main(module_name, module_args, encoding, output)
    test_ansible_main(
        ANSIBLE_MODULE_ARGS.format(src="slurp_test.py"),
        'base64',
        "file not found: slurp_test.py")
    test_ansible_main(
        ANSIBLE_MODULE_ARGS.format(src=__file__),
        'base64',
        "")

# Generated at 2022-06-13 06:12:55.174280
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']

    # Test for error handling when file does not exist
    base_file_name = os.path.basename(source)
    try:
        with open(base_file_name, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source

# Generated at 2022-06-13 06:13:06.825481
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    class ModuleStub(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, *args, **kwargs):
            raise Exception(args)

        def exit_json(self, **kwargs):
            return kwargs

    source_file = os.path.join(os.path.dirname(__file__), 'test/test.txt')
    if os.path.isfile(source_file):
        with open(source_file, 'rb') as source_fh:
            source_content = source_fh.read()
    else:
        raise Exception('source file %s not found' % source_file)


# Generated at 2022-06-13 06:13:12.291382
# Unit test for function main
def test_main():
    module = AnsibleModule({
            'src': 'file.txt'
        })
    source = module.params['src']

    # Open and read the file
    with open(source, 'rb') as source_fh:
        source_content = source_fh.read()

    data = base64.b64encode(source_content)

    module.exit_json(content=data, source=source, encoding='base64')

# Generated at 2022-06-13 06:13:48.458972
# Unit test for function main
def test_main():
    import tempfile

    # Test case for existing file
    with tempfile.NamedTemporaryFile() as file:
        src = file.name
        with open(src, 'wb') as fh:
            fh.write(b'test')
        module_args = {
            'src': src
        }
        module = AnsibleModule(
            argument_spec=dict(
                src=dict(type='path', required=True, aliases=['path']),
            ),
            supports_check_mode=True,
        )
        source = module.params['src']


# Generated at 2022-06-13 06:13:52.307015
# Unit test for function main
def test_main():
    data = {
        'src': '../../../ansible/builtin/modules/files/test/unit/files/ping.pong'
    }
    ansible_module = AnsibleModule(argument_spec=data, supports_check_mode=True)
    assert 0 == main()

# Generated at 2022-06-13 06:13:52.837713
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 06:13:58.455275
# Unit test for function main
def test_main():
    # Test module
    module_args = dict(
        src='file_to_slurp'
    )
    module = AnsibleModule(
        argument_spec=module_args
    )

    # Test module with default args and values
    result = dict(
        changed=False,
        content='SSBjb250ZW50IGluIGEgZmlsZQo=',
        source='file_to_slurp',
        encoding='base64'
    )
    main()
    assert result == module.exit_json

# Generated at 2022-06-13 06:14:09.089690
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

# Generated at 2022-06-13 06:14:19.140041
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']
    path = os.path.dirname(os.path.realpath(__file__))
    print(path)
#    module.exit_json(content=data, source=source, encoding='base64')
    try:
        with open(path+'/test.txt', 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source

# Generated at 2022-06-13 06:14:21.666302
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleExitJson) as exc:
        main()
    assert not exc.value.args[0]['changed']

# Generated at 2022-06-13 06:14:33.309738
# Unit test for function main
def test_main():
    import tempfile
    import shutil

    tmpdir = tempfile.mkdtemp()

    def cleanup():
        shutil.rmtree(tmpdir)

    import os
    import stat
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.text.converters import to_native
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.text.converters import to_native
    with open(os.path.join(tmpdir, 'test_slurp.txt'), 'w') as test_file:
        test_file.write('foobar')

    test_slurp_path = os.path.join(tmpdir, 'test_slurp.txt')

    # Test file exists
    module = Ans

# Generated at 2022-06-13 06:14:44.163724
# Unit test for function main
def test_main():
    # If the module is run locally, this is the
    # working directory
    local_wd = os.path.dirname(os.path.abspath(__file__))
    # This file will be used to test
    # the module
    test_file_name = "test_slurp_file.txt"
    test_file_path = os.path.join(local_wd, test_file_name)

    # Create the test file
    # in the working directory
    test_file = open(test_file_path, "w")
    test_file_contents = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

# Generated at 2022-06-13 06:14:46.279946
# Unit test for function main
def test_main():
    def get_stdin():
        pass
    # FIXME: use mock to test for existence of file (mocks for open, shouldnt be in 
    # test_main either)
    assert 1 == 1

# Generated at 2022-06-13 06:15:23.835169
# Unit test for function main
def test_main():
    """Simulate ansible-test command"""
    mod = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    mod.params['src'] = './tests/files/test.txt'

    try:
        with open(mod.params['src'], 'wb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % mod.params['src']
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % mod

# Generated at 2022-06-13 06:15:32.529191
# Unit test for function main
def test_main():
    import tempfile
    import os
    import random

    with tempfile.NamedTemporaryFile() as f:
        f.write(open(__file__, 'rb').read())
        f.flush()

        module = AnsibleModule(argument_spec=dict(src=dict(type='path', required=True, aliases=['path'])), supports_check_mode=True)
        module.params['src'] = f.name

        main()

        # We don't want to test randomness. So remove the random seed
        module.fail_json.called_times = 0

# Generated at 2022-06-13 06:15:40.346981
# Unit test for function main
def test_main():

    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils._text import to_text
    from ansible.module_utils.basic import AnsibleModule

    # Define the test case inputs
    module_arg_spec = dict(
        src=dict(type='path', required=True, aliases=['path']),
    )

    test_case_inputs = dict(
        src='/tmp/test_file.txt'
    )

    # Build a dummy module
    module = AnsibleModule(
        argument_spec=module_arg_spec,
        supports_check_mode=True,
    )

    # Create a test file
    test_file_contents = "Hello world!"

# Generated at 2022-06-13 06:15:48.008681
# Unit test for function main
def test_main():
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.files import atomic_move

    def _module(src):
        args = dict(
            src=src
        )
        module = AnsibleModule(argument_spec=args, supports_check_mode=True)
        return module

    with open('test_file', 'wb') as file_fh:
        file_fh.write(b'foobar')

    with open('test_dir', 'wb') as dir_fh:
        dir_fh.write(b'foobar')
        os.fchmod(dir_fh.fileno(), 0o600)

# Generated at 2022-06-13 06:16:00.271040
# Unit test for function main
def test_main():
    args = dict(src='test_slurp.py')
    ansible_module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    expected = dict(
        content=base64.b64encode(open('test_slurp.py', 'rb').read()).decode('utf-8'),
        source='test_slurp.py',
        encoding='base64'
    )
    # Run module
    new_module = AnsibleModule(ansible_module.params, supports_check_mode=ansible_module.supports_check_mode)
    result = new_module.exit_json(**expected)

# Generated at 2022-06-13 06:16:01.619661
# Unit test for function main
def test_main():
    assert to_native(slurp(path="file.txt")) == "Hello World!"

# Generated at 2022-06-13 06:16:05.141799
# Unit test for function main
def test_main():
    with patch('ansible.module_utils.basic.AnsibleModule') as MockClass:
        instance = MockClass.return_value
        instance.params = {'src': '/etc/hosts'}
        instance.exit_json.side_effect = SystemExit
        main()
    assert instance.exit_json.call_count == 1


# Generated at 2022-06-13 06:16:05.862342
# Unit test for function main
def test_main():
    # Testing the main function
    main()

# Generated at 2022-06-13 06:16:15.605241
# Unit test for function main
def test_main():
    '''
    Test module with successful results
    '''
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    # Set the content of the file to be slurped.
    os.environ['ANSIBLE_UNIT_TEST_PID'] = "1234"

    # Set the file mode to be slurped.
    os.environ['ANSIBLE_UNIT_TEST_MODE'] = "0o644"

    # Set the parameters passed to the module.
    module.params['src'] = '$ANSIBLE_UNIT_TEST_PID'

    # Slurp the file.
    main()

    # Test the results.

# Generated at 2022-06-13 06:16:23.059119
# Unit test for function main
def test_main():
    # Test parameter "src"
    file_path = os.path.dirname(__file__)
    module = AnsibleModule(
        argument_spec=dict(
            src = dict(type='path', required=True, aliases=['path']),
        ),
         supports_check_mode=True,
    )
    module.params['src'] = os.path.join(file_path, 'test_data', 'test_slurp.py')
    main()

# Generated at 2022-06-13 06:17:26.445233
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

# Generated at 2022-06-13 06:17:28.007142
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 06:17:36.465766
# Unit test for function main
def test_main():
    source = "/var/run/sshd.pid"
    source_content = open(source, 'rb').read()

    module_class_args = [
        "src=%s" % source,
    ]

    def mock_fail_json(*msg):
        raise Exception(msg)

    def mock_exit_json(changed=False, content=''):
        if (content):
            pass
        else:
            raise Exception("content missing")

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    module.fail_json = mock_fail_json
    module.exit_json = mock_exit_json
    module.params = dict(src=source)
   

# Generated at 2022-06-13 06:17:44.354513
# Unit test for function main
def test_main():

    class FakeModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.fail_json = kwargs.get('fail_json')
            self.exit_json = kwargs.get('exit_json')

        def fail_json(self, msg, **kwargs):
            self.fail_json(msg, kwargs)

        def exit_json(self, content, **kwargs):
            global ENCODED_DATA
            global SOURCE
            ENCODED_DATA = content
            SOURCE = kwargs['source']

    def test_source_file(**kwargs):
        module = FakeModule(**kwargs)
        main()
        return False

    # Test file not exist

# Generated at 2022-06-13 06:17:51.413299
# Unit test for function main
def test_main():

    # Import ansible.module_utils (if not already there)
    import sys, os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'module_utils')))
    import ansible.module_utils

    # Fake module arguments
    argv = [ 'arg1', 'arg2' ]

    # Fake module parameters
    params = { 'src': '/var/run/sshd.pid' }

    # Test function
    main(argv, params)

# Generated at 2022-06-13 06:17:55.213102
# Unit test for function main
def test_main():
    os.environ['ANSIBLE_MODULE_ARGS'] = """{'src':'test/testfile_slurp'}"""
    os.environ['ANSIBLE_MODULE_NAME'] = 'slurp'

    print(main())

# Generated at 2022-06-13 06:17:58.946529
# Unit test for function main
def test_main():
    # Create a module (will not have all attributes normally provided)
    test_mod = {'src': './slurp.py'}
    mod = AnsibleModule(argument_spec=test_mod)
    result = main()
    assert isinstance(result, dict) == True
    assert result['changed'] == False
    print(result)

# Generated at 2022-06-13 06:18:00.122129
# Unit test for function main
def test_main():
    # Assert it runs without errors, the return value is unimportant
    main()

# Generated at 2022-06-13 06:18:06.300987
# Unit test for function main
def test_main():
  import os
  import tempfile
  import shutil
  from ansible.module_utils.basic import AnsibleModule

  test_dir = tempfile.mkdtemp()
  test_file = os.path.join(test_dir, "test.txt")

  with open(test_file, 'w') as fd:
      fd.write("Hello world!")

  module = AnsibleModule(
    argument_spec=dict(
      src=dict(type='path', required=True, aliases=['path']),
    ),
    supports_check_mode=True,
  )

  module.params['src'] = test_file

  main()
  shutil.rmtree(test_dir)

# Generated at 2022-06-13 06:18:10.909475
# Unit test for function main
def test_main():
    with open(module.params['src'], "r") as fd:
        assert fd.read() == base64.b64decode(data)
        assert os.path.isfile(module.params['src'])