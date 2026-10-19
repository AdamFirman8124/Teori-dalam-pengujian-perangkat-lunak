

# Generated at 2022-06-13 05:59:42.264414
# Unit test for function write_changes
def test_write_changes():
  assert len("foo") == 3



# Generated at 2022-06-13 05:59:46.024633
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    changed, message = check_file_attrs(module, False, "Something changed")
    assert changed
    assert message == "Something changed and ownership, perms or SE linux context changed"



# Generated at 2022-06-13 05:59:54.333036
# Unit test for function main
def test_main():
    import ansible.module_utils.ansible_release
    if not ansible.module_utils.ansible_release.__version__.startswith('2.4'):
        print("Skipping test for ansible < 2.4")
        return
    import ansible.modules.file.replace
    contents = "#test file\nreplace me\n"
    regexp = "replace me"
    replace = "I've been replaced"
    after = "#test file\n"
    before = ""
    params = {"path": "/tmp/file", "regexp": regexp, "replace": replace, "after": after, "before": before, "backup": "", "validate": "", "encoding": "", "follow": "", "unsafe_writes": ""}

# Generated at 2022-06-13 06:00:06.057130
# Unit test for function main
def test_main():
  import os
  import tempfile
  import shutil
  import filecmp

  def create_file(path, content):
    fp = open(path, 'w')
    fp.write(content)
    fp.close()

  def compare_files(path1, path2):
    return filecmp.cmp(path1, path2)
  
  test_dir = tempfile.mkdtemp()
  test_file_a = os.path.join(test_dir, 'test_a')
  create_file(test_file_a, 'abc def\nabc def\nabc def\nabc def\n')
  main()
  shutil.rmtree(test_dir)

if __name__ == '__main__':
  test_main()

# Generated at 2022-06-13 06:00:11.484234
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import mock
    import tempfile
    import os
    import json

    mock_check_mode = mock.Mock()
    mock_check_mode.check_mode = False

    test_path = os.path.join(os.path.dirname(__file__), 'test.py')

# Generated at 2022-06-13 06:00:15.649566
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

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


# Generated at 2022-06-13 06:00:25.565184
# Unit test for function write_changes
def test_write_changes():
    # Mock needed function
    def mock_run_command(cmd):
      return (0, "", "")
    def mock_atomic_move(src, dest, unsafe_writes=False):
      return True
    def mock_fail_json(msg=""):
      return True

    # Mock AnsibleModule
    class MockModule(AnsibleModule):
      run_command = mock_run_command
      atomic_move = mock_atomic_move
      fail_json = mock_fail_json
    tmp=tempfile.mkstemp()[1]
    module = MockModule(tmpdir=tempfile.gettempdir(), params={"path": tmp, "validate": None})
    module.tmpdir = module.tmpdir
    # Test write_changes
    assert write_changes(module, "test", tmp)



# Generated at 2022-06-13 06:00:32.948368
# Unit test for function main
def test_main():
    args = dict(
        path="/home/jdoe/.ssh/known_hosts",
        regexp="old\.host\.name[^\n]*\n",
        replace="",
        backup=False,
        validate="/usr/sbin/apache2ctl -f %s -t",
        encoding="utf-8",
        unsafe_writes=False
    )
    module = AnsibleModule(**args)
    main()


# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:00:42.158807
# Unit test for function main
def test_main():
    '''
    Unit testing basic functionality:
    Re-format IP addresses in /etc/hosts
    '''

    path = '/home/matt/ansible-testing/ansible/test/'
    regexp = r'\b(192\.168\.[0-9]+\.[0-9]+)\b'
    replace = r'\1.255'
    after = ''
    before = ''
    pattern = u''
    section = ''
    result = ''
    mre = ''
    tmpfd = ''
    tmpfile = ''
    f = ''
    section = ''
    sections = ''
    validate = ''
    valid = ''
    file_args = ''
    module = ''
    module.fail_json = ''
    module.run_command = ''
    module.atomic_move = ''
    main()

