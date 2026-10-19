

# Generated at 2022-06-13 05:34:45.717439
# Unit test for function present

# Generated at 2022-06-13 05:34:58.727478
# Unit test for function absent
def test_absent():
    module = AnsibleModule(argument_spec=dict(
        dest=dict(required=True),
        regexp=dict(default=None),
        backrefs=dict(default='yes', type='bool'),
        state=dict(default='present', choices=['absent', 'present']),
        line=dict(default=None),
        backup=dict(default='no', type='bool')), supports_check_mode=True)

    line = 'ansible-line'
    regexp = line + '.*'
    search_string = None
    dest = 'test_absent.txt'
    changed = False
    backup = False
    msg = ''
    result = absent(module, dest, regexp, search_string, line, backup)
    assert result['changed'] ==  changed
    assert result['msg'] == msg

   

# Generated at 2022-06-13 05:35:07.090192
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )

    test_file_path='/tmp/test_file'
    test_file_lines=[b'line1\n', b'line2\n', b'line3\n']
    write_changes(module, test_file_lines, test_file_path)

    with open(test_file_path, 'rb') as f:
        lines = f.readlines()
        assert lines == test_file_lines



# Generated at 2022-06-13 05:35:22.264867
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import os, sys, tempfile

# Generated at 2022-06-13 05:35:30.402217
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str', required=True),
            line=dict(type='str', required=True),
            backup=dict(type='bool', required=True),
            create=dict(type='bool', required=False),
            validate=dict(type='str', required=False),
            unsafe_writes=dict(type='bool', default=False),
        ),
        supports_check_mode=False
    )
    # Write a test file
    test_content = '''[Unit]\nDescription=Example\n[Service]\nExecStart=/usr/bin/true\n'''
    with open(module.params['path'], 'w') as f:
        f.write(test_content)


# Generated at 2022-06-13 05:35:42.061945
# Unit test for function absent
def test_absent():
    import json
    import pytest
    from ansible.module_utils import basic
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils._text import to_bytes

    FAKE_RC_FAIL = 1
    global module

# Generated at 2022-06-13 05:35:51.711730
# Unit test for function present
def test_present():
    from ansible.module_utils.six import StringIO
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(type='path'),
            regexp=dict(type='str'),
            search_string=dict(type='str'),
            line=dict(type='str'),
            insertafter=dict(type='str'),
            insertbefore=dict(type='str'),
            create=dict(type='bool'),
            backup=dict(type='bool'),
            backrefs=dict(type='bool'),
            firstmatch=dict(type='bool'),
            validate=dict(type='str'),
        ),
        supports_check_mode=True,
    )
    module.tmpdir = tempfile.mkdtemp(prefix='ansible-tmp-')
    dest_file = module.tmpdir + '/dest'

# Generated at 2022-06-13 05:35:58.601085
# Unit test for function absent
def test_absent():
    line = "test line"
    regexp = "test line"
    search_string = None
    dest = "test.file"
    backup = False
    present = True
    m = MyModule()
    m.check_mode = False
    m.params = {}
    m.params['backup'] = backup
    m.params['dest'] = dest
    m.params['regexp'] = regexp
    m.params['search_string'] = search_string
    m.params['line'] = line
    if present:
        present(m, dest, regexp, search_string, line, None, None, False, backup, False, False)
    else:
        absent(m, dest, regexp, search_string, line, backup)

# Generated at 2022-06-13 05:36:11.519976
# Unit test for function main
def test_main():
  # In this case we like to give only argv
  argv = [
    "/root/ansible/lib/ansible/modules/files/lineinfile.py",
    "path=/etc/password",
    "state=present",
    "line=test",
    "create=True",
    "backup=False",
    "backrefs=False",
    "firstmatch=False",
  ]
  argv2 = []
  class MockAnsibleModule:
    def exit_json(self,rc, msg=''):
      print ('exit_json {}'.format(msg))
    def fail_json(self,rc, msg=''):
      print ('fail_json {}'.format(msg))

# Generated at 2022-06-13 05:36:12.234843
# Unit test for function check_file_attrs
def test_check_file_attrs():
    pass



# Generated at 2022-06-13 05:36:56.090325
# Unit test for function main

