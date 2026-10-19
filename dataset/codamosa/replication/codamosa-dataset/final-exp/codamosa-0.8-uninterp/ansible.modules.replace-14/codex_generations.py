

# Generated at 2022-06-13 05:59:51.525319
# Unit test for function write_changes
def test_write_changes():
    fixture='/opt/stack-install/new/ansible-stable/test/unit/modules/files/fixtures/replace'
    module = AnsibleModule(
        argument_spec = dict(
            _ansible_tmpdir={'type': 'str'},
            _ansible_remote_tmp={'type': 'str'},
            _ansible_keep_remote_files={'type': 'bool'},
            validate={'type': 'str'},
        ),
    )
    module.tmpdir='/tmp'
    module.run_command=test_run_command
    try:
      module.atomic_move=test_atomic_move
    except:
      pass
    path='%s/test_write_changes' % module.tmpdir
    write_changes(module, '' , path)

# Generated at 2022-06-13 05:59:58.482599
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # This is hacky and there is probably a better way
    class FakeModule:
        def __init__(self):
            self.params = {}
        def run_command(self, arg):
            return True
        def atomic_move(self, arg1, arg2, arg3):
            return True
        def set_file_attributes_if_different(self, arg1, arg2):
            return True

    fm = FakeModule()
    assert check_file_attrs(fm, False, "Hello") == ("Hello and ownership, perms or SE linux context changed", True)
    assert check_file_attrs(fm, True, "Hello") == ("Hello and ownership, perms or SE linux context changed", True)



# Generated at 2022-06-13 06:00:08.439044
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
            unsafe_writes=dict(type='bool', default=True),
            validate=dict(type='str', default=None),
        ),
        supports_check_mode=False
    )

    path = 'new.txt'
    contents = 'test'
    with open(path, 'wb') as f:
        f.write(contents)

    assert os.path.isfile(path) == True

    write_changes(module, contents, path)
    with open(path, 'rb') as f:
        assert f.read() == contents

    os.unlink(path)
    assert os.path.isfile(path) == False



# Generated at 2022-06-13 06:00:09.016074
# Unit test for function write_changes
def test_write_changes():
    pass



# Generated at 2022-06-13 06:00:17.381383
# Unit test for function write_changes
def test_write_changes():
    class ActionModuleArgs(object):
        def __init__(self):
            self.fail_json = lambda: None
            self.run_command = lambda: (0, '', '')
            self.tmpdir = '/tmp'
            self.params = dict(validate=None, unsafe_writes=False)
        def atomic_move(self, foo, bar, unsafe_writes=False):
            pass

    module = ActionModuleArgs()
    import ansible.module_utils.basic
    old_atomic_move = ansible.module_utils.basic.atomic_move
    ansible.module_utils.basic.atomic_move = lambda source, dest: None
    ansible.module_utils.basic.file = lambda *args, **kwargs: None

# Generated at 2022-06-13 06:00:23.280353
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec=dict(
            src=dict(type='str'),
            dest=dict(type='str'),
            validate=dict(type='str')
        ),
    )
    file_path = '/tmp/test_file'
    contents = 'Test Contents'
    write_changes(module, contents, file_path)
    with open(file_path, 'r') as f:
        assert f.read() == contents


# Generated at 2022-06-13 06:00:29.245573
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.params = dict()
    module.params['unsafe_writes'] = False
    module.params['backup'] = False

    class Attr:
        def __init__(self):
            self.value = False

        def __bool__(self):
            return self.value

    changed = Attr()
    message = ''
    check_file_attrs(module, changed, message)
    assert not changed



# Generated at 2022-06-13 06:00:39.445162
# Unit test for function main
def test_main():
    from ansible.modules.system.replace import *
    file_args = {'path':'/tmp/test_main','backup':'yes','validate':'vali','unsafe_writes':'False'}

# Generated at 2022-06-13 06:00:43.810647
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={'path': {'type': 'str'} })
    changed = False
    message = "Foo"
    try:
        check_file_attrs(module, changed, message)
    except SystemExit:
        pass



