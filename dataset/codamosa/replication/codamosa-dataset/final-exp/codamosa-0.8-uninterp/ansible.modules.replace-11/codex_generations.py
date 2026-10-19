

# Generated at 2022-06-13 05:59:50.039500
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={})
    module.params = {'path': '/tmp/test_file', 'owner': 'test', 'group': 'test'}
    setattr(module, '_execute_module', lambda *args: None)
    module.run_command = lambda *args, **kwargs: (0, '', '')
    changed = False
    message = 'message'
    message, changed = check_file_attrs(module, changed, message)
    assert message == 'message and ownership, perms or SE linux context changed'



# Generated at 2022-06-13 05:59:56.445122
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec={
            'path': {'type': 'path', 'required': True},
            'owner': {'type': 'str', 'default': 'root'},
            'group': {'type': 'str', 'default': 'root'},
            'mode': {'type': 'str', 'default': '0644'},
            'seuser': {'type': 'str', 'default': 'system_u'},
            'serole': {'type': 'str', 'default': 'object_r'},
            'setype': {'type': 'str', 'default': 'etc_t'},
            'selevel': {'type': 'str', 'default': 's0'}
        }
    )

# Generated at 2022-06-13 06:00:07.573013
# Unit test for function write_changes
def test_write_changes():
    with mock.patch('ansible.module_utils.basic.AnsibleModule') as mock_module:
        mock_module.run_command = MagicMock()
        mock_module.run_command.return_value = (0, '', '')
        mock_module.atomic_move = MagicMock()
        tmpfd = MagicMock()
        tmpfile = 'test_write_changes'
        f = 'write_changes'
        with mock.patch('tempfile.mkstemp', return_value=[tmpfd, tmpfile]) as mock_tempfile:
            with mock.patch('os.fdopen', return_value=f) as mock_fdopen:
                write_changes(mock_module, 'contents', 'path')

# Generated at 2022-06-13 06:00:14.111123
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import ansible_posix_default_common
    # read_config was not defined in earlier versions of this module
    # so we add it here so we can use it in older unit tests
    # https://github.com/ansible/ansible-modules-core/commit/5821d3954955f9e1e7c3361683314c69e01d8f2b
    def read_config(module, result, where, config_type=None, key=None, match=None, all_results=False, include_errors=True, expand_vars=True, ignore_includes=False):
        return
    setattr(basic, 'read_config', read_config)

# Generated at 2022-06-13 06:00:18.954061
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True, aliases=['dest', 'destfile', 'name']),
            regexp=dict(type='str', required=True),
            replace=dict(type='str', default=''),
            after=dict(type='str'),
            before=dict(type='str'),
            backup=dict(type='bool', default=False),
            validate=dict(type='str'),
            encoding=dict(type='str', default='utf-8'),
        ),
        add_file_common_args=True,
        supports_check_mode=True,
    )
    res_args = {}
    params = module.params
    path = params['path']
    encoding = params['encoding']
    res_args = dict()



# Generated at 2022-06-13 06:00:25.041498
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    module = basic.AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True, aliases=['dest', 'destfile', 'name']),
            regexp=dict(type='str', required=True),
            replace=dict(type='str', default=''),
            after=dict(type='str'),
            before=dict(type='str'),
            backup=dict(type='bool', default=False),
            validate=dict(type='str'),
            encoding=dict(type='str', default='utf-8'),
        ),
        supports_check_mode=True,
    )

    params = module.params
    path = params['path']

# Generated at 2022-06-13 06:00:25.892003
# Unit test for function main
def test_main():
    res = main()

# Generated at 2022-06-13 06:00:33.895015
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class module(object):
        params = {'path': 'file'}
        def set_file_attributes_if_different(self, file_args, changed):
            return changed
        def load_file_common_arguments(self, params):
            return params
    module.params['path'] = 'file'
    assert check_file_attrs(module, True, '') == ('ownership, perms or SE linux context changed', True)
    module.params['path'] = 'file'
    assert check_file_attrs(module, False, '') == ('ownership, perms or SE linux context changed', True)