# Generated at 2022-06-13 06:00:43.581046
# Unit test for function write_changes
def test_write_changes():
  pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:01:04.523374
# Unit test for function main
def test_main():
    path = "/etc/hosts"
    regexp = r"(\s+)old\.host\.name(\s+.*)?$"
    replace = r"\1new.host.name\2"
    backup = False
    validate = None
    encoding = "utf-8"


# Generated at 2022-06-13 06:01:09.829048
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({})
    contents = to_bytes('12345')
    path = os.path.join(tempfile.gettempdir(), 'test.file')
    with open(path, 'wb') as f:
        f.write(contents)
    module.params = {
        'validate': None,
        'unsafe_writes': True,
    }
    module.tmpdir = tempfile.gettempdir()
    write_changes(module, to_bytes('54321'), path)
    with open(path, 'rb') as f:
        assert f.read() == to_bytes('54321')



# Generated at 2022-06-13 06:01:15.452399
# Unit test for function main
def test_main():

    import unittest
    import tempfile
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import os

    class AnsibleExitJson(Exception):
        pass

    class AnsibleFailJson(Exception):
        pass

    class ModuleTestCase(unittest.TestCase):

        def exec_module(self, *args, **kwargs):

            self.run_method = lambda name, *args, **kwargs: self._exec_module(name, *args, **kwargs)


# Generated at 2022-06-13 06:01:24.748053
# Unit test for function main
def test_main():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule

    ansible_input_file = 'test_main.input'
    contents = '''# This is a comment
    ListenAddress 192.168.1.1
    ListenAddress 192.168.1.2
    ListenAddress 192.168.1.3
    '''
    with open(ansible_input_file, 'wb') as f:
        f.write(to_bytes(contents))


# Generated at 2022-06-13 06:01:36.433774
# Unit test for function check_file_attrs
def test_check_file_attrs():
    m_module = AnsibleModule(argument_spec={})
    m_module.params = {
        'path': '/etc/hosts',
        'owner': 'jdoe',
        'group': 'jdoe',
        'mode': '0644',
        'unsafe_writes': True
    }
    m_module.file_common_argument_spec = {
        'path': m_module.params['path'],
    }
    os_path_exists = m_module.file_common_argument_spec['path']

    if os_path_exists:
        file_args = module.load_file_common_arguments(module.params)
        if module.set_file_attributes_if_different(file_args, False):
            changed = True

# Generated at 2022-06-13 06:01:41.730208
# Unit test for function write_changes
def test_write_changes():
    test_module = AnsibleModule({'debug': False})
    test_module.tmpdir = '/tmp'
    test_module.atomic_move = lambda src, dst: os.rename(src, dst)
    test_module.params['validate'] = None
    test_module.params['unsafe_writes'] = True
    write_changes(test_module, b'foo', os.path.join(test_module.tmpdir, 'test_write_changes'))



# Generated at 2022-06-13 06:01:48.905224
# Unit test for function write_changes
def test_write_changes():
  # This is a hack which just creates a fake module object since the original object is not pickleable
  module = AnsibleModule({'path':'/tmp/foo.txt', 'validate':'/usr/bin/true', 'unsafe_writes':True, 'tmpdir':'/tmp/'}, '', True, '', False)
  existing_file = 'foo bar'
  changed_file = 'foo baz'
  # This function is only used by the replace module, but AnsibleModule is a generic object
  write_changes(module, changed_file, '/tmp/foo.txt')
  with open('/tmp/foo.txt', 'r') as f:
    assert f.read() == 'foo baz'



# Generated at 2022-06-13 06:01:59.101732
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # Basic data
    changed = False
    message = "Testing"

    # Mock argparse
    class MockArgs():
        def __init__(self):
            self.path = "testpath"
            self.unsafe_writes = True

    module = MockArgs()

    # Mock os.stat
    old_stat = os.stat
    class MockStat():
        def __init__(self):
            self.st_mode = 0o777
            self.st_mtime = 0
    os.stat = MockStat

    # Mock os.lstat
    old_lstat = os.lstat
    class MockLStat():
        def __init__(self):
            self.st_mode = 0o777
            self.st_mtime = 0
            self.st_uid = 0

