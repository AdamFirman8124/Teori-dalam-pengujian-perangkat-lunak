

# Generated at 2022-06-13 05:34:47.387963
# Unit test for function present
def test_present():
    module = AnsibleModule({'path': 'test.txt',
                            'firstmatch': False,
                            'state': 'present',
                            'line': 'test'})
    
    # without backup
    with open(module.params['path'], 'w') as f:
        f.write(
'''line one
line two
line three
line four
''')
    dest = module.params['path']
    regexp = 'test'
    search_string = None
    line = module.params['line']
    insertafter = None
    insertbefore = None
    create = False
    backup = False
    backrefs = False
    firstmatch = module.params['firstmatch']

# Generated at 2022-06-13 05:34:56.558604
# Unit test for function present
def test_present():
    ''' Simulate present state '''
    from ansible.modules.files.lineinfile import present
    module = AnsibleModule({})
    dest = 'test'
    line = 'test'
    regexp = 'test'
    search_string = None
    insertafter = 'test'
    insertbefore = None
    create = False
    backup = False
    firstmatch = None
    present(module, dest, regexp, search_string, line, insertafter, insertbefore, create,
            backup, None, firstmatch)


# Generated at 2022-06-13 05:35:05.047673
# Unit test for function absent
def test_absent():
    module = AnsibleModule({
        'dest': 'test.txt',
        'line': 'test line',
        'state': 'absent'
    })
    f = 'test.txt'
    if os.path.exists(f):
        os.remove(f)
    with open(f, 'w+') as f:
        f.write('test line\n')
    absent(module, module.params['dest'], None, None, module.params['line'], True)


# Generated at 2022-06-13 05:35:09.717986
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec = dict(
        owner = dict(required = False),
        group = dict(required = False),
        mode = dict(required = False),
        seuser = dict(required = False),
        serole = dict(required = False),
        setype = dict(required = False),
        selevel = dict(required = False),
        unsafe_writes = dict(required=False, type='bool', default=False)
    ))
    module.params['owner']='root'
    module.params['group']='root'
    module.params['mode']='0755'
    module.params['seuser']='unconfined_u'
    module.params['serole']='unconfined_r'
    module.params['setype']='usr_t'

# Generated at 2022-06-13 05:35:12.111262
# Unit test for function present
def test_present():
    assert present(module, dest, regexp, search_string, line, insertafter, insertbefore, create,
            backup, backrefs, firstmatch) == (msg, changed)


# Generated at 2022-06-13 05:35:12.475671
# Unit test for function absent
def test_absent():
    pass



# Generated at 2022-06-13 05:35:26.054768
# Unit test for function write_changes
def test_write_changes():
    from ansible.utils.path import makedirs_safe
    from ansible.module_utils.basic import AnsibleModule
    import shutil
    import tempfile
    import os
    validate = None
    dest = "/tmp/abc.txt"
    # Used for testing on python3
    b_lines = [b"123"]
    tmpfd, tmpfile = tempfile.mkstemp(dir=tempfile.gettempdir())
    with os.fdopen(tmpfd, 'wb') as f:
        f.writelines(b_lines)
    class AFakeModule():
        params = { "validate":validate, "unsafe_writes" : True }
        def atomic_move(self, src, dest, unsafe_writes=False):
            return shutil.move(src, dest)

# Generated at 2022-06-13 05:35:34.756665
# Unit test for function present
def test_present():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(type='path'),
            regexp=dict(type='str'),
            search_string=dict(type='str'),
            line=dict(type='str'),
            insertafter=dict(type='str'),
            insertbefore=dict(type='str'),
            create=dict(type='bool', default=False),
            backup=dict(type='bool', default=False),
            backrefs=dict(type='bool', default=False),
            firstmatch=dict(type='bool', default=False),
        )
    )
    present(module, '/tmp/test_present1', None, None, 'line', 'BOF', None, True, False, False, False)

# Generated at 2022-06-13 05:35:45.167708
# Unit test for function absent
def test_absent():
    dest = "ansible/test_file_line.txt"
    regexp = "^test"
    search_string = "test"
    line = "test"
    backup = False
    module = MagicMock(
        name="module",
        params={},
        check_mode=False,
        exit_json=MagicMock(),
        backup_local=MagicMock(return_value=backup),
        _diff=False
    )
    type(module).params = PropertyMock(return_value={"dest": dest, "state": "absent", "regexp": regexp,
                                                     "search_string": search_string, "line": line, "backup": backup})
    with patch("os.open") as os_open:
        os_open.return_value = "file_obj"
       

