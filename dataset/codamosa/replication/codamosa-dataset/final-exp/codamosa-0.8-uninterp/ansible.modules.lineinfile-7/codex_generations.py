

# Generated at 2022-06-13 05:34:41.832849
# Unit test for function main
def test_main():
    b_path = to_bytes("tests/files/test.txt", errors='surrogate_or_strict')
    test_args = dict(
        path=b_path,
        state="present",
        regexp="^test",
        search_string=None,
        line="test",
        insertafter=None,
        insertbefore=None,
        backrefs=False,
        create=False,
        backup=False,
        firstmatch=False,
        validate=None,
    )
    with pytest.raises(SystemExit):
        main(test_args)


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:34:52.376608
# Unit test for function write_changes
def test_write_changes():

    filename = '/tmp/testfile'
    f = open(filename, 'w')
    f.write('the value of foo is: foo')
    f.close()

    lines = [b'the value of bar is: bar']
    module = AnsibleModule({
        'path': filename,
        'line': 'bar',
        'validate': 'cat %s'
    })

    write_changes(module, lines, filename)

    f = open(filename, 'r')
    for line in f.readlines():
        assert(line.rstrip() == 'the value of bar is: bar')
    f.close()
    os.remove(filename)



# Generated at 2022-06-13 05:35:05.569326
# Unit test for function present
def test_present():
    b_lines = [b"127.0.0.1\tlocalhost\n",b"127.0.0.1\tlocalhost.localdomain\tlocalhost test\n"]
    dest = "/tmp/test_line.txt"
    regexp = 'test'
    search_string = None
    line = 'test-test-test'
    insertafter = None
    insertbefore = 'localdomain'
    create = False
    backup = False
    backrefs = True
    firstmatch = False
    write_changes(module, b_lines, dest)
    test_present(module, dest, regexp, search_string, line, insertafter, insertbefore, create, backup, backrefs, firstmatch)
    assert os.path.exists(dest)

# Generated at 2022-06-13 05:35:14.120407
# Unit test for function present
def test_present():
    module = AnsibleModule({'state': 'present',
                            'path': '/tmp/foo',
                            'line': 'bar',
                            'insertafter': 'BOF',
                            'create': True,
                            'firstmatch': False})

    # Copy of original method, so we can call it without `self`
    def mock_run_command(cmd, *args, **kwargs):
        return (1, '', '')

    # Write the actual results of the module to a file
    from ansible_collections.ansible.community.tests.unit.modules.utils import set_module_args
    set_module_args(module._store_representation)

# Generated at 2022-06-13 05:35:18.582574
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({'path':'/etc/passwd'})
    setattr(module, 'set_fs_attributes_if_different', lambda x,y: True)
    message = ''
    diff = 'diff'
    changed = False
    result = check_file_attrs(module, changed, message, diff)
    assert result == ('ownership, perms or SE linux context changed', True)

    module = AnsibleModule({'path': '/etc/passwd'})
    setattr(module, 'set_fs_attributes_if_different', lambda x, y: False)
    message = 'Hello '
    diff = 'diff'
    changed = True
    result = check_file_attrs(module, changed, message, diff)

# Generated at 2022-06-13 05:35:28.461787
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(required=True),
            regexp=dict(),
            search_string=dict(),
            line=dict(required=True),
            backup=dict(default=False, type='bool')
        )
    )
    dest = '/tmp'
    regexp = None
    search_string = "grep"
    line = 'root:x:0:0:root:/root:/bin/bash'
    backup = False
    def write_changes(module, b_lines, dest):
        with open(dest, 'wb') as f:
            f.writelines(b_lines)
    absent(module, dest, regexp, search_string, line, backup)



# Generated at 2022-06-13 05:35:39.679058
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(type='path'),
            regexp=dict(type='str', no_log=True),
            search_string=dict(type='str', no_log=True),
            line=dict(type='str', no_log=True),
            backup=dict(type='bool', default=False)
        ),
        supports_check_mode=True,
        mutually_exclusive=[('search_string', 'regexp')]
    )
    module.params['dest'] = 'test_lines'
    module.params['line'] = 'hello world'
    test_module_utils.create_file(module.params['dest'], 'hello world\nfoo bar\n')
    absent(module, **module.params)

