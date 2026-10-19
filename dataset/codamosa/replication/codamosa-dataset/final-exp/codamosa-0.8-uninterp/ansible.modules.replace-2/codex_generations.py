

# Generated at 2022-06-13 05:59:49.444018
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

# Generated at 2022-06-13 05:59:52.442855
# Unit test for function write_changes
def test_write_changes():
  module = AnsibleModule(argument_spec={})
  module.tmpdir = "/tmp"
  path = "/tmp/testfile"
  contents = b"some\ncontents\nto\ncheck"
  write_changes(module, contents, path)

  assert os.stat(path).st_size == len(contents)
  with open(path, 'rb') as f:
    assert f.read() == contents



# Generated at 2022-06-13 06:00:02.731953
# Unit test for function main
def test_main():
  from ansible.modules.files.file import main
  module = AnsibleModule(argument_spec=dict( path=dict(type='path', required=True, aliases=['dest', 'destfile', 'name']), regexp=dict(type='str', required=True), replace=dict(type='str', default=''), after=dict(type='str'), before=dict(type='str'), backup=dict(type='bool', default=False), validate=dict(type='str'), encoding=dict(type='str', default='utf-8'), ),add_file_common_args=True, supports_check_mode=True,)
  main()

# Generated at 2022-06-13 06:00:11.264833
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # setup test
    setattr(AnsibleModule,'check_file_attrs',check_file_attrs)
    setattr(AnsibleModule,'__package__','unit_test')
    setattr(AnsibleModule,'run_command',None)
    setattr(AnsibleModule,'set_file_attributes_if_different',None)
    setattr(AnsibleModule,'load_file_common_arguments',None)
    setattr(AnsibleModule,'module',None)
    setattr(AnsibleModule,'_debug',False)
    setattr(AnsibleModule,'_diff',False)
    setattr(AnsibleModule,'_verbosity',1)
    setattr(AnsibleModule,'_check_mode',False)
    setattr(AnsibleModule,'params',{})
   

# Generated at 2022-06-13 06:00:23.165108
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
            dest=dict(type='path', required=False),
            contents=dict(type='str', required=False),
            backup=dict(type='bool', default=False, required=False),
            validate=dict(type='str', required=False),
            unsafe_writes=dict(type='bool', default=True, required=False),
        )
    )
    contents = to_bytes('hello world')
    path = os.path.join(module.tmpdir, 'hello.txt')
    f = open(path, 'wb')
    f.write(contents)
    f.close()
    write_changes(module, b'hello', path)
    f = open(path, 'rb')


# Generated at 2022-06-13 06:00:27.746832
# Unit test for function main
def test_main():
    import tempfile
    import os.path
    import os
    temp_dir = tempfile.mkdtemp()
    test_file_path = os.path.join(temp_dir, "main_test_file")
    test_file_contents = "old old old"

# Generated at 2022-06-13 06:00:38.336112
# Unit test for function main
def test_main():
  #TODO: use a better test framework than unit test
  import ansible.module_utils.ansible_modlib.replace
  import tempfile
  import uuid
  import os
  import os.path
  import shutil
  tmpdir = tempfile.mkdtemp()

  path = os.path.join(tmpdir, "test-%s" % str(uuid.uuid4()))
  # create a file with original content
  with open(path, "wb") as f:
    f.write(to_bytes('text1\ntext2\ntext3\ntext4\ntext5'))

  # create a module for test

# Generated at 2022-06-13 06:00:50.916834
# Unit test for function main
def test_main():
    contents = '''
c
a
a
b
c
c
'''
    contents2 = '''
c
a
a
b
c
c
'''
    contents3 = '''
c
a
a
b
c
c
'''
    contents4 = '''
c
a
a
b
c
c
'''
    contents5 = '''
c
a
a
b
c
c
'''
    contents6 = '''
c
a
a
b
c
c
'''
    contents7 = '''
c
a
a
b
c
c
'''
    contents8 = '''
c
a
a
b
c
c
'''
    contents9 = '''
c
a
a
b
c
c
'''
    contents

# Generated at 2022-06-13 06:00:51.588823
# Unit test for function check_file_attrs
def test_check_file_attrs():
    pass



# Generated at 2022-06-13 06:01:02.316194
# Unit test for function main
def test_main():

    import os

    # User inputs
    b_path = '/usr/local/bin/'
    b_name = 'myprogram'
    path = os.path.join(b_path, b_name)
    regexp = '#!/usr/bin/python3'
    replace = '#!/usr/bin/python3'

    # Initialize the module

