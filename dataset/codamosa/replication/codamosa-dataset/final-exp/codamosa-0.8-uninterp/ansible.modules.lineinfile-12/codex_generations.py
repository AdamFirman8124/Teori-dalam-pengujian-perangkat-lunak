

# Generated at 2022-06-13 05:34:50.249671
# Unit test for function present
def test_present():
    assert True


# Generated at 2022-06-13 05:35:04.030218
# Unit test for function write_changes
def test_write_changes():

    test_dict = {
        'tmpdir': 'tmpdir',
        'unsafe_writes': True,
        'params': {
            'validate': None
        },
        'atomic_move': None,
        'run_command': None,
        'fail_json': None
    }

    b_lines = []
    dest = 'dest'

    module = DummyModule(**test_dict)

    # dummy for atomic_move
    def atomic_move(f1, f2, unsafe_writes=True, **kwargs):
        test_dict['atomic_move'] = (f1, f2, unsafe_writes)

    module.atomic_move = atomic_move

    # dummy for run_command
    def run_command(cmd):
        test_dict['run_command'] = cmd
        return 0,

# Generated at 2022-06-13 05:35:14.832269
# Unit test for function absent
def test_absent():
    os.environ['ANSIBLE_HOSTNAME'] = "test_host"
    os.path = mock.Mock()
    os.path.exists = mock.Mock(return_value=True)
    mock_module = mock.Mock()
    mock_module.check_mode = False
    mock_module._diff = True
    mock_open = mock.mock_open()
    mock_open.readlines = mock.Mock(return_value=['line1', 'line2', 'line3', 'line4'])
    mock_file = mock.Mock()
    mock_file.writelines = mock.Mock()
    with mock.patch('os.open') as os_open, mock.patch('os.close') as os_close:
        os_open.return_value = 123
        os_close

# Generated at 2022-06-13 05:35:18.297468
# Unit test for function absent
def test_absent():
    '''Returns tuple of args & kwargs for absent'''
    return ({'dest': '/path/to/file',
             'regexp': None,
             'line': 'superman',
             'backup': False,
             },
           {
               'msg': 'removed',
               'changed': True,
               'backup': '',
           })


# Generated at 2022-06-13 05:35:19.126791
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert False



# Generated at 2022-06-13 05:35:29.230364
# Unit test for function write_changes
def test_write_changes():
    test_module = AnsibleModule({
        'atomic_move': lambda *args, **kwargs: None,
        'run_command': lambda *args, **kwargs: (1, None, None),
        'tmpdir': '',
        'validate': '%s',
        'unsafe_writes': False
    })
    lines = ['foo']
    dest = '/bar/baz'
    write_changes(test_module, lines, dest)
    assert test_module.called == 'atomic_move'


# Generated at 2022-06-13 05:35:40.097318
# Unit test for function write_changes
def test_write_changes():
    with open('/tmp/foo', 'w') as f:
        f.write('foo')
    import ansible.module_utils.basic
    b_lines = [b'bar\n']
    dest = '/tmp/foo'
    module = ansible.module_utils.basic.AnsibleModule(argument_spec = dict(), check_invalid_arguments=False, bypass_checks=True)
    module.atomic_move = None
    module.run_command = lambda cmd: (0, '', '')
    module.tmpdir = '/tmp'
    write_changes(module, b_lines, dest)
    with open('/tmp/foo', 'r') as f:
        assert f.read() == 'bar\n'
    os.remove('/tmp/foo')


# Generated at 2022-06-13 05:35:49.379708
# Unit test for function present

# Generated at 2022-06-13 05:35:59.441874
# Unit test for function present
def test_present():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import Mapping

    module = basic.AnsibleModule(
        argument_spec=dict(
            dest=dict(type='path', default='/tmp/test'),
            regexp=dict(required=False),
            search_string=dict(required=False),
            line=dict(required=True),
            insertafter=dict(required=False),
            insertbefore=dict(required=False),
            create=dict(type='bool', default=False),
            backup=dict(type='bool', default=False),
            backrefs=dict(type='bool', default=False),
            firstmatch=dict(type='bool', default=True),
        )
    )



# Generated at 2022-06-13 05:36:04.178736
# Unit test for function present
def test_present():
    result = present(module, dest, regexp, search_string, line, insertafter, insertbefore, create,
            backup, backrefs, firstmatch)
    assert result