# Generated at 2022-06-13 05:35:40.308145
# Unit test for function absent
def test_absent():
    pass



# Generated at 2022-06-13 05:35:44.873213
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({})
    changed, message = False, ''
    result = check_file_attrs(module, changed, message, {})
    assert result == ('ownership, perms or SE linux context changed', True)



# Generated at 2022-06-13 05:35:46.083466
# Unit test for function write_changes
def test_write_changes():
    write_changes()


# Generated at 2022-06-13 05:36:10.239480
# Unit test for function absent
def test_absent():
    from ..mock import (mock_open, Mock)
    from ..unit_tests.unit_test_utils import (set_module_args,
                                              exit_json, fail_json,
                                              AnsibleExitJson, AnsibleFailJson)
    import contextlib
    import os
    import shutil
    import tempfile

    @contextlib.contextmanager
    def create_file(contents):
        fake_file = tempfile.NamedTemporaryFile(mode='wb', delete=False)
        fake_file.write(to_bytes(contents))
        fake_file.close()
        yield fake_file
        os.unlink(fake_file.name)


# Generated at 2022-06-13 05:36:20.933012
# Unit test for function absent
def test_absent():
    import os
    filepath = '/tmp/ansible.txt'

    # Create files
    with open(filepath, 'w') as text_file:
        text_file.write(u'')

    # Remove files
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(required=True, type='str', no_log=True),
            regexp=dict(required=False),
            search_string=dict(required=False),
            line=dict(required=True),
            backup=dict(default=False, type='bool')
        )
    )
    absent(module=module, dest=filepath, regexp=None, search_string=None, line=u'', backup=True)
    assert os.path.isfile(filepath)
    assert os.stat(filepath).st

# Generated at 2022-06-13 05:36:30.456152
# Unit test for function write_changes
def test_write_changes():
    lines = b"""
    This is line 1
    This is line 2
    """
    module = type(str("fake_module"), (object, ), {
        "params": {
            "validate": None,
            "unsafe_writes": True,
            "tmpdir": "/tmp"
        },
        "run_command": lambda self, cmd: (0, None, None),
        "atomic_move": lambda self, src, dest, unsafe_writes: True,
        "fail_json": lambda self, msg: False
    })
    write_changes(module, to_bytes(lines, errors='surrogate_or_strict'), "/tmp/testfile.txt")



# Generated at 2022-06-13 05:36:38.192609
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({'tmpdir': tempfile.gettempdir()})
    dest = '''{0}/test_write_changes_{1}'''.format(tempfile.gettempdir(), os.getpid())
    b_lines = [b'Hello World']
    write_changes(module, b_lines, dest)
    with open('{0}'.format(dest), 'rb') as file_object:
        b_lines = file_object.readlines()
        assert to_text(b_lines[0], errors='surrogate_or_strict') == "Hello World"
    os.remove(dest)



# Generated at 2022-06-13 05:36:39.366785
# Unit test for function check_file_attrs
def test_check_file_attrs():
    check_file_attrs(AnsibleModule(), True, "", {})


# Generated at 2022-06-13 05:36:39.852231
# Unit test for function write_changes
def test_write_changes():
    pass


# Generated at 2022-06-13 05:36:43.829599
# Unit test for function present
def test_present():
    module = AnsibleModule({
        'path': 'index.html',
        'insertafter': 'EOF',
        'line': 'Hello World'
    })
    return module.run_command(['touch', 'index.html'])



# Generated at 2022-06-13 05:36:44.750027
# Unit test for function write_changes
def test_write_changes():
    pass



# Generated at 2022-06-13 05:36:49.133910
# Unit test for function write_changes
def test_write_changes():
    class FakeModule:
        params = {}

        def fail_json(self, *args, **kwargs):
            raise Exception(args[0])

        def atomic_move(self, tmpfile, dest, unsafe_writes=False):
            pass

        def run_command(self, cmd):
            pass
    write_changes(FakeModule(), [], '')