# Generated at 2022-06-13 06:01:25.113437
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class TestMod(AnsibleModule):
        def __init__(self):
            self._ansible_diff = True
            self.params = {}
            self.tmpdir = tempfile.gettempdir()
            self.exit_json = print
            self.fail_json = print

        def atomic_move(self, tmpfile, path, unsafe_writes=None):
            return True

        def load_file_common_arguments(self, params):
            return {'path': '/a/b/c', 'follow': False, 'mode': '0644', 'owner': 'root', 'group': 'root'}

        def set_file_attributes_if_different(self, file_args, changed):
            return False

    mod = TestMod()
    mod.params['follow'] = True
    mod.params['owner']

# Generated at 2022-06-13 06:01:36.777818
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
            unsafe_writes=dict(type='bool', default=False),
        ),
        add_file_common_args=True,
        supports_check_mode=True,
    )

    params = module.params
    path = params['path']

# Generated at 2022-06-13 06:01:43.004259
# Unit test for function main
def test_main():
    test_path = '/tmp/ansible_test'
    path_contents = '''
a
b
c
'''
    test_config = '''
# comment
alice=bob
alpha=beta
'''
    test_file = '''
# comment
alice=bob
1
2
3
alpha=beta
'''

    test_contents = test_file + '\n' + test_config + '\n' + path_contents
    with open(test_path, 'w') as f:
        f.write(test_contents)
    f.close()


# Generated at 2022-06-13 06:01:50.056998
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # purpose: verify that check_file_attrs is returning the expected values
    module = type('AnsibleModule', (object,), {})
    module.params = {}
    module.params['file_permission'] = None
    module.params['file_owner'] = None
    module.params['file_group'] = None
    module.params['follow'] = False
    module.params['backup'] = False
    module.params['unsafe_writes'] = False

    module.fail_json = lambda x: None
    module.atomic_move = lambda x, y, z: None
    module.set_file_attributes_if_different = lambda x, y: (True)
    module.load_file_common_arguments = lambda x: []


# Generated at 2022-06-13 06:01:59.484894
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
        ),
    )

    params = module.params
    path = params['path']
    res_args = dict()

    params['after'] = to_text(params['after'], errors='surrogate_or_strict', nonstring='passthru')

# Generated at 2022-06-13 06:02:07.187924
# Unit test for function write_changes
def test_write_changes():
    """Function to unit test write changes"""
    test_path = '/tmp/unit_test'
    test_contents = 'This is a unit test!\nLine 2\nLine 3'
    module = AnsibleModule({'path': test_path, 'validate': None}, check_invalid_arguments=False)
    test_object = write_changes(module, test_contents, test_path)

    assert not test_object



# Generated at 2022-06-13 06:02:14.599470
# Unit test for function check_file_attrs

# Generated at 2022-06-13 06:02:28.686333
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


# Generated at 2022-06-13 06:02:35.781065
# Unit test for function main
def test_main():
    import os
    import sys
    import pytest
    class AnsibleExitJson(Exception):
        pass
    class AnsibleFailJson(Exception):
        pass
    def exit_json(*args, **kwargs):
        if 'changed' not in kwargs:
            kwargs['changed'] = False
        raise AnsibleExitJson(kwargs)
    def fail_json(*args, **kwargs):
        kwargs['failed'] = True
        raise AnsibleFailJson(kwargs)
    class AnsibleModule(object):
        def __init__(self, *args, **kwargs):
            self.params = kwargs
            self.params['_ansible_diff'] = False
            self.params['_ansible_verbosity'] = 0
            self.tmpdir = 'tmp'

# Generated at 2022-06-13 06:02:47.491304
# Unit test for function write_changes
def test_write_changes():
    # We will simulate success by placing the contents in a temporary file
    # and returning from the function.
    tmpfd, tmpfile = tempfile.mkstemp(dir='/tmp')
    f = os.fdopen(tmpfd, 'wb')
    f.write('')
    f.close()
    module = None
    try:
        import ansible.modules.testing.atomic_move
        class module:
            params = { 'unsafe_writes': False }
            tmpdir = '/tmp'
        def atomic_move(self, src, dest):
            assert '/tmp/' in src
            assert dest == '/foo/bar'
        module.atomic_move = atomic_move
    except:
        pass
    assert write_changes(module, '', '/foo/bar') is True


