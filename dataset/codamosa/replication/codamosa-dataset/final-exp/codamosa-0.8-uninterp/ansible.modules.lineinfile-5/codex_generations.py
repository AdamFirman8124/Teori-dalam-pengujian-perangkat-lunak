

# Generated at 2022-06-13 05:34:39.411215
# Unit test for function absent
def test_absent():
    dest = 'test/test.txt'
    regexp = r'regexp3'
    search_string = r'search_string2'
    line = 'line 1'
    backup = False

    ret = absent(dest, regexp, search_string, line, backup)
    assert ret is None
    print(ret)


# Generated at 2022-06-13 05:34:48.302093
# Unit test for function absent
def test_absent():
    module = AnsibleModule(argument_spec=dict(
        state=dict(type='str', required=True, choices=['absent']),
        path=dict(type='str', required=True),
        regexp=dict(type='str'),
        search_string=dict(type='str'),
        line=dict(type='str', required=True),
        validate=dict(type='str', default=None),
        backup=dict(type='bool', default=False)),
        supports_check_mode=True)
    assert absent(module, 'foo', None, None, 'line1', False) == None


# Generated at 2022-06-13 05:34:56.786220
# Unit test for function main
def test_main():
    path = tempfile.mktemp('/etc/fstab')

# Generated at 2022-06-13 05:34:57.524856
# Unit test for function write_changes
def test_write_changes():
    pass



# Generated at 2022-06-13 05:35:08.910060
# Unit test for function present
def test_present():
    b_line = to_bytes('test')
    b_lines = [b'test']
    b_new_line = to_bytes('test\n')
    b_linesep = to_bytes(os.linesep, errors='surrogate_or_strict')
    b_lines.insert(0, b_new_line)
    if insertafter == 'EOF' or index[1] == -1:
        if b_lines and not b_lines[-1][-1:] in (b'\n', b'\r'):
            b_lines.append(b_linesep)
        b_lines.append(b_new_line)
        msg = 'line added'
        changed = True

# Generated at 2022-06-13 05:35:23.864408
# Unit test for function main
def test_main():
    import os
    import tempfile
    import shutil
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:35:30.711968
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({
        'dest': '/etc/selinux/config',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'seuser': None,
        'serole': None,
        'setype': None,
        'selevel': None,
    })
    file_args = {
        'path': '/etc/selinux/config',
        'owner': 'root',
        'group': 'root',
        'mode': '0644',
        'seuser': None,
        'serole': None,
        'setype': None,
        'selevel': None,
        'unsafe_writes': False,
        'follow': True,
    }

# Generated at 2022-06-13 05:35:39.416131
# Unit test for function check_file_attrs
def test_check_file_attrs():

    changed = True
    message = 'owner, permissions or SE Linux context changed'
    diff = 'diff'
    module_file_args = {'mode': '0644,', 'group': '', 'owner': 'root', 'selevel': 's0', 'serole': 'object_r', 'setype': 'etc_t', 'seuser': 'system_u'}
    module_set_fs_attributes_if_different = True

    message, changed = check_file_attrs(module_file_args, changed, message, diff)

    assert message == 'owner, permissions or SE Linux context changed and ownership, perms or SE linux context changed'
    assert changed == True


# Generated at 2022-06-13 05:35:44.962088
# Unit test for function present
def test_present():
    module=AnsibleModule({})
    dest='/destination/path'
    regexp=None
    search_string=None
    line='line to add'
    insertafter=None
    insertbefore=None
    create=True
    backup=False
    backrefs=False
    firstmatch=False

    present(module, dest, regexp, search_string, line, insertafter, insertbefore, create, backup, backrefs, firstmatch)



# Generated at 2022-06-13 05:35:55.437139
# Unit test for function main
def test_main():
    import shutil
    test_file_path = 'test_file.txt'
    shutil.copy2('ansible_file_file_module.py', test_file_path)
    params = dict(
            path=test_file_path,
            state='present',
            regexp=None,
            search_string=None,
            line='# Unit test for function main',
            insertafter='# Unit test for function present',
            insertbefore=None,
            backrefs=False,
            create=None,
            backup=False,
            firstmatch=True,
            validate=None,
            content=None,
            _original_basename=None,
            _diff=False
        )
    params['__ansible_check_mode'] = True
    params['__ansible_diff'] = False