# Generated at 2022-06-13 05:37:01.686344
# Unit test for function check_file_attrs
def test_check_file_attrs():
    """
    Unit test for function check_file_attrs
    """
    from ansible.modules import lineinfile
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 05:37:32.881087
# Unit test for function present
def test_present():
  dest = "/tmp/test_present"
  regexp = r"^(.*)present(.*)$"
  insertbefore = r"^(.*)insertbefore(.*)$"
  filename = open(dest, "w")

# Generated at 2022-06-13 05:37:41.382153
# Unit test for function main
def test_main():
    import ansible.utils.template
    os.environ['ANSIBLE_MODULE_ARGS'] = """path: /etc/ansible/facts.d/test.fact
state: present
regexp: ^var2
line: var2=something
backrefs: False
firstmatch: False
backup: False
"""
    from ansible.module_utils.basic import *
    main()

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 05:37:53.208346
# Unit test for function absent
def test_absent():
    module = type('args', tuple(), dict(params={'backup':False,
    'dest':'/tmp/unique_file',
    'regexp':None,
    'search_string':None,
    'line':'line_string_to_search',
    'state':'absent'}))()

    with open(module.params['dest'], 'w') as f:
        f.write('line_string_to_search\n')

    absent(module, module.params['dest'], module.params['regexp'],
           module.params['search_string'], module.params['line'], module.params['backup'])
    assert os.path.exists(module.params['dest']) == False


# Generated at 2022-06-13 05:38:07.977896
# Unit test for function check_file_attrs
def test_check_file_attrs():
    test_module = AnsibleModule(argument_spec={'path': {'type': 'str'}, 'changes': {'type': 'dict'}, 'fail_on_diff': {'type': 'bool'}, 'backup': {'type': 'bool'}, 'owner': {'type': 'str'}, 'group': {'type': 'str'}, 'seuser': {'type': 'str'}, 'serole': {'type': 'str'}, 'setype': {'type': 'str'}, 'selevel': {'type': 'str'}, 'unsafe_writes': {'type': 'bool'}, 'follow': {'type': 'bool', 'default': False}, 'mode': {'type': 'str', 'default': '0600'}, '_diff': {'type': 'bool', 'default': True}})
   

# Generated at 2022-06-13 05:38:19.074508
# Unit test for function present
def test_present():
    import os
    import tempfile
    import shutil

    # initial script content
    test_script_content = ''
    with open(tmp, 'w') as test_script:
        test_script.write(test_script_content)

    # test script for test of function 'present'

# Generated at 2022-06-13 05:38:24.430528
# Unit test for function write_changes
def test_write_changes():
    module=AnsibleModule({})
    b_lines=b'test'
    dest='/tmp/test'
    module.atomic_move = True
    write_changes(module, b_lines, dest)
    assert os.path.exists(dest)


# Generated at 2022-06-13 05:38:35.232647
# Unit test for function main
def test_main():
    ones_path = ('/home/somebody/.ansible/tmp/ansible-tmp-1472608700.25-120691407972317/source/sample_of_file')
    f = open(ones_path)
    module = AnsibleModule({}, f.read())
    f.close()
    module.params = {'regexp': '', 'backup': False, 'path': '/etc/ansible/hosts', 'insertbefore': None, 'regex': '', 'search_string': '', 'backrefs': False, 'firstmatch': False, 'line': 'some_line\n', 'create': False, 'insertafter': None, 'state': 'present'}
    main()

# Generated at 2022-06-13 05:38:45.004498
# Unit test for function present
def test_present():
    '''
    Unit test for function present
    '''
    backup=False
    check_mode=False
    create=False
    dest="/root/xyz.txt"
    insertafter="BOF"
    insertbefore=None
    line="xyz"
    regexp=None
    search_string=None
    state="present"
    backrefs=False
    firstmatch=False
    unsafe_writes=False
    b_dest = to_bytes(dest, errors='surrogate_or_strict')
    diff = {'before': '',
            'after': '',
            'before_header': '%s (content)' % dest,
            'after_header': '%s (content)' % dest}

