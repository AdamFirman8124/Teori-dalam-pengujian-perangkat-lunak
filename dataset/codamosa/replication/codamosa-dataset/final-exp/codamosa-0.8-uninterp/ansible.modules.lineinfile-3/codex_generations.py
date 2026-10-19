

# Generated at 2022-06-13 05:34:52.378002
# Unit test for function present
def test_present():
    b_module = AnsibleModule(argument_spec={'dest':{'type': 'path', 'required': True},
                                            'regexp':{'type': 'str'},
                                            'search_string':{'type': 'str'},
                                            'line':{'type': 'str'},
                                            'insertbefore':{'type': 'str'},
                                            'insertafter':{'type': 'str'},
                                            'create':{'type': 'bool'},
                                            'backup':{'type': 'bool'},
                                            'backrefs':{'type': 'bool'},
                                            'firstmatch':{'type': 'bool'},
                                            })

    dest = '/tmp/test_present'

# Generated at 2022-06-13 05:35:05.568801
# Unit test for function present
def test_present():

    lines = ['# this is a comment\n', '# this is another comment\n', '\n']

    # valid:
    # - passed the checks, line added, changed=True
    # - line already added, nothing to do
    # - line added and deleted, change=True
    # - line added and present with to_lines, changed=True
    # - passed no regexp, no backrefs, line added, changed=True
    # - passed regexp, line added, changed=True
    # - passed regexp, no match no insert, line added, changed=True
    # - passed regexp, no match with insertbefore, line added, changed=True
    # - passed regexp, no match with insertafter, line added, changed=True
    # - passed regexp, match with insertbefore, line added, changed=True
    # -

# Generated at 2022-06-13 05:35:18.772476
# Unit test for function write_changes
def test_write_changes():
    import tempfile
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception

    # Create a fake module
    lines = [
        b'Something is going to happen here\n',
        b'More things \n',
        b'Some things happen here\n',
        b'Other things happen here\n'
    ]

    test_data_path = os.path.join(os.path.dirname(__file__), 'test_data')
    data_path = os.path.join(test_data_path, 'lineinfile_test_file')

    tmpfd, tmpfile = tempfile.mkstemp()

# Generated at 2022-06-13 05:35:28.599937
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec = dict(
        path = dict(type=str),
        owner = dict(type=str, default=None),
        group = dict(type=str, default=None),
        seuser = dict(type=str, default=None),
        setype = dict(type=str, default=None),
        context = dict(type=str, default=None),
        mode = dict(type=str, default=None),
    ))

    try:
        file_args = module.load_file_common_arguments(module.params)
    except TypeError:
        file_args = module.load_file_common_arguments(dict(path=module.params['path']))
    changed = module.set_fs_attributes_if_different(file_args, False, diff=dict())


# Generated at 2022-06-13 05:35:39.708979
# Unit test for function absent
def test_absent():
    b_dest = to_bytes('/tmp/testfile', errors='surrogate_or_strict')
    b_lines = [to_bytes('Hello World', errors='surrogate_or_strict'), to_bytes('This is a line, this is another line', errors='surrogate_or_strict')]
    regexp = None
    search_string = to_bytes('This is a', errors='surrogate_or_strict')
    line = to_bytes('This is a line, this is another line', errors='surrogate_or_strict')
    backup = True
    if not os.path.exists(b_dest):
        open(b_dest, 'wb').close()

# Generated at 2022-06-13 05:35:45.289849
# Unit test for function absent
def test_absent():
    module = AnsibleModule(argument_spec=dict(
        dest=dict(required=True),
        regexp=dict(required=False),
        search_string=dict(required=False),
        line=dict(required=True),
    ))
    regexp = None
    search_string = None
    line = '  dest = /tmp/ansible'
    dest = '/tmp/ansible'
    absent(module, dest, regexp, search_string, line, False)



# Generated at 2022-06-13 05:35:55.714873
# Unit test for function write_changes
def test_write_changes():
    import os, tempfile
    # create some temporary file to work with
    tmpfd, tmpfile = tempfile.mkstemp()
    with os.fdopen(tmpfd, 'wb') as f:
        f.writelines([b"a test\n", b"another\n"])

    resultfile = tmpfile + ".copy"

    # create a new ansible module object
    module = AnsibleModule(argument_spec={})
    # pretend the tmpfile exists
    module.params['path'] = tmpfile
    # pretend the tmpfile is a valid file
    module.atomic_move = lambda src, dest, unsafe_writes=False: os.rename(src, dest)
    # run the write changes function
    write_changes(module, [b"a test\n", b"new changed line\n"], resultfile)
   

# Generated at 2022-06-13 05:36:02.711259
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    file_args = module.load_file_common_arguments(module.params)
    assert check_file_attrs(module, False, "Message", "diff") == ("Message and ownership, perms or SE linux context changed", True)