# Generated at 2022-06-13 06:00:34.894766
# Unit test for function check_file_attrs
def test_check_file_attrs():
    check_file_attrs()



# Generated at 2022-06-13 06:00:42.939466
# Unit test for function check_file_attrs
def test_check_file_attrs():
    test_module = AnsibleModule({})
    message = "No change"
    changed = False
    file_args = {
        "path": "/tmp/test_file",
        "mode": "0644",
        "owner": "root",
        "group": "root",
        "selevel": "s0"
    }
    test_module.set_file_attributes_if_different = lambda x, y: True
    assert check_file_attrs(test_module, changed, message) == ("No change and ownership, perms or SE linux context changed", True)
    assert check_file_attrs(test_module, changed, message) == ("No change and ownership, perms or SE linux context changed", True)


# Generated at 2022-06-13 06:01:04.762643
# Unit test for function write_changes
def test_write_changes():
    # Setup test vars
    tmpfd, tmpfile = tempfile.mkstemp()
    os.write(tmpfd, bytes('test_write_changes\n', 'utf-8'))
    os.close(tmpfd)
    module = AnsibleModule(argument_spec={'path': dict(), 'validate': dict()})
    module.atomic_move = lambda src, dest, unsafe_writes: dest
    module.params['unsafe_writes'] = False
    module.run_command = lambda cmd: (0, '', '')
    # Test file creation
    write_changes(module, 'testing', tmpfile)
    with open(tmpfile, 'r') as f:
        contents = f.read()
    assert contents == 'testing\n'
    # Test validation

# Generated at 2022-06-13 06:01:14.316323
# Unit test for function write_changes
def test_write_changes():
  module = AnsibleModule(
    argument_spec=dict(
      validate=dict(required=False, default=None),
      path=dict(required=True, type='str'),
      contents=dict(required=True, type='str'),
      unsafe_writes=dict(required=False, default=True, type='bool'),
      tmpdir=dict(required=True, type='str'),
    ),
    mutually_exclusive=[],
    supports_check_mode=True
  )
  path = '/tmp/test_file.txt'
  tmpdir = '/tmp'
  contents = '''
  test
  '''
  write_changes(module, contents, path)

# Unit test function test_write_changes
test_write_changes()


# ===========================================
# Main control flow


# Generated at 2022-06-13 06:01:14.851022
# Unit test for function main
def test_main():
    assert True
# Unit test to implement

# Generated at 2022-06-13 06:01:21.931317
# Unit test for function write_changes
def test_write_changes():
    '''
    Unit test for function write_changes
    '''
    # Mock module
    module = FakeAnsibleModule()
    module.read_file.return_value = "123"
    module.atomic_move = fake_atomic_move
    # Call write_changes with known file content
    write_changes(module, "456", "file")
    # Check results
    module.run_command.assert_called_with("wc -c < file")
    module.atomic_move.assert_called_with("tmp_file", "file", unsafe_writes=False)


# Generated at 2022-06-13 06:01:28.759784
# Unit test for function write_changes
def test_write_changes():
    # Prepare mocks
    my_module = AnsibleModule(argument_spec={}, skip_checks=True)
    my_module.tmpdir = '/tmp/'
    my_module.params = { 'validate': None, 'unsafe_writes': False }
    def my_run_command(cmd, check_rc=True):
        pass
    my_module.run_command = my_run_command
    def my_atomic_move(src, dest, unsafe_writes=False):
        pass
    my_module.atomic_move = my_atomic_move
    def my_fail_json(msg):
        pass
    my_module.fail_json = my_fail_json

    # Create necessary files
    test_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 06:01:34.721679
# Unit test for function write_changes
def test_write_changes():
    """
    This is a test for the write_changes method
    """
    module = AnsibleModule({})
    path = '/tmp/gen'
    contents = 'content'
    try:
        write_changes(module, contents, path)
        with open(path, 'r') as f:
            contents = f.read()
            assert contents == 'content'
    finally:
        os.unlink(path)