# Generated at 2022-06-13 05:36:36.485019
# Unit test for function absent
def test_absent():
    """ Unit test for function absent. """
    src = '''1. this is line one of file one
2. this is line two of file one
3. this is line three of file one
4. this is line four of file one
5. this is line five of file one
6. this is line six of file one
7. this is line seven of file one
8. this is line eight of file one
9. this is line nine of file one
10. this is line ten of file one
    '''
    dest = '2. this is line 2 of file 2'

    # Test that a file is actually created
    destfile = './destfile'
    args = dict(dest='%s' % destfile, state='absent', line=dest)

# Generated at 2022-06-13 05:36:45.505578
# Unit test for function write_changes
def test_write_changes():
    # Test for Atomic Move exception when used with `atomic_move`
    def fake_atomic_move(src, dest, unsafe_writes=False):
        raise Exception('Test Exception from atomic_move')

    module = AnsibleModule({
        'path': '/etc/test',
        'validate': '/usr/sbin/testvalidate %s',
    })

    lines = [to_bytes('Test Line', errors='surrogate_or_strict')]
    module.atomic_move = fake_atomic_move
    try:
        write_changes(module, lines, '/etc/test')
    except:
        exc = get_exception()
        assert False, exc
    else:
        assert False, 'test should have failed'



# Generated at 2022-06-13 05:36:53.052650
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={})
    module.params['owner'] = 'root'
    module.params['group'] = 'root'
    module.params['mode'] = '0755'
    changed = False
    message = "file changed"
    message, changed = check_file_attrs(module, changed, message, True)
    assert message == "file changed and ownership, perms or SE linux context changed"


# Generated at 2022-06-13 05:37:03.906548
# Unit test for function absent
def test_absent():
    dest = "/etc/test.conf"
    regexp = None
    search_string = "^test_text"
    line = "test_text"
    backup = True

    # 1. File exist but the searched string does not exist.
    b_lines = [to_bytes(u"test_new_text\n")]
    with open(dest, 'wb') as f:
        f.write(b''.join(b_lines))

    # 2. File exist and the searched string exist only one time.
    with open(dest, 'wb') as f:
        f.write(b''.join(b_lines))
    def matcher(line):
        if line.rstrip(b'\r\n') == to_bytes(line):
            return True
        return False


# Generated at 2022-06-13 05:37:16.036325
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:37:23.720070
# Unit test for function present
def test_present():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import io
    import tempfile
    import os

    tmpdir = tempfile.mkdtemp()
    destination = os.path.join(tmpdir, 'destination')
    insertbefore = 'test_insertbefore'
    insertafter = 'test_insertafter'
    regexp = 'test_regexp'
    search_string = 'test_search_string'
    line = 'test_line'
    create = True
    backup = False
    backrefs = False
    firstmatch = False

    with open(destination, 'w') as f:
        f.write('test_insertbefore\n')
        f.write('test_insertafter\n')
        f.write('test_line\n')



# Generated at 2022-06-13 05:37:33.006424
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str'),
            owner=dict(type='str'),
            group=dict(type='str'),
            mode=dict(type='str'),
            seuser=dict(type='str'),
            serole=dict(type='str'),
            selevel=dict(type='str'),
            setype=dict(type='str'),
            backup=dict(type='bool', default=False),
            unsafe_writes=dict(type='bool', default=False),
        ),
        supports_check_mode=False,
    )
    module.run_command = MagicMock()
    check_file_attrs(module, False, "", {})
    module.params['seuser'] = 'foo'
    module.run_command.assert_called

# Generated at 2022-06-13 05:37:45.927019
# Unit test for function write_changes
def test_write_changes():
    s = os.stat(__file__)
    s.st_size=1

# Generated at 2022-06-13 05:37:56.278686
# Unit test for function write_changes
def test_write_changes():
    tmpfd, tmpfile = tempfile.mkstemp(dir='/tmp')
    f = os.fdopen(tmpfd)
    f.writelines(b'line1\nline2\nline3\nline4\n')
    f.close()

    module_args = dict(
        tmpdir = '/tmp',
        validate= "cat %s",
        unsafe_writes= False,
        backup= False,
        dest="/tmp/file",
        create= False,
        force= False,
    )
    module = AnsibleModule(argument_spec=dict(
        tmpdir=dict(type='path'),
        validate=dict(type='path'),
        unsafe_writes=dict(type='bool'),
    ))
    #if module.check_mode:
    #    return dict(changed=True)



