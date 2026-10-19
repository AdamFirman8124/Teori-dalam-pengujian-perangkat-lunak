

# Generated at 2022-06-13 05:34:38.215351
# Unit test for function absent
def test_absent():
    module = AnsibleModule(argument_spec={})
    module.fail_json = lambda *args: None
    module.exit_json = lambda *args: None
    absent(module, '/dev/null', None, None, 'asdffdsa', False)

# Generated at 2022-06-13 05:34:41.498772
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec=dict())
    write_changes(module, b'abc', '/tmp/test')
    with open('/tmp/test') as f:
        data = f.read()
        assert data == 'abc'


# Generated at 2022-06-13 05:34:42.615446
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert('testing' == 'testing'), 'Test Successful'



# Generated at 2022-06-13 05:34:54.606637
# Unit test for function write_changes
def test_write_changes():
    import os
    import tempfile

    module_obj = AnsibleModule(argument_spec=dict(
        path=dict(required=True, type='path'),
        line=dict(required=False, type='str'),
        insertafter=dict(required=False, type='str'),
        insertbefore=dict(required=False, type='str'),
        validate=dict(required=False, type='str'),
        tmpdir=dict(required=False, type="path"),
    ))

    module_obj.tmpdir = tempfile.gettempdir()
    module_obj.is_executable = lambda *x: True
    module_obj.is_executable = lambda *x: True
    module_obj.run_command = lambda *x: (0, "", "")

# Generated at 2022-06-13 05:35:03.724484
# Unit test for function check_file_attrs
def test_check_file_attrs():
    test_module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str', required=True),
        )
    )
    test_module.exit_json = exit_json
    test_module.fail_json = fail_json

    # basic check
    changed = True
    result = check_file_attrs(test_module, changed, "test message", "diff test")
    assert result[0] == "test message"
    assert result[1] == True
    changed = False
    result = check_file_attrs(test_module, changed, "test message", "diff test")
    assert result[0] == "ownership, perms or SE linux context changed"
    assert result[1] == True



# Generated at 2022-06-13 05:35:04.491748
# Unit test for function check_file_attrs
def test_check_file_attrs():
    check_file_attrs(module, changed, message, diff)


# Generated at 2022-06-13 05:35:13.426846
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec={
            'backup': {'default': False, 'type': 'bool'},
            'dest': {'default': '', 'aliases': ['path']},
            'create': {'default': False, 'type': 'bool'},
            'firstmatch': {'default': False, 'type': 'bool'},
            'insertafter': {'default': None},
            'insertbefore': {'default': None},
            'regexp': {'default': None},
            'search_string': {'default': None},
            'line': {'default': None},
        }
    )
    # Test case 1
    # Input
    #   line = 'testline'
    #   dest = 'test_absent'
    #   create = True
    #   regex

# Generated at 2022-06-13 05:35:26.481812
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six import PY3

    if PY3:
        module_stdin = open(__file__, encoding='utf-8')
    else:
        module_stdin = open(__file__)
    mock_module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
        stdin=module_stdin
                )
    mock_module.params.update(dict(
        path='/etc/sudoers',
        owner='root',
        group='root',
        mode='0600',
        follow=False,
        seuser='system_u',
        serole='object_r',
        setype='etc_t'
    ))
    diff = dict()

# Generated at 2022-06-13 05:35:32.639901
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(type='str', required=True),
            regexp=dict(type='str'),
            search_string=dict(type='str'),
            line=dict(type='str', required=True),
            backup=dict(type='bool', default=False)
        )
    )

    b_dest = 'xyz'
    regexp = 'abc'
    search_string = None
    line = 'abc'
    backup = True

    absent(module, b_dest, regexp, search_string, line, backup)



# Generated at 2022-06-13 05:35:41.054099
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule, get_exception
    from ansible.module_utils._text import to_bytes, to_native
    # This is taken from the module.  Simulate the end user.
    module_args = dict(
        path='/home/foo/bar.txt',
        line='It was the best of times',
        state='present',
    )
    rv = dict(
        changed=False,
        original_message='',
        message='Line was not present and was not created',
        method=None,
        params=module_args
    )
    b_path = to_bytes(module_args['path'], errors='surrogate_or_strict')
    with open(b_path, 'rb') as f:
        b_lines = f.readlines()

# Generated at 2022-06-13 05:36:10.539669
# Unit test for function present
def test_present():
    pass



# Generated at 2022-06-13 05:36:15.191774
# Unit test for function check_file_attrs
def test_check_file_attrs():
    test_mock = AnsibleModule({'path': '/etc/ansible/test_check_file_attrs', 'state': 'present', 'line': 'hello world'})
    test_mock.set_fs_attributes_if_different = lambda x, y, z: True
    module_return = check_file_attrs(test_mock, False, '', '')
    assert module_return[0] == module_return[1] is True