# Generated at 2022-06-13 06:01:43.290449
# Unit test for function check_file_attrs
def test_check_file_attrs():
    import ansible.module_utils.basic
    mm = ansible.module_utils.basic.AnsibleModule(
        argument_spec = dict(
            path = dict(type='str'),
            owner = dict(type='str'),
            group = dict(type='str'),
            mode = dict(type='str'),
        ),
    )
    mm.params = dict(path='path', owner='owner', group='group', mode='mode')
    mm.run_command = lambda x: (0, '', '')
    mm.set_file_attributes = lambda x, y: True
    changed = False
    message = ''
    message, changed = check_file_attrs(mm, changed, message)
    assert changed

    mm.set_file_attributes = lambda x, y: False
    message, changed = check_

# Generated at 2022-06-13 06:01:55.978025
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class ModuleTest(object):
        def __init__(self):
            self.params = {}
            self.atomic_move = None
            self.run_command = None
            self.fail_json = None
            self.set_file_attributes_if_different = None

        def load_file_common_arguments(self, params):
            return dict(path=params['path'])

    # File attributes always changed
    module_test = ModuleTest()
    changed = False
    message = ""
    module_test.params = dict(path='/tmp/test/path')
    return_message = 'ownership, perms or SE linux context changed'
    module_test.set_file_attributes_if_different = lambda file_args, tmp: True

# Generated at 2022-06-13 06:02:09.393438
# Unit test for function main
def test_main():
    import os
    import re
    import tempfile
    from traceback import format_exc
    from ansible.module_utils._text import to_text, to_bytes
    from ansible.module_utils.basic import AnsibleModule

    
    

    
    
    
    
    
    
    
    
    
    
    


# Generated at 2022-06-13 06:02:16.669225
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import common
    from ansible.module_utils.common import set_module_args
    from ansible.module_utils._text import to_bytes
    import tempfile
    import os

    path = os.path.join(tempfile.mkdtemp(), "test.tmp")

# Generated at 2022-06-13 06:02:42.485762
# Unit test for function main
def test_main():
    path = 'dummy.txt'
    encoding = 'utf-8'
    res_args = dict()

    params = {}
    params['after'] = 'some expression'
    params['before'] = 'some other expression'
    params['regexp'] = ''
    params['replace'] = ''
    params['path'] = path
    params['encoding'] = encoding
    params['backup'] = False
    params['validate'] = None
    params['dest'] = path
    params['destfile'] = path
    params['name'] = path
    params['validate'] = None
    if os.path.isdir(path):
        raise Exception('Path %s is a directory !' % path)
    if not os.path.exists(path):
        raise Exception('Path %s does not exist !' % path)


# Generated at 2022-06-13 06:02:48.075032
# Unit test for function main
def test_main():
   test_args = {}
   test_args['path'] = '/test/file'
   test_args['backup'] = False
   test_args['regexp'] = 'test'
   test_args['replace'] = 'test'
   test_args['validate'] = 'test'
   test_args['encoding'] = 'utf-8'
   module = AnsibleModule(argument_spec=test_args)
   
   main()

# Generated at 2022-06-13 06:02:59.198197
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.modules.files import replace
    from ansible.modules.files import file
    from ansible.module_utils._text import to_text


# Generated at 2022-06-13 06:03:06.957424
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class MockModule(object):
        params = dict()
        def fail_json(self, msg):
            return msg
        def load_file_common_arguments(self, params):
            return params
        def set_file_attributes_if_different(self, file_args, changed):
            return True
    module = MockModule()
    assert check_file_attrs(module, False, 'message') == ('message and ownership, perms or SE linux context changed', True)
    assert not check_file_attrs(module, True, 'message') == ('message and ownership, perms or SE linux context changed', True)


# Generated at 2022-06-13 06:03:13.172787
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={})
    module.set_file_attributes_if_different = lambda x: True
    module.params['path'] = 'foo'
    message, changed = check_file_attrs(module, False, '')
    assert message == 'ownership, perms or SE linux context changed'
    assert changed