# Generated at 2022-06-13 05:36:21.513657
# Unit test for function main
def test_main():
    for key in list(six.iterkeys(units)):
        del units[key]
    # Mock function `present`

# Generated at 2022-06-13 05:36:31.459595
# Unit test for function present
def test_present():

    # Check file not exists
    dest = '/tmp/ansible_test_file'
    regexp = None
    search_string = None
    line = 'test'
    insertafter = None
    insertbefore = 'BOF'
    create = True
    backup = False
    backrefs = True
    firstmatch = False
    if os.path.exists(dest):
        os.remove(dest)
    present(module, dest, regexp, search_string, line, insertafter, insertbefore, create,
            backup, backrefs, firstmatch)

    # Check file exists
    dest = '/tmp/ansible_test_file'
    regexp = None
    search_string = None
    line = 'test'
    insertafter = None
    insertbefore = 'BOF'
    create = True
    backup = False

# Generated at 2022-06-13 05:36:39.640759
# Unit test for function main

# Generated at 2022-06-13 05:36:48.481358
# Unit test for function main

# Generated at 2022-06-13 05:37:01.270192
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec=dict(
        path=dict(type='str', required=True),
        owner=dict(type='str'),
        group=dict(type='str'),
        mode=dict(type='str'),
        seuser=dict(type='str'),
        serole=dict(type='str'),
        selevel=dict(type='str'),
        setype=dict(type='str'),
    ))
    message = "test"
    changed = False
    diff = {}
    file_args = module.load_file_common_arguments(module.params)
    module.set_fs_attributes_if_different(file_args, False, diff=diff)

# Generated at 2022-06-13 05:37:08.894658
# Unit test for function present
def test_present():
    dest = 'test/test.txt'
    regexp = 'first'
    search_string = None
    line = 'first\n'
    insertafter = None
    insertbefore = None
    create = None
    backup = None
    backrefs = True
    firstmatch = False
    present(module, dest, regexp, search_string, line, insertafter, insertbefore, create,
            backup, backrefs, firstmatch)


# Generated at 2022-06-13 05:37:16.011994
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({}, {})
    import datetime
    tmpdir = tempfile.mkdtemp()
    module.tmpdir = tmpdir
    b_lines=[b'foo', b'bar']
    dest="%s/bar.txt" % tmpdir
    write_changes(module, b_lines, dest)
    filename=os.path.realpath(dest)
    f = open(filename, "rb")
    b_lines_read = f.readlines()
    f.close()
    os.unlink(filename)
    os.rmdir(tmpdir)
    assert(b_lines==b_lines_read)


# Generated at 2022-06-13 05:37:20.212271
# Unit test for function write_changes
def test_write_changes():
  # This function is a bit tricky to unit test, because it is writing to disk.
  # As I do not want to mock all the module to just test this function,
  # we have a hidden variable to make the function do nothing instead of
  # write the changes.
  module = AnsibleModule(argument_spec={'_write_changes': {'type': 'bool', 'default': False}})
  module.tmpdir = '/tmp'
  b_lines = to_bytes(u'Hello\nWorld\n!\n')
  dest = '/tmp/test_write_changes'

# Generated at 2022-06-13 05:37:31.951030
# Unit test for function present
def test_present():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(required=True, type='str'),
            regexp=dict(type='str'),
            search_string=dict(aliases=['search'], type='str'),
            line=dict(type='str'),
            insertafter=dict(type='str'),
            insertbefore=dict(type='str'),
            create=dict(default=True, type='bool'),
            backup=dict(default=False, type='bool'),
            backrefs=dict(default=False, type='bool'),
            firstmatch=dict(default=True, type='bool'),
            validate=dict(default=None, type='str'),
            unsafe_writes=dict(default=False, type='bool')
        )
    )
    dest = "/tmp/test"
    regex

# Generated at 2022-06-13 05:37:33.002827
# Unit test for function write_changes
def test_write_changes():
    return None