# Generated at 2022-06-13 06:03:19.818611
# Unit test for function write_changes
def test_write_changes():
    import tempfile
    write_changes(
        AnsibleModule({
            'REPLACEMENT_FILE': tempfile.mktemp(prefix='ansible-test-replace-', suffix='.tmp'),
            'REPLACEMENT_TMP_FILE': tempfile.mktemp(prefix='ansible-test-replace-', suffix='.tmp'),
            'REPLACEMENT_LONG_FILE': tempfile.mktemp(prefix='ansible-test-replace-', suffix='.tmp'),
        }),
        b'first line\nsecond line\nthird line\n',
        '/non/existent/file.txt'
    )
    return read_file('/non/existent/file.txt') == b'first line\nsecond line\nthird line\n'



# Generated at 2022-06-13 06:03:31.089760
# Unit test for function check_file_attrs

# Generated at 2022-06-13 06:03:43.517985
# Unit test for function write_changes
def test_write_changes():
    contents = 'foo'
    path = '/test/test'
    validate = 'foo'
    tmpfile = '/tmp/test'
    module_name = 'test'

    class Test:
        def __init__(self):
            self.params = {}
            self.tmpdir = '/tmp'

        def get(self, arg, none):
            return self.params.get(arg, none)

        def fail_json(self, msg):
            return msg

        def run_command(self, cmd):
            return 0, cmd

        def atomic_move(self, src, dest, unsafe_writes=True):
            return dest

    module = Test()
    module.params['validate'] = validate
    assert write_changes(module, contents, path) == path





# Generated at 2022-06-13 06:03:53.265998
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    module.params['unsafe_writes'] = True
    module.params['path'] = '/tmp/file'
    module.params['owner'] = 'root'
    module.params['group'] = 'root'
    module.params['mode'] = '0644'
    module.params['seuser'] = 'seuser'
    module.params['serole'] = 'serole'
    module.params['setype'] = 'setype'
    module.params['selevel'] = 'selevel'

    # Test 1
    message = "File not found"
    changed = True
    msg, changed = check_file_attrs(module, changed, message)
    assert msg == "File not found", "msg should be File not found"


# Generated at 2022-06-13 06:04:04.475617
# Unit test for function check_file_attrs
def test_check_file_attrs():
    """Function check_file_attrs unit test"""

# Generated at 2022-06-13 06:04:11.490615
# Unit test for function write_changes
def test_write_changes():
    import base64
    from ansible.module_utils.six import BytesIO

    test_module = AnsibleModule(argument_spec={
        'path':{'required':True},
        'validate':{'required':False},
        'unsafe_writes':{'required':False}
    })

    fd, tmpfile = tempfile.mkstemp(dir=os.path.dirname(__file__))
    f = os.fdopen(fd, 'w')
    f.write('foo')
    f.close()

    test_module.params['path'] = tmpfile

    test_module.params['validate'] = None
    test_module.params['unsafe_writes'] = False

    write_changes(test_module, b'foo', None)

# Generated at 2022-06-13 06:04:23.232577
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

# Generated at 2022-06-13 06:04:24.583690
# Unit test for function main

# Generated at 2022-06-13 06:04:33.206943
# Unit test for function write_changes
def test_write_changes():
    from ansible.module_utils._text import to_bytes
    temp_path = tempfile.mkstemp()[1]
    module = AnsibleModule({'validate': None}, check_invalid_arguments=False)
    module.run_command = lambda *args, **kwargs: (0, '', '')
    test_contents = b"this is a test"
    write_changes(module, test_contents, temp_path)
    with open(temp_path, 'rb') as f:
        assert f.read() == test_contents
    os.remove(temp_path)

# =================================================================================


# Generated at 2022-06-13 06:04:40.074847
# Unit test for function main
def test_main():
    class args:
        path = 'test_ec2_group_facts.py'
        regexp = 's/old/new'
        replace = 's/old/new'
        backup = 's/old/new'
        after = 's/old/new'
        before = 's/old/new'
        validate = 's/old/new'
        encoding = 's/old/new'
        check_mode = 's/old/new'
        diff = 's/old/new'
    b = main(args)
    assert b


# Generated at 2022-06-13 06:05:38.778826
# Unit test for function write_changes
def test_write_changes():
    fake_module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True),
            regexp=dict(required=True),
            replace=dict(required=True),
            diff_mode=dict(type='bool', default=False, required=False),
            safe_file_operations=dict(type='bool', default=True, required=False),
            backup=dict(type='bool', default=False, required=False),
            before=dict(required=False),
            after=dict(required=False),
            validate=dict(required=False)
        )
    )
    fake_module.tmpdir = "tmp"
    fake_module.params['path'] = 'hello'
    fake_module.params['replace'] = 'world'
    tmpfd, tmpfile = tempfile.mkstemp

