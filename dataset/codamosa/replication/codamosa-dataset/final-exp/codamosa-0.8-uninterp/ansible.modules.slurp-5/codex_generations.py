

# Generated at 2022-06-13 06:10:07.931844
# Unit test for function main
def test_main():
    def dummy_module(*args, **kwargs):
        return 1

    module = dummy_module
    module = dummy_module



# Generated at 2022-06-13 06:10:12.369072
# Unit test for function main
def test_main():
    fields = dict(
        src=dict(type='path', required=True, aliases=['path']),
    )

    module_args = dict(
        src='/var/run/sshd.pid',
    )
    module = AnsibleModule(argument_spec=fields, supports_check_mode=True)
    result = main()
    assert result['content'] == 'MjE3OQo='

# Generated at 2022-06-13 06:10:13.128263
# Unit test for function main
def test_main():
    my_test = 1


# Generated at 2022-06-13 06:10:13.476027
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 06:10:18.001198
# Unit test for function main
def test_main():
    """ Test function main """
    from ansible_collections.ansible.community.tests.unit.compat import mock
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch

    with patch('ansible.module_utils.basic.AnsibleModule') as mock_AnsibleModule:
        mock_ansible_module = mock.Mock()
        mock_ansible_module.params = { 'src': 'fake_src'}
        mock_AnsibleModule.return_value = mock_ansible_module

        with patch('ansible.module_utils.basic.open') as mock_open:
            mock_file = mock.Mock()
            mock_open.return_value = mock_file

# Generated at 2022-06-13 06:10:26.098388
# Unit test for function main
def test_main():
    # Create the fixture of the function
    modules_args = dict(
        src="/proc/mounts"
    )

    # Create the AnsibleModule object
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )

    # Execute the function
    main()

    # Check the result
    assert module.exit_json.called
    args, kwargs = module.exit_json.call_args
    assert args == ()
    assert kwargs == dict(
        content='eA==',
        source='/proc/mounts',
        encoding='base64'
    )

# Generated at 2022-06-13 06:10:26.852798
# Unit test for function main
def test_main():
  assert True

# Generated at 2022-06-13 06:10:38.979148
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import sys
    import os
    import pytest
    from ansible.module_utils.six import StringIO
    import ansible.module_utils.slurp as slurp

    test_data = StringIO()
    test_data.write('TEST DATA')
    test_data.seek(0)

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    file_location = os.path.join(sys.path[0], 'test_slurp.data')
    with open(file_location, 'w') as test_file:
        test_file.write(test_data.read())