# Generated at 2022-06-13 05:37:02.210009
# Unit test for function check_file_attrs
def test_check_file_attrs():
    '''Verify check_file_attrs returns expected values'''
    assert check_file_attrs(1, True, 'test', 'test2') == ('test and ownership, perms or SE linux context changed', True)
    assert check_file_attrs(1, False, 'test', None) == ('ownership, perms or SE linux context changed', True)
    assert check_file_attrs(1, True, 'test', None) == ('test and ownership, perms or SE linux context changed', True)
    assert check_file_attrs(1, False, 'test', 'test2') == ('test2', True)
    assert check_file_attrs(1, False, None, None) == (None, False)

# Generated at 2022-06-13 05:37:07.750452
# Unit test for function check_file_attrs

# Generated at 2022-06-13 05:37:17.502338
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec=dict(
        path=dict(type='path',required=True),
        line=dict(type='str'),
        regexp=dict(type='str'),
        insertafter=dict(type='str'),
        insertbefore=dict(type='str'),
        dest=dict(type='str')
    ))
    import inspect
    fun = inspect.currentframe().f_code.co_name
    testobj = Lineinfile(module)
    test_file_args = module.load_file_common_arguments(module.params)
    message = "test_message"
    assert testobj.check_file_attrs(module, False, message, "test_diff") == (message, False), "Function %s failed, Please check"%(fun)
    assert testobj.check_file_

# Generated at 2022-06-13 05:37:23.206074
# Unit test for function check_file_attrs
def test_check_file_attrs():
    test1   = [1, 9, 'test', 'text']
    test2   = [1, 9, 'test', 'text']
    assert check_file_attrs(test1, False, "test", "test") == test2


# Generated at 2022-06-13 05:37:28.888574
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({})
    module.params['path'] = '/tmp/ansible_test_file'
    module.params['owner'] = os.getuid()
    module.params['group'] = os.getgid()
    module.params['mode'] = '0600'
    assert check_file_attrs(module, False, "", "") == ("ownership, perms or SE linux context changed", True)


# Generated at 2022-06-13 05:37:39.722789
# Unit test for function main

# Generated at 2022-06-13 05:37:50.909545
# Unit test for function write_changes
def test_write_changes():
    # create a temp file
    with tempfile.NamedTemporaryFile() as tmpfd:
        tmpfile = tmpfd.name

    # create a module
    data = dict(
        validate = None
    )
    module = AnsibleModule(
        argument_spec = dict(),
        supports_check_mode=True
    )
    m_params = module.params
    m_params.update(data)

    # create some b_line data
    lines = ['linea\n', 'lineb\n', 'linec\n', 'lined\n']
    b_lines = [to_bytes(line, errors='surrogate_or_strict') for line in lines]

    # invoke the function
    write_changes(module, b_lines, tmpfile)

    # verify the file has been created
    assert os.path

# Generated at 2022-06-13 05:37:57.772366
# Unit test for function present
def test_present():

    dest = '/tmp/myfile'
    regexp = 'some regexp'
    search_string = None
    line = 'some line'
    insertafter = 'BOF'
    insertbefore = None
    create = True
    backup = True
    backrefs = False
    firstmatch = True

    present(module, dest, regexp, search_string, line, insertafter, insertbefore, create, backup, backrefs, firstmatch)


# Generated at 2022-06-13 05:38:09.957667
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )
    assert isinstance(module, AnsibleModule)
    assert not module.set_fs_attributes_if_different(dict(path='/foo'), False, diff=True)

    # Create a fake module to set some things
    module.params['path'] = '/foo'
    module.params['owner'] = 'owner'
    module.params['group'] = 'group'
    module.params['mode'] = '0644'
    changed = False
    message = ''
    message, changed = check_file_attrs(module, changed, message, True)
    assert changed
    assert message == 'ownership, perms or SE linux context changed'



# Generated at 2022-06-13 05:38:52.381350
# Unit test for function check_file_attrs
def test_check_file_attrs():

    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={'dest': {'type': 'str'}})
    module.params = {'path': '/tmp/file'}
    module.run_command = run_command
    module.atomic_move = atomic_move
    changed = False
    message = ""
    diff = []
    module.set_fs_attributes_if_different = set_fs_attributes_if_different
    message, changed = check_file_attrs(module, changed, message, diff)
    assert changed == True
    assert message == "ownership, perms or SE linux context changed"
    return changed, message, diff