# Generated at 2022-06-13 06:00:50.636842
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = mock.MagicMock()
    module.params = {'owner': 'root', 'group': 'nobody', 'mode': '0644'}
    module.set_file_attributes_if_different.return_value = True
    check_file_attrs(module, True, "changed")
    check_file_attrs(module, False, "")


# Generated at 2022-06-13 06:01:11.915240
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({
            "path": "/path/to/file",
            "owner": "alice",
            "group": "alice",
            "mode": "0777",
            "seuser": "alice_r",
            "serole": "object_r",
            "setype": "bin_t",
            "selevel": "s0",
            "unsafe_writes": True})
    class TestModule:
        def __init__(self, p):
            self.params = p
            self.atomic_move = lambda src, dest: None
            self.set_file_attributes_if_different = lambda file_args, changed: True
            self.load_file_common_arguments = lambda file_args: None

# Generated at 2022-06-13 06:01:13.843850
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs(None, True, "") == (" and ownership, perms or SE linux context changed", True)



# Generated at 2022-06-13 06:01:14.691380
# Unit test for function write_changes
def test_write_changes():
    assert True
    # module.fail_json(msg='myfail')


# Generated at 2022-06-13 06:01:16.919385
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs('module', True, 'message') == ('message and ownership, perms or SE linux context changed', True)


# Generated at 2022-06-13 06:01:25.857256
# Unit test for function main
def test_main():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.ansible_release
    import contextlib
    import os
    import re
    import sys
    import tempfile
    import shutil
    import copy

    module_args = {}
    module_args.update(
        dict(
            path = os.getcwd(),
            regexp = '^(.+)$',
            replace = '# \1'
        )
    )
    module_args.update(dict(dest=module_args['path']))
    module_args.update(dict(destfile=module_args['path']))

# Generated at 2022-06-13 06:01:37.762936
# Unit test for function write_changes
def test_write_changes():
    replace_module = '''
- name: replace
  ansible.builtin.replace:
    path: /etc/hosts
    backup: yes
    regexp: '\\b(localhost)(\\d*)\\b'
    replace: '\\1\\2.localdomain\\2 \\1\\2'

- name: replace before and after
  ansible.builtin.replace:
    path: /etc/hosts
    backup: yes
    regexp: '\\b(localhost)(\\d*)\\b'
    replace: '\\1\\2.localdomain\\2 \\1\\2'
    after: '<VirtualHost [*]>'
    before: '</VirtualHost>'
    '''
    module = AnsibleModule(replace_module, {'backup': True})

# Generated at 2022-06-13 06:01:39.399457
# Unit test for function write_changes
def test_write_changes():
    assert False


# Generated at 2022-06-13 06:01:48.319091
# Unit test for function write_changes
def test_write_changes():

    #test_replace_file corresponds to test_replace_file in test_action_basic.py
    class test_replace_file_AnsibleModule():
        def __init__(self):
            self.params = {}
            self.check_mode = True
            self.exit_json = lambda c, m: print(c)

    class test_replace_file_FileModule():
        def __init__(self):
            self.params = {}
            self.atomic_move = lambda s, d, uw: print("atomic_move: source:%s destination:%s unsafe_writes:%s" % (s, d, uw))
            self.run_command = lambda s: print("run_command: %s" % s)
            self.fail_json = lambda c, m: print(c)


# Generated at 2022-06-13 06:01:55.979636
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={})
    module.params = {'path': '/path/not/exist', 'owner': 'root', 'group': 'root', 'mode': '644'}
    module.set_file_attributes_if_different = lambda args, changed: True
    module.load_file_common_arguments = lambda params: {}
    changed, message = False, ''
    check_file_attrs(module, changed, message)



# Generated at 2022-06-13 06:02:09.392974
# Unit test for function main
def test_main():
    import os
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

# Generated at 2022-06-13 06:02:44.207250
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

    params['after']