# Generated at 2022-06-13 06:03:21.327938
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.module_utils.basic import AnsibleModule
    class FakeModule(AnsibleModule):
        def fail_json(self, *a, **b):
            raise Exception("fail_json called: %s %s" % (a, b))
        def exit_json(self, *a, **b):
            raise Exception("exit_json called: %s %s" % (a, b))
        def set_file_attributes_if_different(self, *a):
            # mock this function
            return True
    module = FakeModule(
        argument_spec=dict(path=dict(type='path'), test=dict(type='bool')),
        supports_check_mode=True,
        params={'path': '/some/path'}
    )

# Generated at 2022-06-13 06:03:28.514516
# Unit test for function write_changes
def test_write_changes():
    test_module = AnsibleModule(argument_spec={})
    test_module.atomic_move = lambda *args: None
    test_module.params['unsafe_writes'] = True
    # variable for function to write to
    contents = b'#testing'
    path = '/'
    try:
        write_changes(test_module, contents, path)
    except SystemExit:
        assert False, "write_Changes() failed with SystemExit exception"
    assert True



# Generated at 2022-06-13 06:03:37.699335
# Unit test for function main
def test_main():
    import ansible.utils.template as template
    from ansible.inventory.manager import InventoryManager
    from ansible.parsing.dataloader import DataLoader
    from ansible.vars.manager import VariableManager
    from ansible.playbook.play import Play

    loader = DataLoader()
    inventory = InventoryManager(loader=loader, sources=('localhost,'))
    variable_manager = VariableManager(loader=loader, inventory=inventory)


# Generated at 2022-06-13 06:03:47.663724
# Unit test for function write_changes
def test_write_changes():
    mock_module = AnsibleModule({})
    contents = "Test contents"
    path = "path.txt"
    mock_module.params['validate'] = "validate"
    mock_module.run_command = Mock(return_value=(0, "", ""))
    mock_module.atomic_move = Mock()
    write_changes(mock_module, contents, path)
    mock_module.run_command.assert_called_with(mock_module.params['validate'])
    mock_module.run_command.assert_called_with(mock_module.params['validate'])
    mock_module.atomic_move.assert_called_with(mock_module.tmpdir + "/tmp", path, False)


# Generated at 2022-06-13 06:03:56.701594
# Unit test for function write_changes
def test_write_changes():
    m = AnsibleModule({})
    m.tmpdir = '/tmp'
    m.params['unsafe_writes'] = True
    m.atomic_move = lambda src, dest, unsafe_writes: dest
    test_data = "test-data"
    test_path = "/tmp/test_path"
    test_write_changes = write_changes(m, test_data, test_path)
    assert test_write_changes == test_path



# Generated at 2022-06-13 06:04:32.323798
# Unit test for function main
def test_main():

    module_args = dict(
        path="/home/daniel/.ssh/known_hosts",
        regexp='^old\.host\.name[^\n]*\n',
        owner="daniel",
        group="daniel",
        mode="0664"
    )
    # TODO: fix verify_file_attrs
    #p = AnsibleModule(
    #    argument_spec=dict(
    #        path=dict(required=True, type='path'),
    #        regexp=dict(required=True, type='str'),
    #        replace=dict(required=False, type='str'),
    #        after=dict(required=False, type='str'),
    #        before=dict(required=False, type='str'),
    #        backup=dict(required=False, type='bool'),
    #

# Generated at 2022-06-13 06:04:36.873844
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(aliases=['dest', 'destfile', 'name'], type='path', required=True),
            follow=dict(type='bool', required=False, default=False),
            mode=dict(type='raw', required=False),
            owner=dict(type='raw', required=False),
            group=dict(type='raw', required=False),
            seuser=dict(type='str', required=False),
            serole=dict(type='str', required=False),
            selevel=dict(type='str', required=False),
            setype=dict(type='str', required=False),
        ),
        add_file_common_args=True,
        supports_check_mode=True,
    )
    changed=False
    message