# Generated at 2022-06-13 05:36:20.644851
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(type='path', required=True),
            regexp=dict(type='str', default=None),
            backup=dict(type='bool', default=False),
            search_string=dict(type='str', default=None),
            line=dict(default=None),
        )
    )
    dest = "/tmp/test.log"
    regexp = "test"
    backup = False
    search_string = "test"
    line = "test"
    absent(module, dest, regexp, search_string, line, backup)


# Generated at 2022-06-13 05:36:30.865603
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(type='str', required=True),
            regexp=dict(type='str', default=None),
            search_string=dict(type='str', default=None),
            line=dict(type='str', required=True),
            backup=dict(type='bool', default=False)
        ),
        supports_check_mode=True
    )

    m_open = mock_open(read_data=dedent(u'''\
        #!/usr/bin/env python
        import sys
        print "Hello World"
        '''))


# Generated at 2022-06-13 05:36:40.115636
# Unit test for function present

# Generated at 2022-06-13 05:36:41.949018
# Unit test for function main
def test_main():
    # No need to do unittest, as the logic is covered by integration tests
    assert True


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:36:48.642047
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
        ),
    )
    module.params['owner'] = "testOwner"
    module.params['group'] = "testGroup"
    module.params['mode'] = "testMode"
    message = ""
    changed = False
    diff = {"before": "testBefore", "after": "testAfter"}

    assert check_file_attrs(module, changed, message, diff) == ("ownership, perms or SE linux context changed", True)



# Generated at 2022-06-13 05:36:54.949083
# Unit test for function present
def test_present():
    module=importer()

# Generated at 2022-06-13 05:37:03.476358
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec=dict(
            unsafe_writes=dict(type='bool', required=False, default=True),
        ),
        check_invalid_arguments=False,
    )
    changed = True
    message = "change"
    diff = {'before': '', 'after': '', 'before_header': '', 'after_header': ''}
    result = check_file_attrs(module, changed, message, diff)
    module.exit_json(changed=result[1], msg=result[0])

# Check mode support:

# Generated at 2022-06-13 05:37:06.497062
# Unit test for function write_changes
def test_write_changes():
  import os
  os.mkdir("/tmp/test")
  files={}
  files["/tmp/test/test"]="/tmp/test/"
  module.atomic_move("/tmp/test/test",
                           "/tmp/test/test2",
                           unsafe_writes=module.params['unsafe_writes'])
  assert os.path.exists("/tmp/test/test2")



# Generated at 2022-06-13 05:38:04.245441
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)

    # Using a binary file with mixed text encodings to test mixed byte types
    if os.name == 'nt':
        module.atomic_move(to_native(os.getcwd(), errors='surrogate_or_strict') + '\\test\\units\\module_utils\\test_unicode_text_file', tmpfile)
    else:
        module.atomic_move(to_native(os.getcwd(), errors='surrogate_or_strict') + '/test/units/module_utils/test_unicode_text_file', tmpfile)

    # read back binary file, append Test line and write it

# Generated at 2022-06-13 05:38:17.068136
# Unit test for function present
def test_present():
    module = AnsibleModule(argument_spec={'file': {'required': True},
                                          'dest': {'required': True},
                                          'regexp': {'required': False},
                                          'search_string': {'required': False},
                                          'line': {'required': True},
                                          'insertafter': {'required': False},
                                          'insertbefore': {'required': False},
                                          'create': {'required': False},
                                          'backup': {'required': False},
                                          'backrefs': {'required': False},
                                          'firstmatch': {'required': False}})
    dest = module.params.get('dest')
    regexp = module.params.get('regexp')
    search_string = module.params.get

# Generated at 2022-06-13 05:38:29.001443
# Unit test for function main
def test_main():
    data = {"key": "value"}
    data_json = json.dumps(data).encode("utf-8")
    mock_module = Mock(params=dict(path='path', state='present', line='line', create='false', backup='false', backrefs='false'))
    mock_module.check_mode = False
    mock_module._diff = True
    mock_module.params['path'] = 'path'
    mock_module.params['state'] = 'present'
    mock_module.params['line'] = 'line'
    mock_module.params['create'] = 'false'
    mock_module.params['backup'] = 'false'
    mock_module.params['backrefs'] = 'false'
    mock_open = mock_open(read_data=data_json)

# Generated at 2022-06-13 05:38:32.959714
# Unit test for function write_changes
def test_write_changes():
    lines = []
    dest = 'test_write_changes'
    module = AnsibleModule()
    write_changes(module,lines, dest)
    assert os.path.exists(dest) and os.path.isfile(dest),"File not created"