# Generated at 2022-06-13 05:38:08.343067
# Unit test for function write_changes
def test_write_changes():
    results = AnsibleModule(argument_spec={
        'dest': {'type': 'path'},
    }).load_result_file(file_name='lineinfile_result.json')
    # These are the dictionary keys for the result entries
    result_keys = ['_ansible_no_log', 'invocation', 'changed', 'failed']
    # Make sure the result keys are present
    assert all(key in result_keys for key in results['result'])
    # Make sure the value for the failed key is False
    assert results['result']['failed'] == False
    # Make sure the value for the changed key is False
    assert results['result']['changed'] == False


# Generated at 2022-06-13 05:38:50.459778
# Unit test for function absent

# Generated at 2022-06-13 05:38:56.684409
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={
        'dest': {'type': 'path', 'required': True},
        'unsafe_writes': {'type': 'bool', 'required': False, 'default': False},
        'before': {'required': False},
        'after': {'required': False},
        'selevel': {'required': False},
        'serole': {'required': False},
        'seuser': {'required': False},
        'setype': {'required': False},
        'backup': {'required': False},
        'mode': {'type': 'str', 'required': False}
    })
    # Mock file_args

# Generated at 2022-06-13 05:39:02.676011
# Unit test for function absent
def test_absent():
    dest = None
    regexp = None
    search_string = r"^adminuser\s*ALL="
    line = "adminuser ALL="
    backup = False
    class FakeModule(object):
        def __init__(self):
            self.check_mode = False
            self.diff = True
            self.backup = False
            self._diff = True
        def exit_json(self, **kwargs):
            self.fail_json = lambda *x: self.fail(x)
            self.exit_json = lambda *x, **kw: True
        def fail_json(self, **kwargs):
            self.exit_json = lambda *x, **kw: True
            raise Exception(kwargs)
        def backup_local(self, a):
            pass
    f = FakeModule()

# Generated at 2022-06-13 05:39:15.284944
# Unit test for function write_changes
def test_write_changes():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    import os
    import tempfile
    import shutil

    content = 'hello world'
    tmpdir = tempfile.mkdtemp()
    dest = os.path.join(tmpdir, 'destfile')
    with open(dest, 'w') as f:
        f.write(content)
    b_lines = content.encode() + b'\n'

    # Save backup
    backup_file = module.backup_local(dest)

    assert os.path.isfile(dest)

    # 1) Validate success

# Generated at 2022-06-13 05:39:20.961946
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.parsing.convert_bool import boolean

    import json
    import pytest

    from datetime import datetime
    from pytest_mock import mocker
    import shutil
    import tempfile


# Generated at 2022-06-13 05:39:30.991220
# Unit test for function write_changes
def test_write_changes():
    from ansible_collections.ansible.builtin.plugins.modules.test.test_ansible_module import BaseModule
    from ansible.module_utils.basic import AnsibleModule
    import os
    test_data = 'This is a test'
    tmpfd, tmpfile = tempfile.mkstemp()
    with os.fdopen(tmpfd, 'wb') as f:
        f.write(test_data)
    dest_file = tempfile.mkstemp()
    dest = os.fdopen(dest_file[0], 'wb')
    src = os.fdopen(dest_file[0], 'rb')
    test_module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    test_module.atomic_move = BaseModule._atomic_move

# Generated at 2022-06-13 05:39:45.030640
# Unit test for function present
def test_present():
    # Exact line match
    test_lineinfile_params = dict(
        dest="/tmp/test",
        line="192.168.1.1",
        create=False,
        backup=False,
        insertafter="EOF",
        firstmatch=False
    )

# Generated at 2022-06-13 05:39:54.197654
# Unit test for function main

# Generated at 2022-06-13 05:40:02.928625
# Unit test for function main

# Generated at 2022-06-13 05:40:15.811165
# Unit test for function check_file_attrs
def test_check_file_attrs():
    import sys
    import copy
    import ansible.module_utils.basic
    ansible.module_utils.basic.AnsibleModule = AnsibleModule

    src_path = os.path.dirname(__file__)
    sys.path.append(src_path)
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY2

    my_user = os.getuid()
    my_group = os.getgid()
    my_mode = 0o600