# Generated at 2022-06-13 06:02:56.464107
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec=dict(
        validate=dict(default=None, type='str'),
        path=dict(default=None, type='str'),
        unsafe_writes=dict(default=False, type='bool'),
        contents=dict(default=None, type='str'),
    ))
    test_path = '/tmp/file.txt'
    test_contents = u"this is a test"
    result = {
        'original_basename': os.path.basename(test_path),
        'path': test_path,
    }
    write_changes(module, to_bytes(test_contents, errors='surrogate_or_strict'), test_path)
    assert os.path.isfile(test_path)

# Generated at 2022-06-13 06:02:57.333776
# Unit test for function write_changes
def test_write_changes():
    assert write_changes()


# Generated at 2022-06-13 06:03:07.309935
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=True
    )
    # Pass
    module.params = dict(
        name='/tmp/foo',
        owner='alice',
        group='alice',
        mode='0777',
        seuser='alice',
        serole='alice',
        selevel='alice',
        setype='alice',
        unsafe_writes='alice',
    )
    module.file_exists = Mock(return_value=True)

# Generated at 2022-06-13 06:03:16.751144
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({
        "path": "/tmp/test",
        "unsafe_writes": False,
    })
    file_path = module.params.get("path")
    with open(file_path, 'wb') as file_a:
        file_a.write("test")
    try:
        write_changes(module, "test", file_path)
    except SystemExit:
        pass
    with open(file_path, 'rb') as file_b:
        assert file_b.read() == "test"
    assert os.path.exists(file_path)
    os.remove(file_path)



# Generated at 2022-06-13 06:03:23.376449
# Unit test for function write_changes
def test_write_changes():
    # Arrange
    mock_module = AnsibleModule({})

    # Act
    write_changes(mock_module, b'content', '/tmp/fname')

    # Assert
    assert os.path.exists('/tmp/fname'), 'New file is created'
    assert_file_content('/tmp/fname', 'content')
    os.remove('/tmp/fname')


# Generated at 2022-06-13 06:03:34.262172
# Unit test for function write_changes
def test_write_changes():
    def fake_run_command(*args, **kwargs):
        rc, out, err = (0, '', '')
        # probably more work needs to be done to make this module
        # into a valid unit test
        class FakeModule:
            fail_json = None
            return_value = None
            atomic_move = None
            def __init__(self):
                self.tmpdir = '/tmp'
        return rc, out, err
    old_run_command = AnsibleModule.run_command
    AnsibleModule.run_command = fake_run_command
    module = AnsibleModule()
    path = '/tmp/test_write_changes'
    contents = b"test content"
    write_changes(module, contents, path)
    assert(filecmp.cmp(path, '/tmp/test_write_changes'))


# Generated at 2022-06-13 06:03:46.099862
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec=dict(
        src=dict(type='str', required=True),
        dest=dict(type='str', required=True),
        unsafe_writes=dict(type='bool', required=False, default=False),
        follow=dict(type='bool', required=False, default=False),
        mode=dict(type='str', required=False),
        owner=dict(type='str', required=False),
        group=dict(type='str', required=False),
    ))
    setattr(module, 'CHECKMODE', True)
    # mocked variables
    message = "something"
    changed = True
    setattr(module, 'tmpdir', '/tmp')
    setattr(module, 'params', {})

# Generated at 2022-06-13 06:03:51.811942
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={})
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
    os.fdopen(tmpfd, 'wb').close
    # check for test file
    path=tmpfile
    contents="testfile\nnewline"
    write_changes(module, contents, path)
    text_file = open(tmpfile,"r")
    text=text_file.read()
    assert text==contents
    os.remove(tmpfile)


# Generated at 2022-06-13 06:04:04.733532
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

# Generated at 2022-06-13 06:04:54.801028
# Unit test for function main
def test_main():
    main()

# import modules that are required
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

# import basic ansible modules
from ansible.module_utils.basic import *

# import the requests library
import requests


