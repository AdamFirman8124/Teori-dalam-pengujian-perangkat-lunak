

# Generated at 2022-06-13 05:34:36.894013
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True, type='path'),
        ),
    )
    diff = {}
    msg = ""
    changed = False
    assert (check_file_attrs(module, changed, msg, diff) == ('ownership, perms or SE linux context changed', True))

    module.params[u'path'] = None
    assert (check_file_attrs(module, changed, msg, diff) == ('ownership, perms or SE linux context changed', True))


# Generated at 2022-06-13 05:34:46.046236
# Unit test for function check_file_attrs
def test_check_file_attrs():
    """Unit test for function ``check_file_attrs``"""

    # pylint: disable=anomalous-backslash-in-string
    # pylint: disable=import-error
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule({
        'content': 'test',
        'path': '/tmp/test.txt',
        'dest': '/tmp/test.txt',
    })

    module.atomic_move = lambda x, y, z=False: None
    module.set_fs_attributes_if_different = lambda x, y, z=False, diff=False: True
    module.exit_json = lambda x: False

    try:
        check_file_attrs(module, False, "", False)
    except SystemExit:
        pass


# Generated at 2022-06-13 05:34:54.909853
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    changed = False
    message = ''

    path = '/var/tmp/file'
    file_args = module.load_file_common_arguments(module.params)
    diff = {
        'after': path,
        'before': path,
        'before_header': '',
        'after_header': ''
    }

    if module.set_fs_attributes_if_different(file_args, False, diff=diff):

        if changed:
            message += " and "
        changed = True
        message += "ownership, perms or SE linux context changed"

    assert message == 'ownership, perms or SE linux context changed'
    assert changed == True


# Generated at 2022-06-13 05:35:06.105672
# Unit test for function present
def test_present():
    assert 'xms1024m' == present(
        {'params': {'xms': '1024'}, 'line': '\1Xms${xms}m\3'},
        dest='/opt/jboss-as/bin/standalone.conf', regexp='^(.*)Xms(\d+)m(.*)$',
        search_string=None, line='\1Xms${xms}m\3', insertafter='^(.*)Xms(\d+)m(.*)$',
        insertbefore=None, create='', backup=None, backrefs=True, firstmatch=True)


# Generated at 2022-06-13 05:35:15.551737
# Unit test for function absent
def test_absent():
    # Test module

    arguments = dict(
        backup=False,
        create=True,
        dest="./testfile",
        insertafter=None,
        insertbefore="BOF",
        line="line to insert",
        regexp="^line",
        state="absent",
    )

# Generated at 2022-06-13 05:35:27.286969
# Unit test for function write_changes
def test_write_changes():
  # First test
  test_src = '''blahblahblah
  moreblablah
  blah blah blah'''
  test_dest = '/tmp/test_write_changes'
  with open(test_dest, 'w') as f:
    f.write(test_src)
  test_module = AnsibleModule(
    argument_spec = dict(
      path = dict(required=True, type='str'),
      content = dict(required=True, type='str')
    )
  )
  b_lines = to_bytes(test_module.params['content'])
  dest = test_module.params['path']
  write_changes(test_module, b_lines, dest)

# Generated at 2022-06-13 05:35:37.681638
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec = dict(
            dest=dict(type='path'),
            regexp=dict(type='str', required=False),
            search_string=dict(type='str', required=False),
            line=dict(type='str', required=False),
            backup=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
    )
    # Mock
    dest = '/path/to/dest'
    regexp = None
    search_string = 'search_string'
    line = 'search_string'
    backup = True
    matcher = "^(search_string)$"
    found = []

    class AnsibleExitJson(Exception):
        """Exception class to be raised by module.exit_json and caught by the test case"""
       

# Generated at 2022-06-13 05:35:49.424751
# Unit test for function main

# Generated at 2022-06-13 05:35:50.051924
# Unit test for function write_changes
def test_write_changes():
  return



# Generated at 2022-06-13 05:35:53.286264
# Unit test for function write_changes
def test_write_changes():
    dummy_module = DummyModule()
    write_changes(dummy_module, b_lines=b'foo', dest='/tmp/baz')
    assert dummy_module.atomic_move_called



# Generated at 2022-06-13 05:36:30.188708
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs() == "", False

# end unit test