# Generated at 2022-06-13 05:35:55.597414
# Unit test for function write_changes
def test_write_changes():
    args = [os.path.join(os.path.dirname(__file__), 'data', 'lineinfile.ini')]
    args2= [os.path.join(os.path.dirname(__file__), 'data', 'lineinfile.ini')]

    module = AnsibleModule(argument_spec={
                                            'path':{'type': 'path', 'required': True},
                                            'backup':{'type': 'bool', 'default': False},
                                            'mode':{'type': 'str'},
                                            'unsafe_writes':{'type': 'bool', 'default': False},
                                            'validate':{'type': 'str'}
                                            })
    os.chdir(os.path.dirname(__file__))
    module.ex

# Generated at 2022-06-13 05:36:30.628314
# Unit test for function check_file_attrs
def test_check_file_attrs():
    b_lines = ['a\n', 'b\n']
    lines = ['a', 'b']

# Generated at 2022-06-13 05:36:31.785736
# Unit test for function write_changes

# Generated at 2022-06-13 05:36:39.804651
# Unit test for function check_file_attrs

# Generated at 2022-06-13 05:36:49.640127
# Unit test for function present

# Generated at 2022-06-13 05:37:01.592695
# Unit test for function present
def test_present():
    lines = [b'first line\n', b'beforeregexp line\n', b'snippetstart\n', b'snippetend\n', b'afterregexp line\n']
    regexp = 'snippetstart'
    search_string = None
    line = 'changed line'
    insertafter = None
    insertbefore = 'afterregexp line'
    create = False
    backup = False
    backrefs = False
    firstmatch = False
    # 1. test that regexp is not matched, insertbefore is matched and line is inserted before it
    index = [-1, -1]
    bre_ins = re.compile(to_bytes(insertbefore, errors='surrogate_or_strict'))

# Generated at 2022-06-13 05:37:02.725836
# Unit test for function check_file_attrs
def test_check_file_attrs():
    #
    # type: (object, object, object) -> object
    return None



# Generated at 2022-06-13 05:37:12.751602
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec = dict(
        path = dict(required=True),
        owner = dict(),
        group = dict(),
        mode = dict()
    ))
    dest = '/tmp/test/file'
    file_args = module.params
    file_args['path'] = dest
    set_changed = module.set_fs_attributes_if_different(file_args, False, diff='')
    assert change_file_attrs(module, False, '', '') == ('ownership, perms or SE linux context changed', True)



# Generated at 2022-06-13 05:37:19.537233
# Unit test for function write_changes
def test_write_changes():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.six import PY2
    module = basic.AnsibleModule(
        argument_spec=dict(
            content=dict(type='str'),
            src=dict(type='path'),
            dest=dict(type='path', required=True),
            unsafe_writes=dict(type='bool', default=False),
            validate=dict(type='str', default=None),
        ))
    # create a temporary directory and write a file to it
    import tempfile
    tmpdir = tempfile.mkdtemp()
    test_path = os.path.join(tmpdir, 'test_path')

# Generated at 2022-06-13 05:37:28.749727
# Unit test for function main
def test_main():
    from ansible_collections.ansible.community.plugins.module_utils import basic
    from ansible_collections.ansible.community.plugins.module_utils._text import to_bytes


# Generated at 2022-06-13 05:37:30.012359
# Unit test for function absent
def test_absent():
    assert absent(None, dest="test_file", regexp=None, search_string=None, line="line_to_be_deleted", backup=None) == (False, 0, 'file not present', '')



# Generated at 2022-06-13 05:38:07.308932
# Unit test for function present

# Generated at 2022-06-13 05:38:08.305542
# Unit test for function write_changes
def test_write_changes():
    print("Not implemented")


# Generated at 2022-06-13 05:38:13.802967
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({})
    module.tmpdir = '_'
    module._debug = False
    b_lines = [b'a\n', b'b\n']
    dest = 'c'
    write_changes(module, b_lines, dest)
    assert os.path.exists('c') is True
    assert open('c', 'rb').read() == b'a\nb\n'
    os.remove('c')



# Generated at 2022-06-13 05:38:17.522307
# Unit test for function write_changes
def test_write_changes():
    tmpdir = tempfile.mkdtemp()
    tmpfile = tempfile.mkstemp(dir=tmpdir)
    f = open(tmpfile[1], 'w')
    f.write('foobar')
    f.close()

    b_lines = [b'foobar']
    write_changes(get_module(tmpdir=tmpdir), b_lines, tmpfile[1])



# Generated at 2022-06-13 05:38:28.773763
# Unit test for function present
def test_present():
    # function present
    module = ansible_module_create()
    dest = '/tmp/test_dest'
    line = 'test line'
    try:
        os.remove(dest)
    except OSError:
        pass
    # create the file
    with open(dest, 'w') as f:
        pass
    regexp = 'test_regexp'
    search_string = 'search string'
    insertafter = None
    insertbefore = None
    create = False
    backup = False
    backrefs = False
    firstmatch = False
    present(module, dest, regexp, search_string, line, insertafter, insertbefore, create,
            backup, backrefs, firstmatch)