# Generated at 2022-06-13 06:04:47.765129
# Unit test for function write_changes
def test_write_changes():
    """Unit test for write_changes"""
    module = AnsibleModuleStub({
        "path" : "file_name",
        "regexp": "regex_exp",
        "replace": "replace_string",
        "unsafe_writes": "True"
    })
    fd, file_name = tempfile.mkstemp(dir=".")
    f = os.fdopen(fd, 'w')
    f.write("Test string")
    f.close()
    write_changes(module, "Test string", file_name)
    f = open(file_name, 'r')
    test_string = f.read()
    f.close()
    os.remove(file_name)
    assert module.fail_json.called == False
    assert test_string == "Test string"

test_write

# Generated at 2022-06-13 06:04:51.025336
# Unit test for function main
def test_main():
    print("Test main()")
    main()

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 06:04:59.619743
# Unit test for function main
def test_main():
    path = 'examples/files/main.yml'
    args = dict(
          path='examples/files/main.yml',
          regexp='^(ListenAddress[ ]+)[^\\n]+$',
          replace='\g<1>0.0.0.0',
          encoding='utf-8',
        )

# Generated at 2022-06-13 06:05:00.627216
# Unit test for function write_changes
def test_write_changes():
    # TODO: implement
    pass


# Generated at 2022-06-13 06:05:04.035091
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule()
    setattr(module, 'set_file_attributes_if_different', lambda a, b: True)
    changed, message = False, 'baba'
    message, changed = check_file_attrs(module, changed, message)
    assert changed



# Generated at 2022-06-13 06:05:11.068171
# Unit test for function main
def test_main():
    """Unit test for function main"""

    # load the module and its arguments.
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True, aliases=['dest', 'destfile', 'name']),
            regexp=dict(type='str', required=True),
            replace=dict(type='str', default=''),
            after=dict(type='str'),
            before=dict(type='str'),
            backup=dict(type='bool', default=False),
            validate=dict(type='str'),
            encoding=dict(type='str', default='utf-8'),
        ),
        add_file_common_args=True,
        supports_check_mode=True,
    )
    # define return dictionary
    result = dict()

    # set default values for return dictionary

# Generated at 2022-06-13 06:05:22.937468
# Unit test for function check_file_attrs
def test_check_file_attrs():
    tempdir = tempfile.mkdtemp()
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode = True
    )
    module.tmpdir = tempdir
    module._handle_aliases = lambda x: x
    module.params = {
        'unsafe_writes': False
    }
    file_args = dict(path = '/tmp/test_file', owner = 'root', group = 'root', mode = '0644', seuser = 'root', serole='root', setype='user_home_t', selevel='s0')
    module.set_file_attributes_if_different = lambda file_args, unsafe_writes: True
    message, changed = check_file_attrs(module, False, "Attribs")
    assert changed == True

# Generated at 2022-06-13 06:05:33.965331
# Unit test for function write_changes
def test_write_changes():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec=dict(
        test=dict(type='bool')
    ))
    path = tempfile.mktemp()
    contents = b'a'
    tmpfile = tempfile.mkstemp(dir=tempfile.gettempdir())[1]
    f = os.fdopen(tmpfile, 'wb')
    f.write(contents)
    f.close()
    try:
        write_changes(module, contents, path)
        assert os.path.exists(path)
        assert(len(open(path).read()) == 1)
    except:
        module.fail_json(msg='failed to write_changes')
    finally:
        os.remove(path)
        os.remove(tmpfile)



# Generated at 2022-06-13 06:06:30.844631
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={'path': dict(required=True, type='path'), 'unsafe_writes': dict(required=False, type='bool', default=False)})
    path = module.params['path']
    contents = to_bytes('asdf')
    write_changes(module, contents, path)
    assert module.read_file(path) == contents
    os.unlink(path)
    module = AnsibleModule(argument_spec={'path': dict(required=True, type='path'), 'unsafe_writes': dict(required=False, type='bool', default=True)})
    write_changes(module, contents, path)
    assert module.read_file(path) == contents
    os.unlink(path)