# Generated at 2022-06-13 05:36:39.563068
# Unit test for function present
def test_present():
    global orig_generic_run_command
    orig_generic_run_command = AnsibleModule._generic_run_command
    AnsibleModule._generic_run_command = generic_run_command

    test_path = '/test'
    test_regexp = ''
    test_search_string = ''
    test_line = 'test line'
    test_insertafter = ''
    test_insertbefore = ''
    test_create = False
    test_backup = False
    test_backrefs = False
    test_firstmatch = False

    module = get_module(test_path, test_regexp, test_search_string, test_line, test_insertafter, \
                        test_insertbefore, test_create, test_backup, test_backrefs, test_firstmatch)

# Generated at 2022-06-13 05:36:49.368258
# Unit test for function check_file_attrs

# Generated at 2022-06-13 05:37:01.349474
# Unit test for function present
def test_present():
    module = AnsibleModule(
        argument_spec = dict(
            dest = dict(type='path'),
            regexp = dict(aliases=['pattern']),
            search_string = dict(required=False),
            line = dict(required=True),
            insertafter = dict(required=False),
            insertbefore = dict(required=False),
            create = dict(aliases=['touch'], required=False, type='bool'),
            backup = dict(required=False, type='bool'),
            state = dict(choices=['present', 'absent'], default='present'),
            backrefs = dict(required=False, type='bool'),
            validate = dict(required=False, type='path'),
            firstmatch = dict(type='bool', default=False)
        )
    )


# Generated at 2022-06-13 05:37:04.845787
# Unit test for function write_changes
def test_write_changes():
    import pytest
    module = AnsibleModule(argument_spec={})
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
    b_lines = [b'bar']
    write_changes(module, b_lines, tmpfile)
    with open(tmpfile, 'rb') as f:
        assert f.readlines() == [b'bar']
    os.remove(tmpfile)



# Generated at 2022-06-13 05:37:14.053651
# Unit test for function absent
def test_absent():
    test_args = {
        'dest': '/etc/motd',
        'regexp': 'Ansible',
        'line': None,
        'backup': False,
        'search_string': None,
    }

    with pytest.raises(AnsibleExitJson) as excinfo:
        absent(module, **test_args)

    assert excinfo.value.args[0]['changed'] == False
    assert excinfo.value.args[0]['found'] == 0
    assert excinfo.value.args[0]['msg'] == 'file not present'


# Unit tests for function present

# Generated at 2022-06-13 05:37:20.372197
# Unit test for function write_changes

# Generated at 2022-06-13 05:37:22.763351
# Unit test for function check_file_attrs
def test_check_file_attrs():
    pass



# Generated at 2022-06-13 05:37:32.970074
# Unit test for function write_changes
def test_write_changes():
    import sys
    import tempfile
    import shutil
    import os
    import errno

    module = AnsibleModule(argument_spec=dict(path='/tmp/test', backup=dict(default=False,type='bool')),
                           supports_check_mode=True)

    try:
        os.makedirs(module.params['path'])
    except OSError as e:
        if e.errno == errno.EEXIST:
            # directory already exists, use it
            pass
        else:
            raise

    if module.params['backup']:
        backup_name = module.params['path'] + '~'
        if os.path.exists(backup_name):
            os.remove(backup_name)

# Generated at 2022-06-13 05:37:47.192960
# Unit test for function present

# Generated at 2022-06-13 05:38:33.998027
# Unit test for function main
def test_main():
    path = '/etc/sudoers'

    # path: /etc/sudoers
    # state:
    #   present:
    #     regexp:
    #     search_string:
    #     line:
    #     insertafter:
    #     insertbefore:
    #     create:
    #     backup:
    #     backrefs:
    #     firstmatch:
    #   absent:
    #     regexp:
    #     search_string:
    #     line:
    #     create:
    #     backup:

    # path: /etc/sudoers
    # state:
    #   present:
    #     regexp: '^root'
    #     search_string:
    #     line: 'root ALL=(ALL) ALL'
    #     insertafter: 'EOF'
    #

# Generated at 2022-06-13 05:38:43.956240
# Unit test for function main

# Generated at 2022-06-13 05:38:51.425435
# Unit test for function present