# Generated at 2022-06-13 05:38:39.925642
# Unit test for function write_changes
def test_write_changes():
    mock_module = AnsibleModule(
        argument_spec=dict(
            dest=dict(required=True, type='str'),
            lines=dict(required=True, type='list'),
            bufsize=dict(required=False, type='int', default=16384),
            unsafe_writes=dict(required=False, type='bool', default=False),
            validate=dict(required=False, type='str'),
        ),
        supports_check_mode=True
    )
    mock_module.atomic_move = lambda src, dest, unsafe_writes: dest
    mock_module.run_command = lambda x: (0, "good", "")
    mock_module.tmpdir = "/tmp"

# Generated at 2022-06-13 05:38:42.036940
# Unit test for function main
def test_main():
    assert main() is None

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:38:55.772942
# Unit test for function present
def test_present():

    # FIXME: this method should be moved to the top as nested function
    def run_function(*args, **kwargs):
        '''
        This function is used to test the module

        '''
        module = AnsibleModule(*args, **kwargs)
        present(module, dest, regexp, search_string, line, insertafter, insertbefore, create,
                backup, backrefs, firstmatch)


# Generated at 2022-06-13 05:38:57.742944
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    assert True == True


# Generated at 2022-06-13 05:39:07.306595
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # Empty diff, no change, no message
    assert check_file_attrs(AnsibleModule({}), False, "", {}) == \
           ("No changes", False)
    # Empty diff, changed, same message
    assert check_file_attrs(AnsibleModule({}), True, "Changed something", {}) == \
           ("Changed something", True)
    # Changed diff, changed, same message
    assert check_file_attrs(AnsibleModule({}), True, "Changed something", {"before": "", "after": ""}) == \
           ("Changed something", True)
    # Changed diff, no change, added message

# Generated at 2022-06-13 05:39:44.015682
# Unit test for function present

# Generated at 2022-06-13 05:39:46.124224
# Unit test for function write_changes
def test_write_changes():
    # True unit tests coming soon!
    assert False



# Generated at 2022-06-13 05:39:54.818196
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_native
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import env_fallback
    from ansible.module_utils.six import PY2
    from ansible.module_utils.six import b
    import os

    if not PY2:
        from io import StringIO
    else:
        from StringIO import StringIO


# Generated at 2022-06-13 05:40:06.833035
# Unit test for function present
def test_present():
    module = AnsibleModule(argument_spec = dict(
        dest=dict(required=True),
        regexp=dict(required=False),
        search_string=dict(required=False),
        line=dict(required=True),
        insertafter=dict(required=False),
        insertbefore=dict(required=False),
        create=dict(required=False, type='bool', default=False),
        backup=dict(required=False, type='bool', default=False),
        backrefs=dict(required=False, type='bool', default=False),
        firstmatch=dict(required=False, type='bool', default=False),
        validate=dict(required=False, default=None, type='str')
    ))
    test_dest = 'test.txt'
    test_regexp = 'whatever'
    test

# Generated at 2022-06-13 05:40:18.925307
# Unit test for function present

# Generated at 2022-06-13 05:40:31.854438
# Unit test for function main
def test_main():
    args = dict(
        path = 'c:\\Temp\\testfile.txt',
        state = 'present',
        regexp = '',
        search_string = '',
        line = '',
        insertbefore = '',
        insertafter = '',
        create = '',
        backup = '',
        firstmatch = '',
        validate = ''
    )
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 05:40:40.658114
# Unit test for function present
def test_present():

    lines = [b'# Ansible managed: /tmp/foo modified on 2014-09-22 14:24:41 by root on ip-10-170-50-216\n',
             b'# This line will be changed\n',
             b'# This line will be added\n',
             b'# This line will be removed\n',
             b'# This line will stay untouched\n',
             b'# This line will be added\n',
             b'# This line must be the last one\n']

    # Prepare the environment
    # =======================
    # Create the test file
    fname = '/tmp/foo'
    fd1, tmp1 = tempfile.mkstemp()
    with open(tmp1, 'wb') as f:
        f.writelines(lines)

    # Module params
    module_args

# Generated at 2022-06-13 05:40:52.070316
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec=dict(src='', lines='', owner='', mode='', seuser='', serole='', setype='', backup=''))

    module.params = {'owner': 'adam', 'mode': '660', 'seuser': 'adam_u', 'serole': 'adam_r', 'setype': 'adam_t', 'backup': True}
    changed = True
    message = "line changed"
    msg, cn = check_file_attrs(module, changed, message, True)
    assert msg == "line changed and ownership, perms or SE linux context changed"