# Generated at 2022-06-13 06:10:43.167216
# Unit test for function main
def test_main():
    # Set up mock parameters
    module_args = dict(
        src='/tmp/slurp_file'
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    module.params = module_args

    # Create test file
    with open('/tmp/slurp_file', 'w') as file:
      file.write("test")

    # Mock os calls
    module.os = mock_module
    module.os.path.isfile = MagicMock(return_value=True)
    module.os.access = MagicMock(return_value=True)

    # Execute main function
    main()

    # Remove test file
    os.remove('/tmp/slurp_file')

# Generated at 2022-06-13 06:10:44.877733
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 06:11:03.042575
# Unit test for function main

# Generated at 2022-06-13 06:11:03.594032
# Unit test for function main
def test_main():
  assert True

# Generated at 2022-06-13 06:11:04.757439
# Unit test for function main
def test_main():
    """ Returns
    """
    return

# Generated at 2022-06-13 06:11:14.338330
# Unit test for function main
def test_main():
    moduleReality = dict(
        src="/var/run/sshd.pid",
        changed=False,
        content="MjE3OQo=",
        encoding="base64",
        source="/var/run/sshd.pid",
        ansible_facts={}
    )

    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    #module.exit_json(changed=False, source="", content="", encoding="base64")
    assert main() == moduleReality

# Generated at 2022-06-13 06:11:23.174787
# Unit test for function main
def test_main():
    src = os.path.join(os.path.dirname(__file__), '../../lib/ansible/module_utils/facts/system/distribution.py')
    module = AnsibleModule(argument_spec={'src':dict(type='path', required=True, default=src)})

    with open(module.params['src']) as source_fh:
        source_content = source_fh.read()

    module.exit_json(content=base64.b64encode(source_content), source=module.params['src'], encoding='base64')

# Generated at 2022-06-13 06:11:35.612688
# Unit test for function main
def test_main():
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.basic import AnsibleModule

    os.system('echo "test" > /tmp/testfile')

    class TestAnsibleModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            def fake_exit_json(*args, **kwargs):
                self.exit_args = args
                self.exit_kwargs = kwargs
                raise Exception("exit_json called")
            kwargs['exit_json'] = fake_exit_json
            super(TestAnsibleModule, self).__init__(*args, **kwargs)
            self.exit_args = None
            self.exit_kwargs = None


# Generated at 2022-06-13 06:11:39.668589
# Unit test for function main
def test_main():
    assert os.path.exists("/var/run/sshd.pid") == True

# Test function main using a mocked function

# Generated at 2022-06-13 06:11:44.395473
# Unit test for function main
def test_main():
    # need to mock check_mode and exit_json as it is not available in the global namespace
    module = AnsibleModule(argument_spec=dict(
        src=dict(type='path', required=True, aliases=['path']),
    ),
    supports_check_mode=True,
    )

    module.check_mode = False
    module.params['src'] = '/proc/mounts'

    main()

# Generated at 2022-06-13 06:11:44.977616
# Unit test for function main
def test_main():
    assert main() is None

# Generated at 2022-06-13 06:11:51.280124
# Unit test for function main
def test_main():
    # b_src is the binary version of the file being slurped
    b_src = b'#!/bin/bash\nntpdate -u $1\n'
    with open('slurp-test.sh', 'wb') as src_fh:
        src_fh.write(b_src)
    args = {
        'src': './slurp-test.sh',
    }
    expected_result = {
        'content': base64.b64encode(b_src),
        'source': './slurp-test.sh',
        'encoding': 'base64'
    }
    result = AnsibleModule(argument_spec={}).execute_module(module_name='slurp', module_args=args)
    os.remove('./slurp-test.sh')


# Generated at 2022-06-13 06:12:11.877438
# Unit test for function main
def test_main():
    """
    Test module for function main
    """
    # Test with no src argument, should fail
    args = {"src": None}
    # Pass through the args, since we're not mocking the AnsibleModule class
    result = main(args)
    assert result["msg"] == "file not found: None"
    # Test with a directory as the source, should fail
    args = {"src": "/tmp"}
    # Pass through the args, since we're not mocking the AnsibleModule class
    result = main(args)
    assert result["msg"] == "source is a directory and must be a file: /tmp"

# Generated at 2022-06-13 06:12:15.160007
# Unit test for function main
def test_main():
    import io
    import sys
    sys.stdout = io.StringIO()  # disable print for unit testing

    main()
    assert True  # no error raised


# Generated at 2022-06-13 06:12:28.680688
# Unit test for function main
def test_main():
    module_args = dict(
        src='/etc/hosts'
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
        elif e.errno == errno.EACCES:
            msg = "file is not readable: %s" % source

# Generated at 2022-06-13 06:12:42.008999
# Unit test for function main
def test_main():
    module_args = dict(
        src='/tmp/test.txt'
    )
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True
    )
    module.exit_json = Mock()
    module.fail_json = Mock()

    with patch('os.open') as open_mock:
        with patch('os.close') as close_mock:
            open_mock.return_value = 1
            main()
            assert module.exit_json.called
            assert not module.fail_json.called
            assert module.params['src'] == '/tmp/test.txt'
            assert close_mock.called

# Generated at 2022-06-13 06:12:53.288004
# Unit test for function main
def test_main():
    """ Unit test for ansible.module_utils.basic.ansible_module_slurp.main """
    # This just tests basic functionality, it doesn't test argument processing,
    # exception handling, etc.

    # Unit test needs to create a file because this code just reads a local file.
    import tempfile
    import os
    (fh, filename) = tempfile.mkstemp()
    f = os.fdopen(fh, 'w')
    f.write("test")
    f.close()

    # Unit tests are weird: we have to create a module instance and call
    # its fail_json method ourselves
    class ModuleMock(object):
        def __init__(self, filename):
            self.params = {
                'src': filename,
            }
            self.fail_json = None


# Generated at 2022-06-13 06:13:06.038914
# Unit test for function main
def test_main():
  # Test module
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

# Generated at 2022-06-13 06:13:17.951620
# Unit test for function main
def test_main():
    os.system('mkdir -p ~/Ansible/Modules/')
    os.system('cp /etc/ansible/ansible.cfg ~/Ansible/')
    os.system('cp ~/Ansible/Modules/slurp.py ~/Ansible/Modules/slurp')
    os.system('echo \'[defaults]\' > ~/Ansible/ansible.cfg')
    os.system('echo \'library = ~/Ansible/Modules/\' >> ~/Ansible/ansible.cfg')
    os.system('echo \'source = ~/Ansible/Modules/slurp\' >> ~/Ansible/ansible.cfg')
    os.system('ansible localhost -m slurp -a \'src=~/Ansible/Modules/slurp\'')

# Generated at 2022-06-13 06:13:27.250337
# Unit test for function main
def test_main():
    fake_module = AnsibleModule({
        'src': '/home/user/myfile',
    },
    check_invalid_arguments=False,
    supports_check_mode=True,
    )

    myfile_content = "My file content"

    import __builtin__ as builtins
    from ansible_collections.ansible.community.tests.unit.compat.mock import patch

    with patch.object(builtins, 'open', return_value=myfile_content):
        main()
        assert fake_module.exit_json.called
        assert fake_module.exit_json.call_count == 1
        assert fake_module.exit_json.call_args[0][0]['content'] == base64.b64encode(myfile_content)
        assert fake_module.exit_json.call

# Generated at 2022-06-13 06:13:33.541896
# Unit test for function main
def test_main():
    source = os.path.join(os.path.dirname(__file__), "ansible.cfg")

    with open(source, 'rb') as source_fh:
        source_content = source_fh.read()

    data = base64.b64encode(source_content)

    output = {'content': data, 'source': source, 'encoding': 'base64' }

    assert output == main()


# Generated at 2022-06-13 06:13:38.707087
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(src=dict(required=True, aliases=['path']),), supports_check_mode=True)
    with open(os.path.realpath(__file__), 'rb') as source_fh:
        source_content = source_fh.read()
    data = base64.b64encode(source_content)
    module.exit_json(content=data, source=os.path.realpath(__file__), encoding='base64')