# Generated at 2022-06-13 05:38:55.685736
# Unit test for function write_changes
def test_write_changes():
    assert os.system(to_bytes("echo 'UNIT TEST' > test_write_changes.txt")) == 0
    module = AnsibleModule({'src': 'test_write_changes.txt', 'validate': 'cat %s'})
    write_changes(module, [b'UNIT TEST\n'], 'test_write_changes.txt')
    try:
        assert os.system(to_bytes("cat test_write_changes.txt")) == 0
    finally:
        os.unlink('test_write_changes.txt')



# Generated at 2022-06-13 05:39:00.650538
# Unit test for function write_changes
def test_write_changes():
    with tempfile.TemporaryDirectory() as tmpdir:
        module_args = dict(
            path=os.path.join(tmpdir, 'test'),
            line='foo',
            validate='true %s'
        )
        module = _get_module(module_args)
        b_lines = [to_bytes('foo', encoding='utf-8')]
        write_changes(module, b_lines,  os.path.join(tmpdir, 'test'))
        with open(os.path.join(tmpdir, 'test'), 'r') as f:
            assert f.read() == 'foo'



# Generated at 2022-06-13 05:39:09.455216
# Unit test for function check_file_attrs

# Generated at 2022-06-13 05:39:15.851219
# Unit test for function main
def test_main():
    from ansible_collections.ansible.community.tests.unit.modules.utils import set_module_args
    import ansible_collections.ansible.community.tests.unit.modules.utils as testutils
    file_args = dict(
        path='/tmp/testfile',
        state='present',
        line='this is a test',
    )
    set_module_args(file_args)
    testutils.get_exception(main)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:39:24.809924
# Unit test for function present
def test_present():
    o = AnsibleModule({'path': '/tmp/file', 'line': 'something'}, check_invalid_arguments=False)
    o.atomic_move = mock.MagicMock()
    m = MagicMock(side_effect=[IOError(), IOError(), True])
    o.run_command = m

    present(o, '/tmp/file', None, None, 'something', None, None, None, None, None, None)
    present(o, '/tmp/file', None, None, 'something', 'EOF', None, None, None, None, None)
    present(o, '/tmp/file', None, None, 'something', 'BOF', None, None, None, None, None)



# Generated at 2022-06-13 05:39:33.148791
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True, type='path'),
            owner=dict(required=False, type='str'),
            group=dict(required=False, type='str'),
            seuser=dict(required=False, type='str'),
            serole=dict(required=False, type='str'),
            setype=dict(required=False, type='str'),
            selevel=dict(required=False, type='str'),
            mode=dict(required=False, type='raw')
        ),
        supports_check_mode=True
    )

    set_attrs = module.set_fs_attributes_if_different

    # Test owner changed
    set_attrs_mock = MagicMock(return_value=True)
    module.set_fs_

# Generated at 2022-06-13 05:39:36.459265
# Unit test for function present
def test_present():
    assert present(None, None, None, None, None, None, None, None, None, None, None, None) == ('', False)


# Generated at 2022-06-13 05:40:34.572047
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs(AnsibleModule, False, "", "") == ("ownership, perms or SE linux context changed", True)


# Generated at 2022-06-13 05:40:40.227391
# Unit test for function main
def test_main():
    ansible_module_main(ArgvParams(
                        'path',path,
                        'state',state,
                        'regexp',regexp,
                        'search_string',search_string,
                        'line',line,
                        'insertbefore',insertbefore,
                        'insertafter',insertafter,
                        'backrefs',backrefs,
                        'create',create,
                        'backup',backup,
                        'firstmatch',firstmatch
                        ))


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:40:46.727115
# Unit test for function present
def test_present():
    module = AnsibleModule(argument_spec=dict(
        dest=dict(required=True),
        regexp=dict(required=False),
        search_string=dict(required=False),
        line=dict(required=True),
        insertafter=dict(required=False),
        insertbefore=dict(required=False),
        create=dict(required=False),
        backup=dict(required=False),
        backrefs=dict(required=False),
        firstmatch=dict(required=False),
        validate=dict(required=False),
        unsafe_writes=dict(required=False),
    ))

    dest = '/tmp/testfile'
    regexp = r'^regexp$'
    search_string = '^search_string$'
    line = 'line'

# Generated at 2022-06-13 05:40:50.208632
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs(module=None, changed=True, message='test', diff='test') == ('test and ownership, perms or SE linux context changed', True)