# Generated at 2022-06-13 06:02:11.746643
# Unit test for function write_changes
def test_write_changes():
    from ansible.compat.tests.mock import MagicMock, patch
    from ansible.module_utils import basic
    from ansible.module_utils.common._collections_compat import MutableMapping
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import StringIO
    import socket
    import ssl

    if not hasattr(ssl, 'SSLContext'):
        ssl_context_mock = None
    else:
        ssl_context_mock = MagicMock()
        ssl_context_mock.check_hostname = False
    ssl_mock = MagicMock()
    ssl_mock.SSLContext = ssl_context_mock
    socket_mock = MagicMock()
    open_m

# Generated at 2022-06-13 06:02:22.843511
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={'path': {'type': 'str'}})
    module.run_command = lambda cmd: (0, '', '')
    path = os.path.abspath(module.params['path'])
    # The first run will create the file, the second run will check for idempotency
    for _ in range(2):
        write_changes(module, to_bytes(u'data'), path)
        with open(path) as f:
            data = f.read()
        assert to_text(data) == 'data'
        os.unlink(path)



# Generated at 2022-06-13 06:02:57.471001
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    module_mock = basic.AnsibleModule(
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


# Generated at 2022-06-13 06:03:02.930196
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
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
    original_path = '''asdf
    asdf
    asdfas
    '''

# Generated at 2022-06-13 06:03:09.375015
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path'),
            unsafe_writes=dict(type='bool', default=False),
            validate=dict(default=None)
        )
    )
    dest = '/tmp/testfile'
    contents = b'hello world\n'
    # write file
    write_changes(module, contents, dest)
    # read file
    f = open(dest, 'rb')
    f_contents = f.read()
    f.close()
    # assert it's still correct
    assert f_contents == contents
    # cleanup file
    os.remove(dest)



# Generated at 2022-06-13 06:03:19.561034
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
            argument_spec = dict(
                path = dict(required=True, type='path'),
                after = dict(required=False),
                before = dict(required=False),
                backup = dict(type='bool',default=False),
                owner = dict(type='str'),
                group = dict(type='str'),
                mode = dict(required=False),
                seuser = dict(required=False),
                serole = dict(required=False),
                selevel = dict(required=False),
                setype = dict(required=False),
                unsafe_writes = dict(default=False, type='bool')
                ),
            )

    old_file_args = module.load_file_common_arguments(module.params)

# Generated at 2022-06-13 06:03:23.554209
# Unit test for function main
def test_main():
    try:
        import runpy
        runpy.run_module(
            'ansible.modules.files.replace',
            run_name='__main__',
            alter_sys=True
        )
    except SystemExit as e:
        assert not e.code


# Generated at 2022-06-13 06:03:25.649258
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.compat.tests import unittest
    unittest.TestCase(check_file_attrs)


# Generated at 2022-06-13 06:03:29.652858
# Unit test for function write_changes
def test_write_changes():
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
    f = os.fdopen(tmpfd, 'wb')
    f.write(contents)
    f.close()


# Generated at 2022-06-13 06:03:41.870018
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from tempfile import TemporaryFile

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
    encoding = params['encoding']

# Generated at 2022-06-13 06:03:50.264772
# Unit test for function main
def test_main():
    # Test with no parametes
    args = dict()
    actual = dict()
    expected = dict()
    try:
        main(args)
    except SystemExit as e:
        actual['failed'] = False
        actual['msg'] = None
        expected['failed'] = False
        expected['msg'] = None
        assert actual == expected

    # Test with valid parameters
    args = dict(
        path="path",
        regexp=1,
        replace='',
        after='',
        before=''
        )
    actual = dict()
    expected = dict()
    try:
        main(args)
    except SystemExit as e:
        actual['failed'] = False
        actual['msg'] = None
        expected['failed'] = False
        expected['msg'] = None
        assert actual == expected


# Unit test