# Generated at 2022-06-13 05:38:52.839692
# Unit test for function present
def test_present():
    pass


# Generated at 2022-06-13 05:38:54.016425
# Unit test for function absent
def test_absent():
    assert absent('/etc/passwd', None, 'HHH', 'HHH', None, True) == False

# Generated at 2022-06-13 05:38:54.463341
# Unit test for function write_changes
def test_write_changes():
    pass



# Generated at 2022-06-13 05:38:56.658525
# Unit test for function present
def test_present():
    module = AnsibleModule({'dest': '/tmp/foo', 'line': 'line'})
    res = present(module, '/tmp/foo', None, None, 'line', None, None, True, False, False, False)

    assert res == "line added"


# Generated at 2022-06-13 05:39:02.584707
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({})
    diff = {}

    file_args = module.load_file_common_arguments(module.params)
    if module.set_fs_attributes_if_different(file_args, False, diff=diff):
        message += " and "
        changed = True
        message += "ownership, perms or SE linux context changed"

    return message, changed

# unit test for function write_changes

# Generated at 2022-06-13 05:39:13.189598
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec = dict(
            dest=dict(type='path', required=True),
            regexp=dict(type='str'),
            search_string=dict(type='str'),
            line=dict(type='str', required=True),
            backup=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
    )

    (line, dest, regexp, search_string, backup) = module_args(module)
    try:
        absent(module, dest, regexp, search_string, line, backup)
    except Exception as ex:
        module.fail_json(msg=str(ex))



# Generated at 2022-06-13 05:39:13.566678
# Unit test for function present
def test_present():
    pass



# Generated at 2022-06-13 05:39:19.639690
# Unit test for function write_changes
def test_write_changes():
    lines = b"hello world"
    tmpfile = ['/tmp/file.txt','file.txt']
    for dest in tmpfile:
        with open(dest, 'w') as f:
            write_changes(tmpfile,lines,dest)
        assert f.readlines() == lines
        os.remove(dest)



# Generated at 2022-06-13 05:39:27.786921
# Unit test for function present

# Generated at 2022-06-13 05:40:18.131300
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({})
    dest = "test.txt"
    # This actually creates the file
    file_args = module.load_file_common_arguments({})
    module.set_fs_attributes_if_different(file_args, False)

    os.chmod(dest, 0o644)
    file_args['mode'] = '640'
    assert check_file_attrs(module, False, "", "") == ('', True)

    file_args['mode'] = '644'

    os.chown(dest, 0, 0)
    file_args['owner'] = 1
    assert check_file_attrs(module, False, "", "") == ('and ownership, perms or SE linux context changed', True)

    file_args['owner'] = 'root'


# Generated at 2022-06-13 05:40:22.392651
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = None
    changed = False
    message = "test"
    diff = False
    value = check_file_attrs(module,changed,message,diff)
    assert value[1] == False



# Generated at 2022-06-13 05:40:30.457345
# Unit test for function absent
def test_absent():
    lines=["line1\n","line2\n","line3\n"]
    regexp = "^line[0-9]"
    search_string = "line3\n"
    line = "line1\n"
    if regexp is not None:
        bre_c = re.compile(to_bytes(regexp, errors='surrogate_or_strict'))
    found = []
    b_line = to_bytes(line, errors='surrogate_or_strict')
    def matcher(b_cur_line):
        if regexp is not None:
            match_found = bre_c.search(b_cur_line)
        elif search_string is not None:
            match_found = to_bytes(search_string, errors='surrogate_or_strict') in b

# Generated at 2022-06-13 05:40:35.140101
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({'validate': '/bin/true %s'}, check_invalid_arguments=False)
    handle, path = tempfile.mkstemp(dir=module.tmpdir)
    with os.fdopen(handle, 'wb') as f:
        f.write(b'foo\n')
    lines = [b'foo\n', b'bar\n']
    write_changes(module, lines, path)
    assert open(path).read() == 'foo\nbar\n'
    os.unlink(path)