# Generated at 2022-06-13 06:05:41.072329
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # TODO: Rewrite this unit test
    pass



# Generated at 2022-06-13 06:05:42.077763
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 06:05:52.840777
# Unit test for function main
def test_main():
    from ansible_collections.misc.tests.unit.modules.utils import AnsibleExitJson, AnsibleFailJson, ModuleTestCase, set_module_args
    ansible_env = {'_ansible_check_mode': False, '_ansible_remote_tmp': None, '_ansible_tmpdir': 'tmp', '_ansible_keep_remote_files': False}

# Generated at 2022-06-13 06:06:00.001872
# Unit test for function write_changes
def test_write_changes():
    '''
    Unit test for function write_changes
    '''
    module = AnsibleModule(argument_spec={
        'path': {'required': True},
        'unsafe_writes': {'type': 'bool', 'default': False},
    })

    tempfile_name = ''

# Generated at 2022-06-13 06:06:10.126080
# Unit test for function main
def test_main():

    # test 1
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

    params

# Generated at 2022-06-13 06:06:22.150766
# Unit test for function check_file_attrs

# Generated at 2022-06-13 06:06:26.665074
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs(None, False, '') == ('ownership, perms or SE linux context changed', True)
    assert check_file_attrs(None, True, '') == (' and ownership, perms or SE linux context changed', True)



# Generated at 2022-06-13 06:06:27.223761
# Unit test for function write_changes
def test_write_changes():
    pass



# Generated at 2022-06-13 06:06:31.056882
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({'validate': None, 'path': 'fake_path'})
    contents = 'the contents'
    fake_file = 'fake_file'
    write_changes(module, contents, fake_file)

    with open(fake_file, 'r') as f:
        assert f.read() == 'the contents'
    os.remove(fake_file)



# Generated at 2022-06-13 06:08:45.653428
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
            contents=dict(type='str')
        )
    )
    tmpfd, path = tempfile.mkstemp(dir=module.tmpdir)
    os.close(tmpfd)
    contents = b'file contents'
    write_changes(module, contents, path)
    with open(path, 'rb') as f:
        assert f.read() == contents
    os.unlink(path)


# Generated at 2022-06-13 06:08:55.571218
# Unit test for function write_changes
def test_write_changes():
    from ansible.module_utils import basic
    import shutil
    import tempfile
    import os

    tmpdir = tempfile.mkdtemp()
    fd, path1 = tempfile.mkstemp(dir=tmpdir)
    f = os.fdopen(fd, 'wb')
    s = b'hi'
    f.write(s)
    f.close()
    fd, path2 = tempfile.mkstemp(dir=tmpdir)
    f = os.fdopen(fd, 'wb')
    s = b'hey'
    f.write(s)
    f.close()
    m = basic.AnsibleModule(
        argument_spec = dict(
        ),
        supports_check_mode=True
    )
    m.tmpdir = tmpdir

# Generated at 2022-06-13 06:09:06.304887
# Unit test for function write_changes
def test_write_changes():
    """Test write_changes module function.

    This test will test whether the content matches the
    expected output by validating the file contents.

    """
    tmp_path = os.path.join(mkdtemp(), "create")
    tmp_file = os.path.join(tmp_path, "file")
    os.makedirs(tmp_path)
    module = DummyModule(tmp_file, "w")
    contents = '# this line stays\n'
    contents += '# this line too\n'
    contents += 'this line is removed'
    contents += '# and this line too'
    write_changes(module, contents, tmp_file)
    assert module.b_path == to_bytes(tmp_file)
    assert module.b_args == to_bytes(contents)



# Generated at 2022-06-13 06:09:15.684847
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={'path': dict(required=True), 'unsafe_writes': dict(type='bool', default=False)})
    contents = to_bytes("test\n")
    tmpdir = '/tmp'
    module.tmpdir = tmpdir
    tmpfile = to_text(os.path.join(tmpdir, 'test_file'))
    path = tmpfile
    write_changes(module, contents, path)
    assert os.path.exists(tmpfile)
    assert os.path.getsize(tmpfile) == 5



# Generated at 2022-06-13 06:09:20.728665
# Unit test for function main
def test_main():
    pass

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.splitter import *

if __name__ == '__main__':
    main()