# Generated at 2022-06-13 06:04:02.388037
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
    # match without check file attrs
    message = 'regexp pattern replaced'
    changed = False
    msg, changed = check_file_attrs(module, changed, message)
    assert msg == message
   

# Generated at 2022-06-13 06:04:58.534346
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({},{})
    module.params = {'backup': False,
        'content': '',
        'force': True,
        'group': '',
        'local_follow': True,
        'mode': '0644',
        'owner': 'not_used',
        'path': None,
        'selevel': '',
        'serole': '',
        'setype': '',
        'seuser': '',
        'unsafe_writes': False,
        'validate': None,}
    module.exists = lambda x: True
    module.atomic_move = lambda x,y,z: True
    module.fail_json = lambda x: True
    module.run_command = lambda x: (0,'','')
    tmpfile = "12345"
    contents

# Generated at 2022-06-13 06:05:06.310994
# Unit test for function main
def test_main():
  from ansible.module_utils import basic
  from ansible.module_utils._text import to_bytes
  from ansible.module_utils._text import to_text

  tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
  f = os.fdopen(tmpfd, 'wb')
  f.write(contents)
  f.close()

  validate = module.params.get('validate', None)
  valid = not validate
  if validate:
    if "%s" not in validate:
      module.fail_json(msg="validate must contain %%s: %s" % (validate))
    (rc, out, err) = module.run_command(validate % tmpfile)
    valid = rc == 0

# Generated at 2022-06-13 06:05:16.365784
# Unit test for function write_changes

# Generated at 2022-06-13 06:05:26.535275
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class FakeModule:
        params = {
            'path': None,
            'unsafe_writes': None,
        }
        def set_file_attributes_if_different(self, file_args, changed):
            return True
        def fail_json(self, msg):
            pass
        def load_file_common_arguments(self, params):
            return params
    changed = False
    fm = FakeModule()
    msg, changed = check_file_attrs(fm, changed, "")
    assert changed
    msg, changed = check_file_attrs(fm, changed, msg)
    assert changed
    msg, changed = check_file_attrs(fm, changed, "Message...")
    assert changed


# Generated at 2022-06-13 06:05:28.178808
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert True



# Generated at 2022-06-13 06:05:29.484316
# Unit test for function main
def test_main():
    assert True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:05:37.883674
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
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
        add_file_common_args=True,
        supports_check_mode=True,
    )

    params = module.params
    path = params['path']
    encoding = params['encoding']
   

# Generated at 2022-06-13 06:05:49.984430
# Unit test for function main
def test_main():
    test_args = {
        'backup': False,
        'encoding': 'utf-8',
        'path': 'ansible/test/test_replace.txt',
        'replace': 'test.test2.test3',
        'regexp': '\\b(localhost)(\\d*).*',
    }
    test_path = os.path.realpath(__file__)
    test_dir = os.path.dirname(test_path)
    test_file_path = os.path.join(test_dir, test_args['path'])
    test_backup_file_path = os.path.join(test_dir, 'ansible/test/test_replace.txt.2019-01-19@09:27~')


# Generated at 2022-06-13 06:05:54.604199
# Unit test for function main
def test_main():

    #### Main
    # set defaults
    path = 'testFile'
    contents = 'a string'
    regexp = 'This string exists\nand is on two lines'
    replace = 'This string has been replaced\nwith this one'
    validate = 'cat %s'
    encoding = 'utf-8'
    after = None
    before = None
    backup = False
    diff = False
    changed = True

    class fakeModule(object):
        def __init__(self, changed, backup, diff, path):
            self.changed = changed
            self.backup_local = backup
            self.params = {
                'backup': False,
                'diff': diff,
                'path': path,
            }
            self.check_mode = False
    module = fakeModule(changed, backup, diff, path)

# Generated at 2022-06-13 06:06:03.124984
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({'dest': '/path/to/testfile', 'unsafe_writes': False, 'validate': None}, check_invalid_arguments=False)
    def run_command(command, no_log=False):
        if command.endswith(('somescript', '/path/to/testfile')):
            return (0, 'success', '')
        elif command.endswith(('failscript', '/path/to/testfile')):
            return (1, 'failure', '')
        else:
            assert False
    module.run_command = run_command