# Generated at 2022-06-13 05:36:13.800649
# Unit test for function absent
def test_absent():
    """
    This function tests the function absent
    """
    # Argument spec for function absent
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(required=True),
            regexp=dict(required=False, default=None),
            search_string=dict(required=False, default=None),
            line=dict(required=False, default=None),
            backup=dict(required=False, default='no'),
        ),
        supports_check_mode=True,
    )
    dest = 'dest'
    regexp = None
    search_string = 'test'
    line = None
    backup = 'no'
    dest_path = os.path.join(os.path.dirname(__file__), dest)
    dest_file = open(dest_path, 'w')
    dest

# Generated at 2022-06-13 05:36:22.225072
# Unit test for function write_changes
def test_write_changes():
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
    module = AnsibleModule(
        argument_spec = dict(
            param1=dict(type='str', default='test'),
            param2=dict(type='int', required=True),
        ),
    )
    b_lines = []
    dest = 'myDest'
    write_changes(module, b_lines, dest)

# For backwards compatibility

# Generated at 2022-06-13 05:37:05.134348
# Unit test for function main
def test_main():
    module = get_module_mock(params={
        'path':"/tmp/file.txt",
        'state':'present',
        'regexp':'string',
        'search_string':'string',
        'line':'string',
        'insertafter':'string',
        'insertbefore':'string',
        'backrefs':False,
        'create':True,
        'backup':True,
        'firstmatch':True,
        'validate':'string',
    })

    def get_bin_path(name, opts=None):
        return ' '.join([name])

    def get_ex_code(cmd, shell):
        return 0

    module = get_module_attribute(module, 'get_bin_path', get_bin_path)
    module = get_module_attribute

# Generated at 2022-06-13 05:37:07.727940
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({'path': '/etc/hostname', 'unsafe_writes': True}, check_invalid_arguments=False)
    changed = False
    message = ''
    diff = ''
    assert [message, changed] == check_file_attrs(module, changed, message, diff)
    module.exit_json(**{'changed': False})


# Generated at 2022-06-13 05:37:16.707225
# Unit test for function present
def test_present():

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    dest = '/tmp/testfile'
    temp_dir = tempfile.mkdtemp()

# Generated at 2022-06-13 05:37:18.910419
# Unit test for function present
def test_present():
    assert present(None, '/tmp/config', '^(host=).*', None, '\1my_host', None, None, True, False, True, False) is None


# Generated at 2022-06-13 05:37:27.824528
# Unit test for function write_changes
def test_write_changes():
    testfile = tempfile.mkstemp()
    result = ''
    try:
        with os.fdopen(testfile[0], 'w') as f:
            f.write('1\n2\n3\n')
        b_lines = [b'1\n', b'hello world\n', b'3\n']
        write_changes(None, b_lines, testfile[1])
        with open(testfile[1], 'r') as f:
            result = f.read()
        assert result == '1\nhello world\n3\n'
    finally:
        os.unlink(testfile[1])

# Back-references for replace
#
# Allows for \1, \2, \3... to be used in line, with \1 being whatever the first
# group in regexp matched

# Generated at 2022-06-13 05:37:36.903090
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule, EnvironmentError

    def my_open(path, mode):
        return open('/tmp/test.txt', mode)

    def my_remove(path):
        pass

    def my_exists(path):
        return True

    def my_open_fail(path, mode):
        raise IOError

    def my_close(f):
        f.close()

    def my_env_error(path, mode):
        raise EnvironmentError

    def my_close_fail(f):
        raise IOError

    def write_changes(module, lines, dest):
        f = my_open('/tmp/test.txt', 'w')
        my_close(f)

    def check_file_attrs(module_instance, changed, msg):
        return msg, changed



# Generated at 2022-06-13 05:37:50.120503
# Unit test for function write_changes
def test_write_changes():
    import ansible.module_utils.basic
    (rc, out, err) = ansible.module_utils.basic.run_command('which true')
    assert rc == 0
    assert out
    module = AnsibleModule(argument_spec={'validate': {'type': 'str', 'required': False, 'default': '/bin/true %s'}})
    os.mkdir('/tmp/ansible')
    b_lines = [b'foo']
    write_changes(module, b_lines, '/tmp/ansible/bar')
    assert os.path.isfile('/tmp/ansible/bar')
    assert os.path.isfile('/tmp/ansible/bar.ansible_backup')
    os.unlink('/tmp/ansible/bar')

# Generated at 2022-06-13 05:37:59.495452
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(type='path'),
            regexp=dict(type='str'),
            search_string=dict(type='str'),
            line=dict(type='str')
        ),
        supports_check_mode=True
    )
    # The strings and locations in these lines need to be chosen carefully
    # to not give false positives or negatives.
    module.params['dest'] = '/tmp/testfile'
    module.params['line'] = "the cat sat on the mat"
    module.params['regexp'] = r"^the [cC]at (sat|slept) on the [mM]at$"
    # This is the initial content of the file.
    # Note the extra lines at the top, bottom and immediately after the
    # target line