# Generated at 2022-06-13 06:14:12.234030
# Unit test for function main
def test_main():
    test_file = 'test_file'
    with open(test_file, 'wb') as f:
        f.write(b'12345')
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src'] = test_file
    try:
        main()
    finally:
        os.remove(test_file)

    source_content = b'12345'
    data = base64.b64encode(source_content)
    assert data == b'MTIzNDU='
    module.exit_json(content=data, source=source, encoding='base64')

# Generated at 2022-06-13 06:14:20.128365
# Unit test for function main
def test_main():
    source = '/tmp/test_slurp.txt'
    with open(source, 'w') as source_fh:
        source_fh.write("I'm a test file for slurp")

    module = AnsibleModule(
        argument_spec = dict(
            src = dict(type = 'path', required=True, aliases=['path'])
        ),
        supports_check_mode = False)

    module.params['src'] = source
    data = main()

    data_decoded = base64.b64decode(data['content'])
    assert data_decoded == b"I'm a test file for slurp"

    os.remove(source)

# Generated at 2022-06-13 06:14:32.293426
# Unit test for function main
def test_main():
    # First test case covers empty file
    module_args = {}
    module_args['src'] = 'test_slurp.txt'
    module = AnsibleModule(
        argument_spec = module_args
        )
    with open(module_args['src'], 'w') as f:
        f.write('')
    test_base64 = base64.b64encode(b'')
    try:
        with open(module.params['src'], 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        msg = "unable to slurp file: %s" % to_native(e, errors='surrogate_then_replace')
        module.fail_json(msg)

# Generated at 2022-06-13 06:14:43.645132
# Unit test for function main
def test_main():
    # Mock ansible.module_utils.basic.AnsibleModule
    class AnsibleModuleMock(object):
        def __init__(self, argument_spec, supports_check_mode, **kwargs):
            self.params = {
                'src': '/some/file'
            }

        def exit_json(self, content, source, encoding):
            assert content == b'aGVsbG8K'
            assert source == '/some/file'
            assert encoding == 'base64'

    # Mock builtins.open().
    open_mock = Mock(return_value="hello\n")

    # Mock base64.b64encode().
    b64encode_mock = Mock(return_value=b'aGVsbG8K')

    # Mock os.path.isfile().
    isfile_

# Generated at 2022-06-13 06:14:53.419474
# Unit test for function main
def test_main():
    # Test if the first parameter is a valid path
    path = '/tmp/test_file'
    open(path, 'a').close()
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']
    source = '/tmp/test_file'

    try:
        with open(source, 'rb') as source_fh:
            source_content = source_fh.read()
    except (IOError, OSError) as e:
        if e.errno == errno.ENOENT:
            msg = "file not found: %s" % source

# Generated at 2022-06-13 06:15:04.806666
# Unit test for function main
def test_main():
    content = 'test'

    def new_open(*args, **kwargs):
        return args[0]

    class FakeModule(object):
        def __init__(self):
            self.params = { 'src': 'test' }
            self.exit_json = lambda x: x

        def fail_json(self, msg):
            raise SystemExit(msg)

    def new_base64(*args, **kwargs):
        return content

    old_open = os.open
    old_base64 = base64.b64encode

    os.open = new_open
    base64.b64encode = new_base64


# Generated at 2022-06-13 06:15:14.157603
# Unit test for function main
def test_main():
    # Get path to file
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'slurp_file.txt')

    # Read file content
    with open(filename, 'r') as f:
        result = f.read()

    # Trigger test function
    module = AnsibleModule(argument_spec=dict(src=dict(type='path', required=True, aliases=['path'])))
    module.params['src'] = filename
    main()

    # Get data from module results
    result_decoded = base64.b64decode(module.exit_json['content'])
    result_source = module.exit_json['source']
    result_encoding = module.exit_json['encoding']

    # Assert data is correct
    assert result_decoded