# Generated at 2022-06-13 05:40:42.675056
# Unit test for function present
def test_present():
    module = AnsibleModule(
        argument_spec = dict(
            dest=dict(type='path', required=True),
            regexp=dict(type='str'),
            search_string=dict(type='str'),
            line=dict(type='str', required=True),
            insertafter=dict(type='str'),
            insertbefore=dict(type='str'),
            backrefs=dict(type='bool', default=False),
            state=dict(type='str', default='present', choices=['present']),
            create=dict(type='bool', default=False),
            backup=dict(type='bool', default=False),
            firstmatch=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
    )
    dest = 'test.txt'

# Generated at 2022-06-13 05:40:55.789997
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec = dict(
            dest = dict(type='str', required=True),
            lines = dict(type='list', required=True),
            validate = dict(type='str'),
            unsafe_writes=dict(type='bool', default=False),
        ),
    )
    module.run_command = run_command
    set_module_args(dest="/path/to/file", lines=['line1', 'line2', 'line3'])
    write_changes(module, module.params['lines'], module.params['dest'])
    assert os.path.exists("/path/to/file"), "/path/to/file does not exist"

# Generated at 2022-06-13 05:40:59.803988
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({
        'mode': '0644',
    })
    testmodule = FakeModule(module)
    check_file_attrs(testmodule, False, "", "")
    module = AnsibleModule({})
    testmodule = FakeModule(module)
    check_file_attrs(testmodule, True, "ownership, perms or SE linux context changed", "")
# End unit test



# Generated at 2022-06-13 05:41:05.071670
# Unit test for function write_changes
def test_write_changes():
    import tempfile
    lines = b'Hello World\n'
    tmp_fd, tmp_fname = tempfile.mkstemp()
    with os.fdopen(tmp_fd, 'wb') as f:
        f.write(b'Hello World\n')
    m = AnsibleModule(
        argument_spec={},
    )
    lines = b'FOO'
    res = write_changes(m, lines, tmp_fname)
    assert res is None
    f = open(tmp_fname, 'r')
    data = f.read()
    f.close()
    assert data == 'FOO'
    os.unlink(tmp_fname)


# Generated at 2022-06-13 05:41:13.727103
# Unit test for function present
def test_present():
    dest = '/tmp/present'

    # Check that create doesn't create a new file when no match is found.
    assert not os.path.exists(dest)

    present(module, dest, regexp=None, search_string=None, line='hello world', insertafter=None,
            insertbefore=None, create=False, backup=False, backrefs=False, firstmatch=False)

    assert not os.path.exists(dest)

    # Check that create creates a new file when no match is found.
    assert not os.path.exists(dest)
    present(module, dest, regexp=None, search_string=None, line='hello world',
            insertafter=None, insertbefore=None, create=True, backup=False, backrefs=False,
            firstmatch=False)
    assert os.path

# Generated at 2022-06-13 05:41:23.822568
# Unit test for function write_changes
def test_write_changes():
    test_dest = '/test_write_changes'
    test_module = AnsibleModule(argument_spec={
        'dest': {'type': 'str', 'default': test_dest},
        'line': {'type': 'str', 'default': 'test_write_changes'},
        'unsafe_writes': {'type': 'bool', 'default': False},
        'validate': {'type': 'str', 'default': None}
    })
    test_b_lines = []
    write_changes(test_module, test_b_lines, test_dest)
    assert os.path.isfile(test_dest)
    assert to_text(open(test_dest, 'rb').read(), errors='surrogate_or_strict') == ''

# Generated at 2022-06-13 05:42:48.964849
# Unit test for function main
def test_main():
    testmod_main(module_utils.basic)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:42:57.603494
# Unit test for function main
def test_main():
    class MyModule:
        def __init__(self,params,check_mode=None, backup_local=None, diff=None):
            self.params = params
            self.check_mode = check_mode
            self.backup_local = backup_local
            self.diff = diff

        class AnsibleFileAttrs(object):
            def __init__(self,attrs):
                self.attrs = attrs
            def __getattr__(self, attr):
                return self.attrs[attr]

        def exit_json(self,changed=None,msg=None,backup=None, diff=None):
            print("changed: %s" % changed)
            print("msg: %s" % msg)
            print("backup: %s" % backup)
            print("diff: %s" % diff)