# Generated at 2022-06-13 05:38:09.887770
# Unit test for function absent
def test_absent():
    test = {
        'dest': '/tmp/test_ansible_lineinfile',
        'line': 'first line',
        'regexp': 'second line',
        'search_string': 'second line',
        'expected_results': {
            'changed': True,
            'found': 2
        }
    }

    with open(test['dest'], 'w') as f:
        f.write('first line\nsecond line')
        f.write('second line\nthird line')
    module_args = dict(
        dest=test['dest'],
        regexp=test['regexp'],
        state='absent'
    )
    # Create a mock module object

# Generated at 2022-06-13 05:38:20.817126
# Unit test for function absent
def test_absent():

    test_line = '#This is test line'
    test_file = 'testfile.txt'
    test_regex = '#.*'
    test_search = '^#'


# Generated at 2022-06-13 05:39:17.107811
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule, get_exception
    import ansible.module_utils.common.collection
    import ansible.module_utils.common.file
    import ansible.module_utils.common.validation


# Generated at 2022-06-13 05:39:24.809676
# Unit test for function write_changes
def test_write_changes():

    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(type='path', default=None, required=True),
            b_lines=dict(type='raw', default=None, required=True),
        )
    )
    b_lines = to_bytes(module.params['b_lines'])
    dest = to_bytes(module.params['dest'])
    write_changes(module, b_lines, dest)
    assert os.path.exists(dest)
    with open(dest, 'rb') as f:
        assert b_lines == f.read()


# Generated at 2022-06-13 05:39:33.148884
# Unit test for function present
def test_present():
    '''
    Test function with valid and invalid parameters
    :return:
    '''
    import imp
    import os
    import shutil
    import tempfile

    from ansible.module_utils.basic import AnsibleModule

    # Make a temp dir to work in
    tmpdir = tempfile.mkdtemp()

    # Make a fake src and dest file
    src = os.path.join(tmpdir, "src.txt")
    dest = os.path.join(tmpdir, "dest.txt")

    with open(src, "w") as f:
        f.write('''line1
line2
line3''')

    # Make the fake module args

# Generated at 2022-06-13 05:39:45.586911
# Unit test for function absent
def test_absent():
    module = AnsibleModule(argument_spec=dict(
        backup=dict(required=False, default=False, type='bool'),
        dest=dict(required=True, type='path'),
        line=dict(required=True, type='str'),
        regexp=dict(required=False, type='str'),
        search_string=dict(required=False, type='str'),
        state=dict(required=False, default='present', choices=['absent', 'present'])
    ))
    dest = '/tmp/test.txt'
    regexp = None
    search_string = None
    changed = False
    if os.path.isfile(dest):
        with open(dest, 'r+', encoding='utf-8') as f:
            lines = f.readlines()
            line = 'some line\n'
           

# Generated at 2022-06-13 05:39:46.385250
# Unit test for function write_changes
def test_write_changes():
    assert True
    
    

# Generated at 2022-06-13 05:39:54.985644
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    import shutil
    import os
    import io
    import contextlib
    from tempfile import mkstemp
    from ansible.module_utils import basic

    # create a temp file
    (fd, test_file) = mkstemp()

    print(test_file)

    # create a temp directory
    (fd, test_dir) = mkstemp()

    print(test_dir)

    # remove the temp file and make it a directory
    os.remove(test_file)
    os.mkdir(test_file)


    # create a module object

# Generated at 2022-06-13 05:40:03.015604
# Unit test for function write_changes
def test_write_changes():
    with tempfile.TemporaryDirectory() as tmpdir:
        module = AnsibleModule({
            'path': __file__,
            'search_string': 'foo',
            'line': 'foobar',
            'backup': False,
            'tmpdir': tmpdir,
            'unsafe_writes': True
        })
        b_lines = to_bytes(module.params['line'] + '\n', errors='surrogate_or_strict')
        write_changes(module, b_lines, module.params['path'])
        with open(module.params['path'], 'rb') as f:
            new_content = f.read()
        assert new_content == b_lines



# Generated at 2022-06-13 05:40:04.791791
# Unit test for function write_changes
def test_write_changes():
    '''
    test_file_exists:
    '''
    assert True


# Generated at 2022-06-13 05:40:17.540689
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec = dict(path = dict()))
    module.params['path'] = '/test/file'
    module.params['owner'] = 'test'
    module.params['group'] = 'group'
    module.params['seuser'] = 'user'
    module.params['serole'] = 'role'
    module.params['setype'] = 'type'
    module.params['selevel'] = 'level'
    module.params['mode'] = '0400'
    changed = True
    diff = {'before_header': '', 'diff': '', 'after_header': ''}
    message, changed = check_file_attrs(module, changed, '', diff)
    assert isinstance(message, str)
    assert message == 'ownership, perms or SE linux context changed'