# Generated at 2022-06-13 06:15:25.279999
# Unit test for function main
def test_main():
    fake_file_contents = (b"fake contents")
    expected_data = base64.b64encode(fake_file_contents)
    fake_source = "/tmp/fake_source.txt"

    m = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = m.params['src']

    class mock_open():
        def __init__(self, path, mode):
            self.path = path

        def read(self):
            return fake_file_contents

    with mock.patch('ansible.module_utils.slurp.open', mock_open, create=True):
        main()
        assert m.exit_json.call_args

# Generated at 2022-06-13 06:15:35.746856
# Unit test for function main
def test_main():
    os.chdir("test/units/modules/core/files/ansible")

    try:
        with open("test.yml", "w") as text_file:
            text_file.write("""- name: Find out what the remote machine's mounts are
  ansible.builtin.slurp:
    src: /proc/mounts
  register: mounts

- name: Print returned information
  ansible.builtin.debug:
    msg: "{{ mounts['content'] | b64decode }}"
""")
        with open("ansible.cfg", "w") as text_file:
            text_file.write("""[defaults]
library = ../../../../../../lib
""")
    except (IOError, OSError) as e:
        print("Error while creating test.yml")



# Generated at 2022-06-13 06:15:41.431023
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

    assert module.params['src'] == 'file_slurp'
    assert module.params['path'] == 'file_slurp'

    source = module.params['src']
    assert source == 'file_slurp'

    source_content = os.path.abspath(__file__)
    assert source_content != ''

    assert not module.fail_json.called

# Generated at 2022-06-13 06:16:37.905458
# Unit test for function main
def test_main():
    # Just be sure we can load this module
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 06:16:49.355194
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

# Generated at 2022-06-13 06:17:02.178983
# Unit test for function main
def test_main():
    # Module os provides the function path.join()
    # Function getcwd() provides the current working directory
    # Function dirname() provides the directory of the path
    # Function basename() provides the final component of the path
    # Module sys provides the function argv which returns
    # the list of command line arguments passed to the script
    # Function join() joins one or more path components intelligently
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
    )
    source = module.params['src']
    
    module.exit_json(content=data, source=source, encoding='base64')

# Generated at 2022-06-13 06:17:06.586311
# Unit test for function main
def test_main():
    original_open_builtin = __builtins__['open']
    def fake_open(filename, mode):
        return original_open_builtin(filename, mode)
    __builtins__['open'] = fake_open

    original_module = __import__('ansible.modules.system.slurp', globals(), locals(), ['AnsibleModule'], 0)
    original_module.AnsibleModule = original_module.AnsibleModule
    module = __import__('ansible.modules.system.slurp', globals(), locals(), ['AnsibleModule'], 0)
    module.AnsibleModule = original_module.AnsibleModule
    module.main()



# Generated at 2022-06-13 06:17:18.284103
# Unit test for function main
def test_main():
    import tempfile
    temp_dir = tempfile.mkdtemp()
    test_file = os.path.join(temp_dir, 'testfile.tmp')
    module = AnsibleModule(argument_spec=dict(
        src=dict(type='path', required=True, aliases=['path']),
        ),
        supports_check_mode=True,
        )

    source = module.params['src']

    with open(test_file, 'w') as doug:
        doug.write('Testing')
        doug.close

    with open(test_file, 'rb') as source_fh:
        source_content = source_fh.read()

    data = base64.b64encode(source_content)

    assert data == b'VGVzdGluZw=='
    os.remove

# Generated at 2022-06-13 06:17:24.510515
# Unit test for function main
def test_main():
    """Unit testing function main"""

    with open('tests/files/file1.txt', 'rb') as main_fh:
        source_content = main_fh.read(20)

    data = base64.b64encode(source_content)


    assert data == "dGVzdCBmaWxlIDEuCg==", "file not found: /var/run/sshd.pid"

# Generated at 2022-06-13 06:17:35.110007
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

# Generated at 2022-06-13 06:17:36.322780
# Unit test for function main
def test_main():
    os.environ["ANSIBLE_CONFIG"] = "ansible.cfg"
    print('Test main does not run as a module')

# Generated at 2022-06-13 06:17:36.855704
# Unit test for function main
def test_main():
    pass

# Generated at 2022-06-13 06:17:41.264016
# Unit test for function main
def test_main():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b'test')

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main(src=f.name)

    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0