# Generated at 2022-06-13 05:38:50.257764
# Unit test for function main
def test_main():
    b_path = to_bytes('/tmp/test_main.txt')
    with open(b_path, 'w') as f:
        f.write('Append line to file')
    present(module, b_path, regexp=None, search_string=None, line = 'This is appended line', ins_aft='EOF', ins_bef=None, create=False, backup=False, backrefs=False, firstmatch=False)
    os.remove(b_path)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:38:59.749865
# Unit test for function absent
def test_absent():
    module = AnsibleModule(
        argument_spec=dict(
            dest=dict(type='path', required=True),
            regexp=dict(type='str', required=False),
            search_string=dict(type='str', required=False),
            line=dict(type='str', required=False, default=None),
            backup=dict(type='bool', required=False, default=False),
        ),
        supports_check_mode=True
    )

    module.exit_json = Mock(return_value=module)

    module.check_mode = False
    dest = 'test.txt'
    regexp = None
    search_string = 'test'
    line = None
    backup = False

    content = ['12345\n', 'test\n', 'test\n']

# Generated at 2022-06-13 05:39:46.773222
# Unit test for function absent
def test_absent():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils import common_koji
    module = AnsibleModule(
        argument_spec = dict(
            dest = dict(required=True),
            regexp = dict(required=False),
            search_string = dict(required=False),
            line = dict(required=True),
            backup = dict(default=False, type='bool')
        ),
        supports_check_mode=True
    )

    import tempfile
    tmpdir = tempfile.mkdtemp()
    tmpfile = tempfile.mktemp(dir=tmpdir)

    fd = open(tmpfile, 'w')
    fd.write('#test')
    fd.close()

    module.absent(tmpfile, 'test', None, 'test')
   

# Generated at 2022-06-13 05:39:48.359913
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs(1, True, 1, True)



# Generated at 2022-06-13 05:39:55.780917
# Unit test for function check_file_attrs
def test_check_file_attrs():

    from ansible.modules.files import file
    from ansible.module_utils.six.moves import StringIO


# Generated at 2022-06-13 05:40:07.391835
# Unit test for function present
def test_present():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True, type='str'),
            regexp = dict(type='str'),
            line = dict(required=True, type='str'),
            insertafter = dict(type='str'),
            insertbefore = dict(type='str'),
            create = dict(type='bool', default='no'),
            backup = dict(type='bool', default='no'),
            backrefs = dict(type='bool', default='no'),
            firstmatch = dict(type='bool', default='no'),
        ),
        supports_check_mode=True
    )
    dest = module.params.get('path')
    regexp = module.params.get('regexp')
    line = module.params.get('line')
    insertafter = module.params.get

# Generated at 2022-06-13 05:40:18.957895
# Unit test for function check_file_attrs
def test_check_file_attrs():
    import tempfile
    import os
    from shutil import rmtree

    assert_msg = "Unit test for function check_file_attrs"
    test_dir = tempfile.mkdtemp()
    test_file = "%s/test_file" % test_dir
    open(test_file, 'a').close()
    initial_stat = os.stat(test_file)

    module = AnsibleModule(argument_spec={'path':{'type':'str', 'required': True}})

    os.chmod(test_file, 0o644)
    changed, message = False, ""
    changed, message = check_file_attrs(module, changed, message, True)
    assert changed == False, assert_msg
    assert message == "", assert_msg


# Generated at 2022-06-13 05:40:21.207371
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # Execute the function check_file_attrs
    check_file_attrs()



# Generated at 2022-06-13 05:40:32.159455
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True),
            owner = dict(),
            group = dict(),
            mode = dict(),
            backup = dict(default=True,type='bool'),
            unsafe_writes = dict(type='bool', default=False),
        )
    )
    changed = False
    message = ""
    diff = ""
    assert(check_file_attrs(module, changed, message, diff) == ("ownership, perms or SE linux context changed", True))

    changed = True
    assert(check_file_attrs(module, changed, message, diff) == ("ownership, perms or SE linux context changed", True))


# Generated at 2022-06-13 05:40:32.589412
# Unit test for function write_changes
def test_write_changes():
    pass