# Generated at 2022-06-13 05:42:02.035239
# Unit test for function absent
def test_absent():
    def test_absent_lines(lines, regexp, search_string, line,
                          expected_lines, expected_found):

        module = AnsibleModule(
            argument_spec = dict(
                regexp=dict(default=regexp),
                search_string=dict(default=search_string, type='str'),
                path=dict(default="test_path"),
                line=dict(default=line),
            ),
            supports_check_mode=True
        )

        dest = os.path.join(tempfile.mkdtemp(), "test_path")
        with open(dest, "w") as f:
            for l in lines:
                f.write(to_bytes(l, errors='surrogate_or_strict'))
                f.write(to_bytes(os.linesep))


# Generated at 2022-06-13 05:42:05.009670
# Unit test for function absent
def test_absent():
    '''returns module, dest, regexp, search_string, line, backup'''
    return None, "dest", "regexp", "search_string", "newline", "backup"



# Generated at 2022-06-13 05:42:18.840477
# Unit test for function present
def test_present():
    module = AnsibleModule({
        'path': '/path/to/file',
        'regexp': '^pattern$',
        'state': 'present',
        'line': 'line content',
        'insertbefore': 'BOF',
        'insertafter': None,
        'create': False,
        'backup': False,
        'backrefs': False,
        'unsafe_writes': False,
        '_diff': True,
        '_ansible_check_mode': True,
        '_ansible_no_log': False,
        'dest': '/path/to/file'
    })

# Generated at 2022-06-13 05:42:19.552322
# Unit test for function absent
def test_absent():
    assert absent('b','c','d','e','f','g') == None

# Generated at 2022-06-13 05:42:24.570995
# Unit test for function absent
def test_absent():
  import os
  import copy
  import tempfile

  MOCK_INPUT = {
    "changed": False,
    "msg": "file not present",
    "backup": "",
    "diff": {
      "before": "",
      "after": "",
      "before_header": "/root/test_module.pyc (content)",
      "after_header": "/root/test_module.pyc (content)",
    }
  }

  (fd, fname) = tempfile.mkstemp()
  os.write(fd, b"""
# This test is a line with no EOL
This is a test\r
This is a test\r""")
  os.close(fd)

  (fd, fname2) = tempfile.mkstemp("-2")
  os.close(fd)

# Generated at 2022-06-13 05:42:36.278388
# Unit test for function main

# Generated at 2022-06-13 05:42:45.705244
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec = dict(
            dest = dict(type='path', required=True),
            regexp = dict(type='str', required=False),
            search_string = dict(type='str', required=False),
            line = dict(type='str', required=False, default='#'),
        ),
        supports_check_mode = True
    )
    path = module.params['dest']
    regexp = module.params['regexp']
    search_string = module.params['search_string']
    line = module.params['line']

    if regexp is not None:
        bre_c = re.compile(to_bytes(regexp, errors='surrogate_or_strict'))


# Generated at 2022-06-13 05:42:51.094889
# Unit test for function absent
def test_absent():
    module = AnsibleModule({
        "dest": "/tmp/ansible_test_file",
        "line": 'test line',
        "state": "absent",
    })
    dest = "/tmp/ansible_test_file"
    regexp = None
    search_string = None
    line = 'test line'
    backup = False
    absent(module, dest, regexp, search_string, line, backup)


# Generated at 2022-06-13 05:42:58.611371
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class Module(object):
        params = {
            'path': 'test_path',
            'owner': 'test_owner',
            'group': 'test_group',
            'mode': 'test_mode',
            'selevel': 's0',
            'serole': 'object_r',
            'setype': 'test_setype',
            'seuser': 'test_seuser',
            'unsafe_writes': False,
        }

        def load_file_common_arguments(self, params):
            return self.params

        def set_fs_attributes_if_different(self, file_args, changed, diff = False):
            return changed

    module = Module()

    message = ""
    changed = False
    # Test 1: changed is False
    result_message, result_changed = check_

# Generated at 2022-06-13 05:43:07.957928
# Unit test for function present
def test_present():
    b_dest = to_bytes(dest, errors='surrogate_or_strict')
    if not os.path.exists(b_dest):
        if not create:
            module.fail_json(rc=257, msg='Destination %s does not exist !' % dest)
        b_destpath = os.path.dirname(b_dest)
        if b_destpath and not os.path.exists(b_destpath) and not module.check_mode:
            try:
                os.makedirs(b_destpath)
            except Exception as e:
                module.fail_json(msg='Error creating %s (%s)' % (to_text(b_destpath), to_text(e)))

        b_lines = []