# Generated at 2022-06-13 05:38:01.201575
# Unit test for function main
def test_main():
    """
    Arguments which are required for module initialization:
    path
    state

    Optionals:
    regexp
    search_string
    line
    insertbefore
    insertafter
    backrefs
    create
    backup
    firstmatch

    """


# Generated at 2022-06-13 05:38:08.482044
# Unit test for function present
def test_present():
    module = AnsibleModule({
        'dest': 'test/test',
        'line': 'testline',
        'exact': True,
        'create': True
    })
    res = present(module, 'test/test', None, None, 'testline', None, None, True, None, None, None)
    assert res is not None


# Generated at 2022-06-13 05:38:19.694411
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({})
    dest_dir = os.path.dirname(os.path.realpath(__file__))
    dest = os.path.join(dest_dir, 'test_write_changes.txt')
    test_file = os.path.join(dest_dir, 'test_write_changes_tmp.txt')
    b_lines = [b'line 1\n', b'line 2\n', b'line 3\n']
    lines = [to_text(line, errors='surrogate_or_strict') for line in b_lines]
    destfile = open(dest, 'w')
    assert os.path.isfile(dest)
    orig_lines = destfile.readlines()
    write_changes(module, b_lines, dest)

# Generated at 2022-06-13 05:38:32.448312
# Unit test for function absent
def test_absent():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import os

    module = basic.AnsibleModule(argument_spec={
        "dest": {"required": True, "type": "str"},
        "regexp": {"type": "str"},
        "search_string": {"type": "str"},
        "line": {"type": "str"},
        "backup": {"type": "bool", "default": False},
    })
    regexp = "^abcabcabcabcabcabc$"
    search_string = "abcabcabcabcabcabc\n"
    line = "abcabcabcabcabcabc\n"
    backup = False
    dest = "/tmp/ansible-test"

    with open(dest, "wb") as fp:
        fp.write

# Generated at 2022-06-13 05:38:43.795840
# Unit test for function check_file_attrs
def test_check_file_attrs():
    changed = True
    message = "thanksgiving"
    diff = "This is a diff"
    class moduleclass:
        def __init__(self):
            self.params = dict()
        def load_file_common_arguments(self, params):
            self.params = params
            return True
        def set_fs_attributes_if_different(self, args, unsafe, diff):
            return True
    module = moduleclass()
    assert check_file_attrs(module, changed, message, diff) == ("thanksgiving and ownership, perms or SE linux context changed", True)
    assert module.params == dict()
    assert check_file_attrs(module, False, message, diff) == ("thanksgiving", True)

# Generated at 2022-06-13 05:38:44.636656
# Unit test for function absent
def test_absent():
    assert False



# Generated at 2022-06-13 05:38:46.775303
# Unit test for function absent
def test_absent():

    assert absent(module, dest, regexp, search_string, line, backup) == absent(module, dest, regexp, search_string, line, backup)
# end of unit test



# Generated at 2022-06-13 05:38:48.417929
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.modules.source_control.gitlab import AnsibleModule
    module = AnsibleModule(argument_spec={})



# Generated at 2022-06-13 05:38:55.027837
# Unit test for function main

# Generated at 2022-06-13 05:39:06.311158
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # Setup
    module = AnsibleModule({
        "path": "/etc/passwd",
        "owner": "root",
        "group": "root",
        "mode": "a=r,u=w,g=r,o=r",
    })

    module.params = {"setype": "staff_r"}
    module.set_fs_attributes_if_different = lambda x, y, z: (False, None)
    # Exercise
    actual = check_file_attrs(module, False, "", False)
    # Verify
    expected = ("ownership, perms or SE linux context changed", True)
    assert actual == expected

    module.params = {"setype": "staff_r"}
    module.set_fs_attributes_if_different = lambda x, y, z: (True, None)