# Generated at 2022-06-13 05:40:31.071501
# Unit test for function main
def test_main():
    """ Test function main()"""

    class TestException(Exception):
        """ TestException class"""
        pass

    # Unit test for function main with error
    def err_raise_exception(s):
        """ Error function for raising exception"""
        raise TestException()

    def err_return(s):
        """ Error function for returning"""
        yield s

    base_path = '/tmp/ansible-test'
    path = os.path.join(base_path, 'file')
    regexp = None
    search_string = None
    ins_bef = None
    ins_aft = None
    create = False
    backup = False
    backrefs = False
    firstmatch = False
    line = 'new line'

    # Test for raising exception
    m = MagicMock()

# Generated at 2022-06-13 05:42:25.536291
# Unit test for function main

# Generated at 2022-06-13 05:42:35.009953
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(type='path'),
            regexp=dict(type='str'),
            search_string=dict(type='str'),
            line=dict(type='str'),
            backup=dict(type='bool', default=False)
        ),
        required_one_of=[['regexp', 'search_string', 'line']],
    )
    module.params['dest'] = './testfile'
    absent(module, './testfile', '^test', None, 'test', module.params['backup'])



# Generated at 2022-06-13 05:42:44.521506
# Unit test for function present

# Generated at 2022-06-13 05:42:46.995039
# Unit test for function main
def test_main():
    main()
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:42:52.247161
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec=dict(path=dict(type='str', required=True),
                                              _diff_peek=dict(type='bool', default=True),
                                              _backup=dict(type='bool', default=False),
                                              owner=dict(type='str'),
                                              group=dict(type='str'),
                                              mode=dict(type='str'),
                                              seuser=dict(type='str'),
                                              serole=dict(type='str'),
                                              selevel=dict(type='str')
                                             )
                          )
    changed = False
    message = 'fake message'

# Generated at 2022-06-13 05:42:59.451088
# Unit test for function write_changes
def test_write_changes():
    # We can't use the mock module here because it doesn't work with
    # python -m pytest test/units/modules/file_lineinfile.py, only with py.test
    # This is because ansible.module_utils.basic.AnsibleModule is a class
    # and it doesn't get read by the mock module (not a method, not a function)
    # So we use monkeypatch
    # See http://pythontesting.net/framework/pytest/pytest-monkeypatch/
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import common
    import tempfile
    import os
    import os.path
    # Tests for module.atomic_move
    import shutil
    m_atomic_move_called = False
    m_os_rename_called = False


# Generated at 2022-06-13 05:43:08.642177
# Unit test for function absent
def test_absent():
    module = AnsibleModule(argument_spec={
        "dest": {"required": True},
        "line": {},
        "regexp": {},
        "search_string": {},
        "backup": {"default": False, "type": "bool"},
    })
    b_dest = to_bytes('test.txt', errors='surrogate_or_strict')

    with open(b_dest, 'w') as f:
        f.write('test line 1\n')
        f.write('test line 2\n')
        f.write('test line 3\n')

    dest = to_text(b_dest)
    regexp = 'line'
    search_string = None
    line = 'test line 1'
    backup = True

# Generated at 2022-06-13 05:43:13.791771
# Unit test for function main
def test_main():
    testdata = {
        'name': 'test.cfg',
        'path': 'test.cfg',
        'state': 'present',
        'line': 'test line',
        'backup': False,
        'regexp': None,
        'search_string': None,
        'firstmatch': False,
        'backrefs': False,
        'create': False,
        'insertbefore': None,
        'insertafter': None,
    }

# Generated at 2022-06-13 05:43:17.354595
# Unit test for function absent
def test_absent():
    a1 = {
        'dest': '/tmp/test.txt',
        'regexp': None,
        'search': 'line1',
        'line': 'line1',
        'backup': False
    }
    assert absent(a1) == 'not found'


# Generated at 2022-06-13 05:43:25.182902
# Unit test for function check_file_attrs
def test_check_file_attrs():
    '''
    tempfile.mkstemp()
    '''
    tmpfd, tmpfile = tempfile.mkstemp()
    os.close(tmpfd)
    module = AnsibleModule(argument_spec={'owner': {'type': 'str',},
                             'group': {'type': 'str',},
                             'mode': {'type': 'str',},
                             'selevel': {'type': 'str',},
                             'serole': {'type': 'str',},
                             'setype': {'type': 'str',},
                             'seuser': {'type': 'str',},},
                             supports_check_mode=True)

    args = module.params
    args['path'] = tmpfile
    changed = False
    message = ""

    ret = check_file_attrs