# Generated at 2022-06-13 06:06:38.319836
# Unit test for function write_changes
def test_write_changes():
    m = AnsibleModule(argument_spec=dict(
        path=dict(type='path'),
        contents=dict(type='str', default=''),
        unsafe_writes=dict(type='bool', default=False)
    ))
    write_changes(m, "test", "/tmp/test")
    f = open("/tmp/test", 'r')
    assert f.read() == "test"
    f.close()



# Generated at 2022-06-13 06:06:48.536354
# Unit test for function check_file_attrs
def test_check_file_attrs():
    temp_file = tempfile.NamedTemporaryFile()
    module = AnsibleModule(argument_spec=dict(path=dict(required=True, type='path'),
                                              owner=dict(required=True, aliases=['user']),
                                              group=dict(default=None),
                                              mode=dict(default=None),
                                              seuser=dict(default=None),
                                              serole=dict(default=None),
                                              selevel=dict(default=None),
                                              setype=dict(default=None)))
    # set module.params['path'] to the temp file before calling
    # check_file_attrs(), otherwise AnsibleModule.set_file_attributes_if_different()
    # will return false.
    module.params['path'] = temp_file.name
   

# Generated at 2022-06-13 06:06:50.189289
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert (check_file_attrs(None, False, "message")) == ("message and ownership, perms or SE linux context changed", True)



# Generated at 2022-06-13 06:07:01.260884
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True, aliases=['dest', 'destfile', 'name']),
            regexp=dict(type='str', required=True),
            replace=dict(type='str', default=''),
            after=dict(type='str'),
            before=dict(type='str'),
            backup=dict(type='bool', default=False),
            validate=dict(type='str'),
            encoding=dict(type='str', default='utf-8'),
        ),
        add_file_common_args=True,
        supports_check_mode=True,
    )

    params = module.params
    path = params['path']
    encoding = params['encoding']
    res_args = dict()

    params['after'] = to

# Generated at 2022-06-13 06:07:08.739536
# Unit test for function write_changes
def test_write_changes():
    result = dict(
        changed=False,
        diff=dict(before='', after='', before_header='', after_header='', before_header_lines=['#'], after_header_lines=['#'])
    )
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
            unsafe_writes=dict(type='bool', default=False)
        )
    )
    write_changes(module, b"new file", './test_file')
    f = open('./test_file', 'rb')
    file_contents = f.read()
    f.close()
    assert file_contents == b"new file"
    os.unlink('./test_file')


# Generated at 2022-06-13 06:07:09.337603
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 06:07:13.831601
# Unit test for function main
def test_main():
    orig_stdin = sys.stdin
    tmp_fd, tmp_file = tempfile.mkstemp()
    args.path = tmp_file
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True, aliases=['dest', 'destfile', 'name']),
            regexp=dict(type='str', required=True),
            replace=dict(type='str', default=''),
            after=dict(type='str'),
            before=dict(type='str'),
            backup=dict(type='bool', default=False),
            validate=dict(type='str'),
            encoding=dict(type='str', default='utf-8'),
        ),
        add_file_common_args=True,
        supports_check_mode=True,
    )

# Generated at 2022-06-13 06:07:14.404531
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert True



# Generated at 2022-06-13 06:07:20.860185
# Unit test for function write_changes
def test_write_changes():
    import os

    # Create a temp directory
    tmpdir = tempfile.mkdtemp()
    path = "%s/test_file.txt" % tmpdir

    # Create the file, then remove it
    test_str = "test_write_changes()"
    f = open(path, 'wb')
    f.write(test_str)
    f.close()
    os.remove(path)

    # Run the function, then test for success
    module = AnsibleModule(tmpdir=tmpdir)
    write_changes(module, to_bytes(test_str), path)
    f = open(path, 'rb')
    read_str = to_text(f.read())
    f.close()
    assert read_str == test_str
    os.remove(path)

    # Clean up the temp directory
   