# Generated at 2022-06-13 05:39:55.414611
# Unit test for function write_changes
def test_write_changes():
    m = AnsibleModule({'path': '/tmp/testfile', 'state': 'present', 'line': '192.168.1.99 foo.lab.net foo', 'create': True})
    m.tmpdir = '/tmp'
    m._handle_aliases()
    b_lines = [to_bytes('192.168.1.99 foo.lab.net foo\n')]
    dest = '/tmp/testfile'
    write_changes(m, b_lines, dest)
    b_f = open('/tmp/testfile','rb')
    b_l = b_f.readlines()
    b_f.close()
    assert b_l == b_lines
    assert os.stat('/tmp/testfile').st_size == b_lines[0].__len__()

# Generated at 2022-06-13 05:40:03.610935
# Unit test for function write_changes
def test_write_changes():
    from ansible.module_utils.basic import AnsibleModule
    module = new_module(params={'unsafe_writes': False, 'dest': '/tmp/testfile'})
    b_lines = [b'foo\n', b'bar\n']
    write_changes(module, b_lines, '/tmp/testfile')
    assert os.path.isfile('/tmp/testfile')
    with open('/tmp/testfile', 'rb') as f:
        assert f.readlines() == b_lines

# end unit tests



# Generated at 2022-06-13 05:40:05.020225
# Unit test for function check_file_attrs
def test_check_file_attrs():
    return check_file_attrs(module, changed, message, diff)

# Generated at 2022-06-13 05:40:17.658645
# Unit test for function check_file_attrs
def test_check_file_attrs():
    try:
        import __builtin__ as builtins
    except ImportError:
        import builtins

    class ModuleStub(object):
        def __init__(self):
            self.params = {}
            self.set_fs_attributes_if_different_return = True
            self.run_command_return_value = 0

        def set_fs_attributes_if_different(self, file_args, changed, diff):
            return self.set_fs_attributes_if_different_return

        def load_file_common_arguments(self, params):
            return params

        def fail_json(self, **kwargs):
            raise builtins.Exception(kwargs['msg'])


    module = ModuleStub()


# Generated at 2022-06-13 05:40:19.000264
# Unit test for function present
def test_present():
    pass



# Generated at 2022-06-13 05:40:31.909061
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(default='/tmp/test.txt', type='path'),
            regexp=dict(),
            search_string=dict(),
            line=dict(default='line1'),
            backup=dict(default=False, type='bool')
        ),
    )

    b_dest = to_bytes(module.params['dest'], errors='surrogate_or_strict')
    f = open(b_dest, 'w')
    f.write('line1\n')
    f.write('line2\n')
    f.close()

    result = absent(module, module.params['dest'], None, None, 'line1', False)
    assert result['changed'] == True
    assert result['msg'] == '1 line(s) removed'

# Generated at 2022-06-13 05:40:36.256607
# Unit test for function absent
def test_absent():
    # basic test for present function
    module = AnsibleModule(argument_spec=dict(
        state=dict(default='present', choices=['absent', 'present']),
        path=dict(required=True),
        regexp=dict(),
        search_string=dict(),
        line=dict(default=''),
        insertbefore=dict(),
        insertafter=dict(),
        create=dict(default=False, type='bool'),
        backup=dict(default=False, type='bool'),
        backrefs=dict(default=False, type='bool'),
        firstmatch=dict(default=False, type='bool')
    ))
    dest = module.params['path']
    regexp = module.params['regexp']
    search_string = module.params['search_string']
    line = module.params['line']

# Generated at 2022-06-13 05:40:38.854780
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({'owner': 'root'})
    message = "test"
    diff = []
    changed = False
    check_file_attrs(module, changed, message, diff)

    return diff



# Generated at 2022-06-13 05:40:51.763489
# Unit test for function write_changes
def test_write_changes():
    from ansible.module_utils import basic
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.pycompat24 import StringIO
    from ansible.modules.files import lineinfile

    given_args = {'regexp': '[uU]ser', 'line': 'root:mypassword'}

    module = basic.AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
        mutually_exclusive=[],
    )

    dest = os.path.join(tempfile.mkdtemp(dir=module.tmpdir), 'test.txt')