# Generated at 2022-06-13 05:40:59.901819
# Unit test for function present

# Generated at 2022-06-13 05:41:00.290790
# Unit test for function absent
def test_absent():
    pass



# Generated at 2022-06-13 05:42:02.034655
# Unit test for function main

# Generated at 2022-06-13 05:42:04.628296
# Unit test for function present
def test_present():
    o = present(module, dest, regexp, search_string, line, insertafter, insertbefore, create,
                backup, backrefs, firstmatch)
    assert o == None


# Generated at 2022-06-13 05:42:17.553019
# Unit test for function present
def test_present():
    module = AnsibleModule({
        "dest": "tests/testdata/unknown",
        "regexp": None,
        "insertafter": "",
        "insertbefore": "append_me",
        "line": "Hello World!",
        "create": True,
        "backup": False,
        "backrefs": False
        })

    # is the file there?
    dest = module.params.get('dest')
    assert not os.path.exists(dest)

    # if the file is not there, it should be created
    with open(dest, "a") as f:
        f.write(module.params.get('line'))

    # check if it has been created
    assert os.path.exists(dest)



# Generated at 2022-06-13 05:42:27.709388
# Unit test for function check_file_attrs
def test_check_file_attrs():
    dict1 = dict()
    test_module = AnsibleModule({})
    test_dict = dict()


    test_dict['test1'],test_dict['test2'] = check_file_attrs(test_module,True,"changed","changed")
    assert test_dict['test1'] == "changed and ownership, perms or SE linux context changed"
    assert test_dict['test2'] == True
    test_dict['test1'], test_dict['test2'] = check_file_attrs(test_module, False, "changed", "changed")
    assert test_dict['test1'] == "ownership, perms or SE linux context changed"
    assert test_dict['test2'] == True

# Generated at 2022-06-13 05:42:33.602247
# Unit test for function write_changes
def test_write_changes():
    from ansible.module_utils._text import to_bytes
    assert not write_changes(AnsibleModule(
        argument_spec=dict(validate='/bin/true %s'),
        supports_check_mode=True),
        to_bytes("line1", errors='surrogate_or_strict'),
        'testfile')



# Generated at 2022-06-13 05:42:38.155932
# Unit test for function absent
def test_absent():

    dest = '/root/abc.txt'
    regexp = '^Test\s'
    line = 'Test line'

    module = MagicMock()
    m_open = mock_open(read_data='Test line\nTest line1')
    with patch("__builtin__.open", m_open):
        absent(module, dest, regexp, None, line, 'yes')

# Generated at 2022-06-13 05:42:42.618090
# Unit test for function main
def test_main():

    # Setup
    import tempfile
    temp_file = tempfile.NamedTemporaryFile()
    temp_path = temp_file.name


    # Test function
    main()

    # Cleanup
    temp_file.close()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:42:53.728809
# Unit test for function check_file_attrs
def test_check_file_attrs():
    changed = False
    message = ""
    file_args = {}
    file_args["path"] = 'abc'
    file_args["owner"] = 'ansible'
    file_args["mode"] = '600'
    file_args["seuser"] = 'user'
    file_args["serole"] = 'role'
    file_args["setype"] = 'svirt_lxc_net_t'
    file_args["selevel"] = 's0'
    file_args["unsafe_writes"] = False
    diff = {'propagated': False, 'before_header': u'before /etc/hosts', 'after_header': u'after /etc/hosts', 'before': u'',
            'after': u'', 'before_lines': [], 'after_lines': []}

# Generated at 2022-06-13 05:43:01.258063
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec=dict(
            unsafe_writes=dict(type='bool', default=False),
            backup=dict(type='bool', default=False),
            _changes=dict(type='dict')
        )
    )
    b_lines = ["foo", "bar", "baz"]

    dest = "test.txt"
    tempfd, tempfile = tempfile.mkstemp(dir=module.tmpdir)
    with os.fdopen(tempfd, 'wb') as f:
        f.writelines(b_lines)

    module.atomic_move(tempfile, os.path.realpath(dest), unsafe_writes=module.params['unsafe_writes'])

    write_changes(module, b_lines, dest)

# Generated at 2022-06-13 05:43:08.910356
# Unit test for function present
def test_present():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(type='str', required=True),
            regexp=dict(type='str'),
            search_string=dict(type='str'),
            line=dict(type='str', required=True),
            insertafter=dict(type='str'),
            insertbefore=dict(type='str'),
            create=dict(type='bool', default=False),
            backup=dict(type='bool', default=False),
            backrefs=dict(type='bool', default=True),
            firstmatch=dict(type='bool', default=False),
            validate=dict(type='str'),
            unsafe_writes=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
    )

    dest = os.path.join