# Generated at 2022-06-13 06:08:09.423055
# Unit test for function check_file_attrs
def test_check_file_attrs():
    import ansible.module_utils.basic as basic
    test_basic = basic.AnsibleModule(
        argument_spec=dict(
            src=dict(required=True, type='str'),
            dest=dict(required=True, type='str'),
        )
    )
    test_basic.atomic_move = lambda x, y, z=None: None
    test_basic.set_file_attributes_if_different = lambda x, y: True
    test_basic.params = dict(
        src='/tmp/src',
        dest='/tmp/dest',
        owner=None,
        group='group',
        mode=None,
        seuser=None,
        serole=None,
        selevel=None,
        setype=None,
    )
    test_basic.load_file_common_

# Generated at 2022-06-13 06:08:21.846026
# Unit test for function main
def test_main():

    file_p = tempfile.NamedTemporaryFile()
    file_p.write(b"#\n")
    file_p.write(b"# This is an example of a file\n")
    file_p.write(b"#\n")
    file_p.write(b"# A few things to notice\n")
    file_p.write(b"#\n")
    file_p.flush()

    if file_p is None:
        print("Failed to create temporary file to test function main")


# Generated at 2022-06-13 06:08:35.135283
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # mocks
    class MockModule:
        def __init__(self, **kwargs):
            self.params = kwargs
            self.set_file_attributes_if_different_data = True
            self.set_file_attributes_if_different_changed = False

        def set_file_attributes_if_different(self, data, changed):
            self.set_file_attributes_if_different_data = data
            self.set_file_attributes_if_different_changed = changed

        def load_file_common_arguments(self, params):
            return params


# Generated at 2022-06-13 06:08:45.745745
# Unit test for function check_file_attrs

# Generated at 2022-06-13 06:08:47.795577
# Unit test for function write_changes
def test_write_changes():
    """
    Unit test for function write_changes
    """


# Generated at 2022-06-13 06:08:57.096846
# Unit test for function main
def test_main():
  from ansible.module_utils import basic
  import sys
  import shutil
  from ansible.module_utils._text import to_bytes
  from ansible.module_utils.basic import AnsibleModule
  from ansible.modules.files.replace import to_text
  from ansible.modules.files.replace import check_file_attrs
  from ansible.modules.files.replace import write_changes
  import os
  import re

  path = sys.argv[1]
  backup = True
  encoding = 'utf-8'
  replace = 'march'
  regexp = 'january|february|april'
  module_args = dict(path=path, backup=backup, encoding=encoding, replace=replace, regexp=regexp)

# Generated at 2022-06-13 06:09:06.503419
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={
        'path': {'required': True, 'type': 'path'},
        'tmpdir': {'default': '/tmp'},
        'validate': {'type': 'str', 'default': None}
    })

    contents = to_text(b'123')
    path = '/tmp/test_write_changes'
    # Replace a non-existing file
    try:
        os.remove(path)
    except OSError:
        # File doesn't exist
        pass
    write_changes(module, contents, path)
    assert filecmp.cmp(os.path.abspath(path), os.path.abspath('/tmp/test_write_changes'))

    # Replace an existing file
    contents_new = to_text(b'456')
   

# Generated at 2022-06-13 06:09:10.774596
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs(None, True, "test") == ("test and ownership, perms or SE linux context changed", True)


# Generated at 2022-06-13 06:09:11.570823
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:09:15.656292
# Unit test for function main
def test_main():
    locale = { 
        'path': '/etc/ansible/ansible.cfg',
        'regexp': '\\b(localhost)(\\d*)\\b', 
        'replace': '\\1\\2.localdomain\\2 \\1\\2',
        'unsafe_writes': False, 
        'follow': False, 
        'backup': False,
        'dest': '/etc/ansible/ansible.cfg',
        'destfile': '/etc/ansible/ansible.cfg',
        'name': '/etc/ansible/ansible.cfg',
        'encoding': 'utf-8'
    }
    assert main(locale)