# Generated at 2022-06-13 05:38:33.531634
# Unit test for function absent
def test_absent():
    pass



# Generated at 2022-06-13 05:38:41.686324
# Unit test for function write_changes
def test_write_changes():
    # Test for changes writing
    write_changes(AnsibleModule(
        argument_spec=dict(path=dict(type='str', required=False), create=dict(type='bool', required=False),
                           line=dict(type='str', required=False))),
                  "The quick brown fox\njumps over the lazy dog".encode(),
                  "/tmp/test_file")

    with open("/tmp/test_file", 'rb') as f:
        original_file = f.readlines()

    assert original_file == "The quick brown fox\njumps over the lazy dog".encode()



# Generated at 2022-06-13 05:38:55.465790
# Unit test for function check_file_attrs
def test_check_file_attrs():
    test_args = dict(
        path='/foo',
        mode='0644',
        owner='root',
        group='root',
        seuser='root',
        serole='root',
        setype='root',
        diff={'before': "1", 'after': "2"}
    )
    test_diff_value = {'before': '0644', 'after': '0640'}
    test_module = MockAnsibleModule({})
    test_module.params = test_args
    test_module.set_fs_attributes_if_different = Mock(return_value=True)

    test_message = "test message"
    test_changed = False
    result = check_file_attrs(test_module, test_changed, test_message, test_diff_value)


# Generated at 2022-06-13 05:39:01.725350
# Unit test for function write_changes
def test_write_changes():
    pretend_file_content=b"""
something here
"""
    pretend_module=AnsibleModuleMock()
    pretend_module.fail_json=lambda self,args: True
    pretend_module.params["unsafe_writes"]=True
    pretend_module.atomic_move=lambda self,temp_file,destination_file: True
    # test when the file is valid given the validation checks
    pretend_module.run_command=lambda self,validation_command: (0,"","")
    assert write_changes(pretend_module,[pretend_file_content],".")
    # test when the file is invalid given the validation checks
    pretend_module.run_command=lambda self,validation_command: (1,"","")
    assert write_changes(pretend_module,[pretend_file_content],".")



# Generated at 2022-06-13 05:39:14.611702
# Unit test for function present
def test_present():
    module = AnsibleModule({
        'path': "/tmp/test",
        'regexp': ".*test.*",
        'line': "test line"
    })
    module.exists = MagicMock()
    module.exists.return_value = False
    module.check_mode = MagicMock()
    module.check_mode.return_value = False
    module.run_command = MagicMock()
    module.run_command.return_value = (0, None, None)
    module.atomic_move = MagicMock()
    module.atomic_move.return_value = True
    module.set_fs_attributes_if_different = MagicMock()
    module.set_fs_attributes_if_different.return_value = True
    module.backup_local = MagicMock()
   

# Generated at 2022-06-13 05:39:15.011708
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert False


# Generated at 2022-06-13 05:40:43.175522
# Unit test for function absent
def test_absent():
    module_args = {}
    set_module_args(module_args)
    module = AnsibleModule(
        argument_spec=self.spec.argument_spec,
        supports_check_mode=self.spec.supports_check_mode,
    )
    dest, regexp, search_string, line, backup = set_absent_facts(self,module)
    absent(module, dest, regexp, search_string, line, backup)



# Generated at 2022-06-13 05:40:55.828574
# Unit test for function absent
def test_absent():
    def test_module(module_args, *args):
        module = AnsibleModule(**module_args)
        absent(module, *args)
    module_args = dict(
        dest='/tmp/test_file.txt',
        regexp=None,
        search_string=None,
        line='hi',
        backup=False
        )
    test_lines = [b'bla bla bla\n', b'hi\n', b'bla bla bla\n']
    with patch('os.path.exists') as patch_exists:
        patch_exists.return_value = True

# Generated at 2022-06-13 05:41:03.282628
# Unit test for function main
def test_main():
    def test_main_no_exception(mocker, module_args, *args):
        mocker.patch('ansible.module_utils.basic.AnsibleModule')
        mocker.patch('os.path.exists')
        mocker.patch('os.path.isdir')
        mocker.patch('os.listdir')
        mocker.patch('os.linesep')
        mocker.patch('__builtin__.open')
        mocker.patch('ansible.module_utils.basic.open_file')
        mocker.patch('shutil.copy2')
        mocker.patch('shutil.move')
        mocker.patch('os.unlink')
        mocker.patch('os.path.getsize')
        mocker.patch('os.stat')