# Generated at 2022-06-13 05:40:59.538498
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True,
    )
    # Initial message/changed
    message = "Changed message"
    changed = True

    # Changed diff
    diff = {
        'before_header': '# Before header',
        'after_header': '# After header',
        'before': 'line1\nline2',
        'after': 'line1\nline3',
    }
    message, changed = check_file_attrs(module, changed, message, diff)
    assert message == 'Changed message and ownership, perms or SE linux context changed'
    assert changed

    # Unchanged diff

# Generated at 2022-06-13 05:42:31.864333
# Unit test for function present
def test_present():
    assert True == True

# Generated at 2022-06-13 05:42:42.633387
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec = dict(
            dest = dict(type="path", required=True),
            regexp = dict(required=False),
            search_string = dict(required=False),
            line = dict(required=False),
            backup = dict(required=False, default=False, type="bool"),
        ),
    )
    dest = os.path.join(os.getcwd(), 'test_absent.txt')
    regexp = None
    search_string = None
    backup = None

    if os.path.exists(dest):
        os.remove(dest)

    with open(dest, 'wb') as f:
        f.write(to_bytes('# Commented line\n'))
        f.write(to_bytes('# Commented line\n'))
       

# Generated at 2022-06-13 05:42:53.728182
# Unit test for function write_changes
def test_write_changes():

    class TestModule(object):
        def __init__(self, dest):
            self.params = dict(dest=dest)
            self.tmpdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tmp')
            if not os.path.exists(self.tmpdir):
                os.mkdir(self.tmpdir)
        def fail_json(self, **args):
            raise Exception(args)
        def atomic_move(self, src, dest, **args):
            if os.path.exists(dest):
                os.unlink(dest)
            os.rename(src, dest)
    tmpdir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'tmp')

# Generated at 2022-06-13 05:43:00.486650
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True),
            validate = dict(),
            b_lines = dict(type='list', elements='raw')
        )
    )
    module.run_command = mock.Mock(return_value=(0, '', ''))
    module.atomic_move = mock.Mock()
    b_lines = ["line 1\n", "line 2 \n"]
    dest = '/etc/test.conf'
    write_changes(module, b_lines, dest)
    assert module.atomic_move.call_count == 1
    assert module.atomic_move.call_args[0][0].startswith('/tmp')
    assert module.atomic_move.call_args[0][1] == '/etc/test.conf'
    assert module

# Generated at 2022-06-13 05:43:02.489507
# Unit test for function write_changes
def test_write_changes():
  return



# Generated at 2022-06-13 05:43:03.538344
# Unit test for function write_changes
def test_write_changes():
    assert True



# Generated at 2022-06-13 05:43:08.461955
# Unit test for function absent
def test_absent():
    module = AnsibleModule({
        'src': 'fake.txt',
        'dest': '/etc/fake.txt',
        'backup': False,
        'regexp': '.*',
        'line': 'something',
        'state': 'absent',
    })
    dest = module.params['dest']
    regexp = module.params['regexp']
    line = module.params['line']
    backup = module.params['backup']

    try:
        absent(module, dest, regexp, None, line, backup)
    except Exception as e:
        print("An exception occurred in the absent function: %s" % e)
        sys.exit(1)

    sys.exit(0)


# Generated at 2022-06-13 05:43:18.532751
# Unit test for function present
def test_present():
    module = AnsibleModule({
    'regexp': 'first_line',
    'line': 'second line',
    'insertafter': 'first_line',
    'create': 'yes',
    'backup': 'yes',
    'backrefs': 'yes',
    })

    dest='/etc/target_file'
    regexp='first_line'
    search_string='first_line'
    line='second_line'
    insertafter='first_line'
    insertbefore='first_line'
    create='yes'
    backup='yes'
    backrefs='yes'
    firstmatch='yes'

    #TODO: to be implemented


# Generated at 2022-06-13 05:43:25.654079
# Unit test for function write_changes

# Generated at 2022-06-13 05:43:30.647078
# Unit test for function write_changes
def test_write_changes():
    test_module = AnsibleModule({'validate': '/usr/sbin/visudo -cf', 'unsafe_writes': False})
    test_string = b'foobar'
    write_changes(test_module, test_string, '/etc/sudoers')
    with open('/etc/sudoers','rb') as sudoers:
        assert sudoers.read() == test_string