# Generated at 2022-06-13 05:40:58.016728
# Unit test for function absent
def test_absent():

    class FakeModule(object):
        def __init__(self):
            self.arg_spec = {}
            self.params = {}

        def fail_json(self, *args, **kwargs):
            print(args, kwargs)
            raise RuntimeError('fail_json')

        def exit_json(self, *args, **kwargs):
            print(args, kwargs)


    module = FakeModule()
    b_dest = "/tmp/test.txt"
    # create test.txt
    with open(b_dest, 'wb') as f:
        f.write(b"Hello world")


# Generated at 2022-06-13 05:41:04.403016
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True),
            regexp = dict(),
            search = dict(),
            line = dict(),
            backup = dict(default=False, type='bool'),
        ),
    )
    m_path = module.params['path']
    m_regexp = module.params['regexp']
    m_search = module.params['search']
    m_line = module.params['line']
    m_backup = module.params['backup']

    dest = replace_path_sep(m_path)
    regexp = m_regexp
    search_string = m_search
    line = m_line
    backup = m_backup

    # execute function absent

# Generated at 2022-06-13 05:41:13.378778
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True, type='path'),
            regexp = dict(required=False, type='str'),
            search_string = dict(required=False, type='str'),
            line = dict(required=False, type='str'),
            backup = dict(default=False, type='bool')
        )
    )

    dest = 'test/file'
    regexp = 'test'
    search_string = 'test'
    line = 'test'
    backup = False

    if os.path.exists(dest):
        os.remove(dest)

    f = open(dest, 'wb')
    f.write(to_bytes(line))
    f.close()

# Generated at 2022-06-13 05:41:17.502803
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class Obj:
        def __init__(self):
            self.changed = False
            self.params = {
                'owner': 'user',
                'group': 'group',
                'mode': '777',
                'selevel': 's0',
                'serole': 'role',
                'setype': 'type',
                'seuser': 'user',
            }

        def set_fs_attributes_if_different(self, path, changed, diff=True):
            self.changed = True
            return changed

    module = Obj()
    msg, changed = check_file_attrs(module, True, "msg", False)
    assert msg == "msg and ownership, perms or SE linux context changed"
    assert changed == True

    msg, changed = check_file_attrs(module, False, "", True)

# Generated at 2022-06-13 05:41:19.726207
# Unit test for function write_changes
def test_write_changes():
    assert write_changes() == ''



# Generated at 2022-06-13 05:41:25.568321
# Unit test for function present
def test_present():
    _, dest = tempfile.mkstemp(prefix='ansible-test-fileinfile-')
    os.close(_)
    os.unlink(dest)


# Generated at 2022-06-13 05:42:42.683421
# Unit test for function main
def test_main():
    line = "10.10.10.0"
    regexp = "^10\.10\.10\.0"
    search_string = "^10\.10\.10\.0"
    ins_bef = "192.168.0.10"
    ins_aft = "192.168.0.12"
    path = "/etc/fstab"
    regexp = "^10\.10\.10\.0"
    search_string = "^10\.10\.10\.0"
    create = False
    backup = False
    backrefs = False
    firstmatch = False
    present(module, path, regexp, search_string, line, ins_aft, ins_bef, create, backup, backrefs, firstmatch)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:42:45.784565
# Unit test for function absent
def test_absent():
    assert absent(module=None, dest='file', regexp=None, search_string=None, line='line', backup=None) is None



# Generated at 2022-06-13 05:42:51.014850
# Unit test for function main
def test_main():
    args = dict(path ='/tmp/ansible-test-file',name ='/tmp/ansible-test-file', dest ='/tmp/ansible-test-file', destfile ='/tmp/ansible-test-file',)
    if 'insertbefore' in args:
        args['insertbefore'] = args['insertbefore'].strip()
    if 'insertafter' in args:
        args['insertafter'] = args['insertafter'].strip()
    if 'regexp' in args and args.get('regexp') is not None:
        args['regexp'] = args['regexp'].strip()
    if 'search_string' in args and args.get('search_string') is not None:
        args['search_string'] = args['search_string'].strip()