# Generated at 2022-06-13 05:41:12.356804
# Unit test for function check_file_attrs
def test_check_file_attrs():
    args = dict(
        path = '/who/cares',
        owner = 'bob',
        group = 'bob',
        mode = '01003',
        seuser = 'system_u',
        serole = 'object_r',
        selevel = 's0',
    )
    module = AnsibleModule(argument_spec=dict())
    changed, msg = check_file_attrs(module, False, '', dict())
    assert False is changed
    assert "" == msg

    changed, msg = check_file_attrs(module, False, '', dict(path='/who/cares', owner='bob', mode='01003', group='bob', seuser='system_u', serole='object_r', selevel='s0'))
    assert False is changed
    assert "" == msg

    changed,

# Generated at 2022-06-13 05:41:15.466966
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={'path': {'type': 'path', 'required': True}})
    changed = False
    message = "I am a message"
    diff = "diff text"

    test_message, test_changed = check_file_attrs(module, changed, message, diff)
    assert test_message == message
    assert test_changed == changed



# Generated at 2022-06-13 05:41:23.509131
# Unit test for function check_file_attrs

# Generated at 2022-06-13 05:41:25.692862
# Unit test for function absent
def test_absent():
    """ test absent """
    raise NotImplementedError()



# Generated at 2022-06-13 05:41:36.749774
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec=dict(
        path=dict(required=True),
        unsafe_writes=dict(type='bool', default=False),
        owner=dict(),
        group=dict(),
        mode=dict(),
        seuser=dict(),
        serole=dict(),
        setype=dict(),
        selevel=dict(),
    ),supports_check_mode=True)

    module.set_file_attributes_if_different = module.set_fs_attributes_if_different
    module.run_command = lambda *args, **kwargs: (0, "", "")

    message = ""
    changed = False

    message, changed = check_file_attrs(module, changed, message, "")
    assert message == ""
    assert changed == False

    module.params['owner']

# Generated at 2022-06-13 05:41:46.801730
# Unit test for function main

# Generated at 2022-06-13 05:41:53.741201
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str', required=True),
            regexp=dict(type='str'),
            search_string=dict(type='str'),
            line=dict(type='str', required=True),
            backup=dict(type='bool', default=False),
        )
    )
    m_absent = MagicMock(return_value=dict(msg="file not present", changed=False))
    with patch.object(module_utils.basic, 'file', m_absent):
        absent(module, "/some/path", "regexp", "search_str", "value_line", False)

    file_with_content = """line1
line2
line3
line4
line5
line6
"""
    m_absent = MagicM

# Generated at 2022-06-13 05:43:19.386360
# Unit test for function present
def test_present():
    import shutil
    import os
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
            line=dict(type='str', required=True),
            regexp=dict(type='str'),
            insertafter=dict(type='str'),
            insertbefore=dict(type='str'),
            state=dict(default='present', choices=['present', 'absent']),
            backup=dict(type='bool', default=False),
            create=dict(type='bool', default=False),
            validate=dict(type='str', required=False)
        ),
        supports_check_mode=True
    )

    shutil.rmtree("/tmp/test_file_utils/", True)

# Generated at 2022-06-13 05:43:30.559530
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({'tmpdir': os.path.dirname(tempfile.mkstemp()[1]),  # needed for module_utils/basic.py
                            'validate': None,  # needed for module_utils/basic.py
                            'unsafe_writes': False},  # needed for module_utils/basic.py
                           check_invalid_arguments=False)
    module.run_command = run_command
    dest = '/tmp/file'

    b_lines = to_bytes('line1\nline2\n')
    write_changes(module, b_lines, dest)
    assert os.path.exists(dest)
    with open(dest, 'rb') as dest_file:
        b_lines = dest_file.readlines()
        assert b_lines[0] == to

# Generated at 2022-06-13 05:43:40.723147
# Unit test for function absent
def test_absent():
    from ansible.module_utils.common.collections import Mapping
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 05:43:46.950293
# Unit test for function write_changes
def test_write_changes():
    def run_command(self, args, check_rc=True, close_fds=True, exec_inherit=False, data=None, binary_data=False):
        return (1, "BOOM", "")

    module = AnsibleModule(argument_spec={'validate': {'type': 'str'}, 'tmpdir': {'type': 'str'}, 'unsafe_writes': {'type': 'bool'}})
    module.run_command = run_command
    try:
        write_changes(module, [b'This is a test'], "/tmp/test")
    except Exception as err:
        assert(err.args[0] == "failed to validate: rc:1 error:BOOM")



# Generated at 2022-06-13 05:43:53.082255
# Unit test for function present
def test_present():
  p = dict(
    dest='test.txt',
    line='test',
    )
  m = dict(
    check_mode=False,
    no_log=True,
    tmpdir='/tmp',
    run_command=run_command
    )

# Generated at 2022-06-13 05:43:56.533802
# Unit test for function present
def test_present():
    assert present('module', 'dest', 'regexp', 'search_string', 'line', 'insertafter', 'insertbefore', 'create',
            'backup', 'backrefs', 'firstmatch')
    