# Generated at 2022-06-13 06:05:01.681894
# Unit test for function write_changes
def test_write_changes():
    import tempfile
    tmp = tempfile.NamedTemporaryFile(delete=True)
    module = AnsibleModule({
        "path": tmp.name,
        "validate": None
    })
    assert write_changes(module, b'h\x00i', tmp.name) == True
    with open(tmp.name, "rb") as tmp2:
        assert tmp2.read() == b'h\x00i'
    module = AnsibleModule({
        "path": tmp.name,
        "validate": "cat %s"
    })
    assert write_changes(module, b'h\x00i', tmp.name) == True
    with open(tmp.name, "rb") as tmp2:
        assert tmp2.read() == b'h\x00i'

# Generated at 2022-06-13 06:05:13.031014
# Unit test for function write_changes
def test_write_changes():
    # pylint: disable=unused-variable
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch, mock_open, MagicMock, sentinel

    class Module(object):
        def __init__(self):
            self.params = {'unsafe_writes': True}

        def fail_json(self, *args, **kwargs):
            raise Exception('fail_json')

    tmpfd = MagicMock()


# Generated at 2022-06-13 06:05:24.513276
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={
        'path': {'required': True},
        'validate': {'default': None},
        'backup': {'default': False},
        'unsafe_writes': {'type': 'bool', 'default': True},
    })
    contents = "hello world"

    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
    f = os.fdopen(tmpfd, 'wb')
    f.write(contents)
    f.close()

    module.params['path'] = tmpfile
    write_changes(module, contents, tmpfile)

    assert True == os.path.exists(tmpfile)
    os.remove(tmpfile)

# Unit test

# Generated at 2022-06-13 06:05:34.895527
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import strings

    module=basic.AnsibleModule(
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

# Generated at 2022-06-13 06:05:41.007328
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    # Setup the mock module

    module_name = 'ansible.builtin.replace'
    module_args = dict(
            path=dict(type='path', required=True, aliases=['dest', 'destfile', 'name']),
            regexp=dict(type='str', required=True),
            replace=dict(type='str', default=''),
            after=dict(type='str'),
            before=dict(type='str'),
            backup=dict(type='bool', default=False),
            validate=dict(type='str'),
            encoding=dict(type='str', default='utf-8'),
        )


# Generated at 2022-06-13 06:05:51.776848
# Unit test for function check_file_attrs
def test_check_file_attrs():

    # test1 - check_file_attrs - return changed
    module = AnsibleModule(argument_spec=dict())
    changed = True
    message = "Regex search/replace"
    message, changed = check_file_attrs(module, changed, message)
    assert changed is True
    assert message == "Regex search/replace and ownership, perms or SE linux context changed"

    # test2 - check_file_attrs - return same
    module = AnsibleModule(argument_spec=dict())
    changed = False
    message = "Regex search/replace"
    message, changed = check_file_attrs(module, changed, message)
    assert changed is False
    assert message == "Regex search/replace and ownership, perms or SE linux context changed"


# Generated at 2022-06-13 06:05:53.676029
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # TODO: Make a test for this function
    return True



# Generated at 2022-06-13 06:06:02.254252
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path'),
        ),
        supports_check_mode=True
    )
    # mock this out since we don't want to create anything
    module.set_file_attributes_if_different = lambda a, b: True
    # build our "fake" set of args
    args = dict(
        path='/foo/bar',
        follow=False,
        owner='foo',
        group='bar',
        mode=448,
        seuser='foo',
        serole='bar',
        setype='foo',
        selevel='bar',
    )
    # set the file_common_args in our module to this dict
    module.params.update(args)
    # load the file_common_args into module.file_args


# Generated at 2022-06-13 06:06:04.165127
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs(None, True, "") == (' and ownership, perms or SE linux context changed', True)