# Generated at 2022-06-13 05:42:58.581440
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec=dict(), check_invalid_arguments=False, bypass_checks=True, supports_check_mode=True)
    module.params = {'path': None, 'unsafe_writes': True}
    assert check_file_attrs(module, False, "", "") == (None, False)
    module.params['path'] = '/tmp/file'
    module.params['owner'] = 'root'
    module.params['group'] = 'root'
    module.params['seuser'] = 'foo'
    assert check_file_attrs(module, False, "", "") == ("ownership, perms or SE linux context changed", True)
    module.params['owner'] = 'foo'

# Generated at 2022-06-13 05:43:03.416340
# Unit test for function present
def test_present():
    values = {
        'dest': '/etc/test.conf',
        'regexp': '^(.*)Xms(\d+)m(.*)$',
        'line': '\1Xms64m\3',
        'backrefs': True,
        'firstmatch': True,
    }
    b_lines = [b"fooXms1mbar\n", b"bazXms2mquux\n"]
    with tempfile.NamedTemporaryFile() as tmpfile:
        with open(tmpfile.name, 'wb') as f:
            f.writelines(b_lines)

        values['dest'] = tmpfile.name
        present(None, values['dest'], values['regexp'], None, values['line'], None, None, None, None, values['backrefs'])

# Generated at 2022-06-13 05:43:08.765759
# Unit test for function write_changes
def test_write_changes():
    test_module = AnsibleModule(
        argument_spec=dict(
            content=dict(type='list', elements='raw'),
            dest=dict(type='path'),
            validate=dict(type='str', default=''),
            tmpdir=dict(type='path', default='/tmp'),
            unsafe_writes=dict(type='bool', default='no')
        ),
        add_file_common_args=True,
        supports_check_mode=True
    )
    test_module.params.update({'content': ['foo', 'bar']})
    test_module.params.update({'dest': '/tmp/dest'})
    bf = '/tmp/foo'
    f = open(bf, 'w')
    f.close()

# Generated at 2022-06-13 05:43:19.596469
# Unit test for function absent
def test_absent():
    from ansible.module_utils.basic import AnsibleModule
    import sys
    import os

    # Create an AnsibleModule for test
    fields = {
        "state": {"default": "absent", "choices": ["absent", "present"], "type": "str"},
        "backup": {"default": False, "type": "bool"},
        "dest": {
            "required": True,
            "type": "str"
        },
        "line": {"required": True, "type": "str"},
        "search": {"required": False, "type": "str"},
        "regexp": {"required": False, "type": "str"},
        "backrefs": {"required": False, "type": "bool", "default": True},
    }
    module = AnsibleModule(argument_spec=fields)
   

# Generated at 2022-06-13 05:43:30.777864
# Unit test for function absent
def test_absent():

    module = AnsibleModule(argument_spec={
        'dest': {'type': 'path', 'required': True},
        'regexp': {'type': 'str', 'required': False},
        'state': {'type': 'str', 'required': False},
        'line': {'type': 'str', 'required': False},
        'search_string': {'type': 'str', 'required': False},
        'backup': {'default': False, 'type': 'bool'},
    })

    regexp = "^include"

    dest= "/etc/test.cfg"

    b_dest = to_bytes(dest, errors='surrogate_or_strict')
    b_regexp = to_bytes(regexp, errors='surrogate_or_strict')

# Generated at 2022-06-13 05:43:40.752233
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={
            'path': {'type': 'path', 'required': True},
            'owner': {'type': 'str'},
            'group': {'type': 'str'},
            'mode': {'type': 'str'},
            'seuser': {'type': 'str'},
            'serole': {'type': 'str'},
            'setype': {'type': 'str'},
            'selevel': {'type': 'str'},
            'unsafe_writes': {'type': 'bool', 'default': False},
        })

    x = {}
    x['changed'] = False
    x['msg'] = 'message'
    x['diff'] = [{}]

# Generated at 2022-06-13 05:43:49.688656
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({})
    module.params = {"path": "tempfile", "owner": "user", "group": "group", "mode": "0644"}
    message = ""
    diff = False
    module.set_fs_attributes_if_original = lambda x, y, z: False
    assert (check_file_attrs(module, False, message, diff) == ("ownership, perms or SE linux context changed", True))
    module.set_fs_attributes_if_original = lambda x, y, z: True
    assert (check_file_attrs(module, False, message, diff) == ("ownership, perms or SE linux context changed", True))
# end of unit test for function check_file_attrs