# Generated at 2022-06-13 05:43:07.246984
# Unit test for function present
def test_present():
    lines = to_bytes("""
#
# This is an example configuration file
#
# Lines starting with "#" are treated as comments and ignored

# A key without a value is treated as "true"

# To set a value, use the "key = value" syntax
foo = bar

[section1]
key1 = value1
another_key = another value

[section2]
key1 = value1
another_key = another value
key2 = value2
""")
    b_lines = lines.split(b'\n')


# Generated at 2022-06-13 05:43:12.230675
# Unit test for function main
def test_main():
    args = dict(path = 'path', state = 'present', regexp = 'regexp', search_string = 'search_string', line = 'line', insertafter = 'insertafter', insertbefore = 'insertbefore', backrefs = 'backrefs', create = 'create', backup = 'backup', firstmatch = 'firstmatch', validate = 'validate')

# Generated at 2022-06-13 05:43:21.079610
# Unit test for function present
def test_present():
    import os
    import tempfile
    from ansible_collections.ansible.builtin.plugins.modules import lineinfile as linf
    LINES = (b'foo: cool beans\n', b'bar: not as cool\n')

    tf = tempfile.NamedTemporaryFile(delete=False)
    tf.writelines(LINES)
    tf.flush()

    # Test 1: search a line that isn't there
    module = linf.AnsibleModule({
        'path': tf.name,
        'regexp': r'foo bar',
        'line': 'foo bar: baz',
    })
    linf.present(module, tf.name, r'foo bar', None, 'foo bar: baz', None, None, False, False, False, False)


# Generated at 2022-06-13 05:43:27.850442
# Unit test for function absent
def test_absent():
    assert absent(False,"test_absent.py","absent","test","test_added_line", True) != ["test","test_added_line"]
    assert absent(False,"test_absent.py","absent","test","test_added_line", True) == ["test"]
    assert absent(False,"test_absent.py","absent","test","test_added_line", False) == ["test"]


# Generated at 2022-06-13 05:43:34.043722
# Unit test for function present
def test_present():
    ''' Function to test present function '''
    with patch('ansible.modules.files.lineinfile.present') as mock_present:
        with patch('ansible.modules.files.lineinfile.absent') as mock_absent:
           with patch.object(AnsibleModule, 'run_command') as mock_run_command:
                mock_run_command.return_value = (0, 'success', '')
                mock_absent.return_value = 'success'
                mock_present.return_value = 'success'
                result = main()
                assert result['changed'] == False


# Generated at 2022-06-13 05:43:40.751499
# Unit test for function absent
def test_absent():
    assert absent('/etc/test.txt', '^Example',None, 'Example line that is different', backup=False) == (True, '1 line(s) removed')
    assert absent('/etc/test.txt', '^Example',None, 'Example line', backup=False) == (False, '0 line(s) removed')
    assert absent('/etc/test.txt', None,'Example', 'Example line', backup=False) == (False, '0 line(s) removed')
    assert absent('/etc/test.txt', None,'Example', 'Example line that is different', backup=False) == (True, '1 line(s) removed')

# Generated at 2022-06-13 05:43:47.468926
# Unit test for function write_changes
def test_write_changes():
    # Mock module
    module = AnsibleModule({
        'validate': '%s',
        'executable': '/bin/sh',
        'tmpdir': '/tmp',
        'unsafe_writes': 'yes'
    })
    # Set up the module.run_command side effect
    module.run_command = lambda command: (0, '', '')
    # Create a temporary file
    tmpfd, tmpfile = tempfile.mkstemp()
    with os.fdopen(tmpfd, 'wb') as f:
        # Write some data to it
        f.write(to_bytes('data\n'))
        # close it
        f.close()
    # Mock the atomic_move side effect to return the tmpfile name
    module.atomic_move = lambda src, dest, unsafe: tmpfile
    # Run the

# Generated at 2022-06-13 05:43:53.531375
# Unit test for function absent
def test_absent():
    test_lines = [b'1\n', b'2\n', b'3\n']
    test_line_remove_before = b'1\n'
    test_line_add_before = b'0\n'
    test_line_remove_middle = b'2\n'
    test_line_add_middle = b'4\n'
    test_line_remove_after = b'3\n'
    test_line_add_after = b'5\n'
    test_regex_remove_before = b"^1"
    test_regex_add_before = b"^0"
    test_regex_remove_middle = b"^2"
    test_regex_add_middle = b"^4"