# Generated at 2022-06-13 06:07:53.040124
# Unit test for function write_changes
def test_write_changes():
    module_args = dict(
        path = "/etc/hosts",
        regexp = "test",
        replace = "test",
        validate= "/bin/bash",
        unsafe_writes = False
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    setattr(module, '_ansible_tmpdir', '/tmp')
    write_changes(module, b"test", "/etc/hosts")


# Generated at 2022-06-13 06:07:58.984283
# Unit test for function write_changes
def test_write_changes():
  import sys
  if sys.version_info[0] < 3 or sys.version_info[1] < 5:
    return
  from unittest.mock import patch, call, MagicMock
  from io import StringIO, BytesIO
  from ansible.module_utils.basic import AnsibleModule
  MyModule = AnsibleModule('/test', None)
  target = MyModule.tmpdir
  with patch('tempfile.mkstemp') as mkstemp:
    with patch('os.fdopen') as fdopen:

      fdopen.return_value = StringIO('newfile_content')  # python3
      mkstemp.return_value = (123, os.path.join(target, 'test'))

# Generated at 2022-06-13 06:08:00.207921
# Unit test for function write_changes
def test_write_changes():
    assert True


# Generated at 2022-06-13 06:08:09.881991
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    # create the expected results for the tests
    path = '/etc/hosts'
    encoding = 'utf-8'

# Generated at 2022-06-13 06:08:22.089898
# Unit test for function write_changes
def test_write_changes():
    from ansible.modules.files.replace import write_changes
    from ansible.module_utils.basic import AnsibleModule

    class TestModule(AnsibleModule):
        @staticmethod
        def fail_json(**kwargs):
            pass

        @staticmethod
        def atomic_move(tmpfile, path, unsafe_writes=False):
            return True

        @staticmethod
        def params():
            return False

        @staticmethod
        def tmpdir():
            return tempfile.gettempdir()

        @classmethod
        def run_command(cls, cmd, *args, **kwargs):
            if cmd == "validate":
                return 0, 0, 0
            else:
                cls.fail_json(msg="expected to call validate")

    path = tempfile.mkstemp()[1]
   

# Generated at 2022-06-13 06:08:35.196802
# Unit test for function main
def test_main():
    argument_spec = dict(
        path=dict(type='path', required=True, aliases=['dest', 'destfile', 'name']),
        regexp=dict(type='str', required=True),
        replace=dict(type='str', default=''),
        after=dict(type='str'),
        before=dict(type='str'),
        backup=dict(type='bool', default=False),
        validate=dict(type='str'),
        encoding=dict(type='str', default='utf-8'),
    )

    # create the mock module
    module = AnsibleModule(argument_spec=argument_spec)

    # Unit tests for function 'write_changes'
    # Nothing to test for now, since the function does not
    # return anything and calling tempfile.mkstemp() lower
    # down in the code will not

# Generated at 2022-06-13 06:08:36.869926
# Unit test for function main
def test_main():
    main()
# main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:08:46.828119
# Unit test for function check_file_attrs
def test_check_file_attrs():

    import ansible.utils.template as template

    # values from argument_spec
    module_args = {
        'src': '/etc/ansible/ansible.cfg',
        'owner': 'root',
        'group': 'root',
        'mode': None,
        'seuser': None,
        'serole': None,
        'setype': None,
        'selevel': None,
    }

    # create a mock module

# Generated at 2022-06-13 06:08:56.085883
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={'path': {'type': 'path', 'required': True}, 'unsafe_writes': {'type': 'bool', 'default': False}})
    module.atomic_move = lambda param1, param2, param3: True
    module.params = {'unsafe_writes': False, 'path': 'test'}
    module.tmpdir = 'test'
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
    os.close(tmpfd)
    tmp_file_f = open(tmpfile, 'w')
    tmp_file_f.write('test')
    tmp_file_f.close()
    contents = 'test'
    write_changes(module, contents, tmpfile)

# Generated at 2022-06-13 06:09:06.369161
# Unit test for function write_changes
def test_write_changes():
    # Create a pretend module
    class module_class :
        params={'unsafe_writes': False}
        def __init__(self, unsafe_writes):
            self.params={'unsafe_writes':unsafe_writes}
        def fail_json(self, msg):
            print("fail msg=%s" % (msg))
        def atomic_move(self, tmpfile, path, unsafe_writes=False):
            #print("atomic_move(tmpfile=%s, path=%s, unsafe_writes=%s" % (tmpfile, path, unsafe_writes))
            if unsafe_writes:
                print("unsafe move")
                os.rename(tmpfile, path)
            else:
                print("safe move")
    module = module_class(False)

    # Make a