# Generated at 2022-06-13 05:40:41.291847
# Unit test for function main
def test_main():
    # All of these can probably be mocked, but I'm not sure how to do that
    # with AnsibleModule yet.

    def run_module(*args, **kwargs):
        # Initialize args
        if args is None:
            args = ()

        # Initialize kwargs
        if kwargs is None:
            kwargs = {}

        # Needing to import this here is bad, but AnsibleModule
        # doesn't seem to play nice with the unittesting framework.
        from ansible.module_utils.basic import AnsibleModule
        module = AnsibleModule(*args, **kwargs)
        main()

    # Let's first test that if we provide only line, a regexp and a
    # search_string that we get an error.

# Generated at 2022-06-13 05:40:41.911587
# Unit test for function absent
def test_absent():
    pass



# Generated at 2022-06-13 05:41:37.122926
# Unit test for function write_changes
def test_write_changes():
    # import Mocking modules
    from ansible.modules.files.lineinfile import write_changes
    from ansible.module_utils.basic import AnsibleModule
    from unittest.mock import MagicMock, Mock
    module = Mock()
    module.params = {'dest':'/tmp/test'}
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.validate.return_value = True
    module.tmpdir = '/tmp'
    test_content = b'test content'
    write_changes(module,[test_content],'test')
    assert test_content == open('/tmp/test').read()
    os.remove('/tmp/test')




# Generated at 2022-06-13 05:41:47.051000
# Unit test for function present
def test_present():

    import textwrap

# Generated at 2022-06-13 05:41:53.741009
# Unit test for function present
def test_present():
    line_in_file = __file__.replace('/test/lib/ansible/modules/files/', '/lib/ansible/modules/files/') + '.py'
    module = AnsibleModule({'dest': '/tmp/lineinfile-testfile', 'line': '#this is a comment', 'regexp': '^#.+'})
    module.params.update({'path': line_in_file, 'line': '#test line'}),
    present(module, module.params['path'], module.params['regexp'], None, module.params['line'], None, None,
            module.params['create'], module.params['backup'], module.params['backrefs'], module.params['firstmatch'])



# Generated at 2022-06-13 05:42:04.931682
# Unit test for function write_changes
def test_write_changes():
    import sys
    sys.path.append('..')
    # Create test units on disk and in memory

# Generated at 2022-06-13 05:42:16.179555
# Unit test for function present
def test_present():

    dest = '/etc/ansible/test_lineinfile.conf'

    lines = [
        '# Ansible managed: /etc/ansible/test_lineinfile.conf modified on 2017-03-01 01:02:03 by root on testhost.example.com\n',
        '#\n',
        'host=localhost\n',
        '# port=5432\n',
        '\n',
        'foo=bar\n',
        '#\n'
    ]

    # Test 1: Insert the line
    dest1 = dest + '1'
    regexp1 = '^port='
    insertbefore1 = '^#'
    line1 = 'port=5433\n'


# Generated at 2022-06-13 05:42:19.430386
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleAssertionError):
        main()

# Generated at 2022-06-13 05:42:28.691566
# Unit test for function check_file_attrs

# Generated at 2022-06-13 05:42:30.280148
# Unit test for function check_file_attrs

# Generated at 2022-06-13 05:42:40.664036
# Unit test for function main
def test_main():

    # output generated by AnsibleModule.exit_json()
    golden_output = {
        'changed': False,
        'msg': 'file not present',
        'rc': 0,
        'warnings': []
    }

    # Generates the AnsibleModule object

# Generated at 2022-06-13 05:42:52.394085
# Unit test for function write_changes
def test_write_changes():

    import ansible.module_utils.basic
    import ansible.module_utils.action
    import ansible.module_utils.ansible_release
    import ansible.compat.tests.mock as mock
    import os

    module = mock.Mock()

    module.params = {'validate': 'Yay!'}
    module.exit_json = lambda **kwargs: kwargs
    tmpfile = '/tmp/testinfile'
    module.tmpdir = '/tmp/'
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
    b_lines= [b'Testing1\n',b'Testing2\n']

    dest = '/etc/ansible/testinginfile'
