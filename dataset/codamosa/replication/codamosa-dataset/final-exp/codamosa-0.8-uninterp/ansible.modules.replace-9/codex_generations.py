

# Generated at 2022-06-13 05:59:49.393746
# Unit test for function main
def test_main():
    path = 'myfile'
    regexp = 'abc'
    replace = 'xyz'
    after = 'savor'
    before = 'savor'
    backup = False
    validate = 'apachectl -t'
    with patch('ansible.module_utils.basic.AnsibleModule') as mock_module:
        obj = mock_module.return_value
        obj.params = {
            'path': path,
            'regexp': regexp,
            'replace': replace,
            'after': after,
            'before': before,
            'backup': backup,
            'validate': validate,
        }
        obj.check_mode = False
        obj.set_file_attributes_if_different.return_value = True
        obj.atomic_move.return_value = True

# Generated at 2022-06-13 05:59:56.130927
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

# Generated at 2022-06-13 06:00:07.530261
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # Mock file attributes
    get_file_attributes = {'owner': 'evan', 'group': 'evan', 'mode': '0644'}
    exists = True
    # Mock module, module.params and other properties.
    module = AnsibleModule({})
    module.set_file_attributes_if_different = mock_set_file_attributes_if_different
    return_val = check_file_attrs(module, False, "")
    assert return_val[0] == "ownership, perms or SE linux context changed"
    assert return_val[1]
    # Unit test for function check_file_attrs, test for value unchanged
    get_file_attributes = {'owner': 'root', 'group': 'root', 'mode': '0644'}
    return_val = check_file_

# Generated at 2022-06-13 06:00:13.365021
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={})
    module.params.update(dict( path='/tmp', content='{}', owner='user', group='group', mode='0644', seuser='user', serole='role', setype='type'))
    changed, message = False, ''
    return_message, return_changed = check_file_attrs(module, changed, message)
    assert return_message == 'ownership, perms or SE linux context changed'
    assert return_changed == True


# Generated at 2022-06-13 06:00:22.565301
# Unit test for function write_changes
def test_write_changes():
    f = tempfile.NamedTemporaryFile(mode='a', delete=False)
    f.write('change\n')
    f.close()
    module_args = dict(
        path=f.name,
        validate=None,
        unsafe_writes=False,
    )
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )
    write_changes(module, 'unchange\n', f.name)
    f = open(f.name, 'r')
    assert f.read() == 'unchange\n'
    os.unlink(f.name)



# Generated at 2022-06-13 06:00:25.897698
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={'path': {}, 'unsafe_writes': {}})
    changed = False
    message = ""
    module.params['owner'] = "auser"
    module.params['group'] = "agroup"
    module.params['seuser'] = "aseuser"
    module.params['serole'] = "aserole"
    module.params['selevel'] = "aselevel"
    message,changed = check_file_attrs(module, changed, message)
    assert changed == True


# Generated at 2022-06-13 06:00:35.730927
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec=dict())

    class MockModule:
        pass

    m = MockModule()
    m.params = dict()
    m.tmpdir = tempfile.mkdtemp()
    m.run_command = lambda x: (0, '', '')
    m.fail_json = lambda x: None
    m.atomic_move = lambda x, y, z: None

    setattr(m, "check_mode", False)

    class MockFileArgs:
        pass

    f = MockFileArgs()
    f.content = "content"
    def mock_set_file_attributes_if_different(f, c):
        return True
    m.set_file_attributes_if_different = mock_set_file_attributes_if_different
    m.diff = "diff"


# Generated at 2022-06-13 06:00:39.226551
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs(module, False, "test") == ('test and ownership, perms or SE linux context changed', True,)
    assert check_file_attrs(module, True, "test") == ('test and ownership, perms or SE linux context changed', True,)


# Generated at 2022-06-13 06:00:46.458956
# Unit test for function main
def test_main():
  from ansible.module_utils import basic
  from ansible.module_utils._text import to_bytes
  module = AnsibleModule(argument_spec=dict(path=dict(type='path', required=True, aliases=['dest', 'destfile', 'name']), regexp=dict(type='str', required=True), replace=dict(type='str', default=''), after=dict(type='str'), before=dict(type='str'), backup=dict(type='bool', default=False), validate=dict(type='str'), encoding=dict(type='str', default='utf-8')))
  path = "/home/admin/Downloads/ansible/library/ansible/builtin/replace.py"
  encoding = "utf-8"

# Generated at 2022-06-13 06:00:56.113887
# Unit test for function write_changes
def test_write_changes():
    os.chdir(os.path.dirname(__file__))
    m = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True, type='path'),
            unsafe_writes=dict(required=False, default=False, type='bool'),
        ),
    )
    # Write out changes
    write_changes(m, 'test', os.path.abspath("./test.file"))
    res_file = open("./test.file")
    res = res_file.read()
    res_file.close()
    os.remove("./test.file")
    if res != "test":
        raise AssertionError('test_write_changes result: "%s" != "test"' % res)
    # Fail validation

# Generated at 2022-06-13 06:01:24.516004
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = type('module', (object, ), {})
    module.set_file_attributes_if_different = lambda x, y: True
    module.params = {}
    module.load_file_common_arguments = lambda x: dict()
    assert ('ownership, perms or SE linux context changed', True) == check_file_attrs(module, False, "")
    assert ('msg and ownership, perms or SE linux context changed', True) == check_file_attrs(module, True, "msg")



# Generated at 2022-06-13 06:01:27.355831
# Unit test for function write_changes
def test_write_changes():
    # Replace this with your actual test.
    assert "write_changes" == "test_write_changes"


# Generated at 2022-06-13 06:01:35.523391
# Unit test for function write_changes
def test_write_changes():
    module=AnsibleModule({'changed':False, 'msg':''})
    fd, path=tempfile.mkstemp(dir='/tmp')
    contents=to_bytes(u'Some test text\n')
    os.close(fd)
    module.params['unsafe_writes']=True
    write_changes(module, contents, path)
    assert os.path.exists(path)
    assert os.path.getmtime(path) >= module.start
    assert os.path.getsize(path) == len(contents)
    os.unlink(path)



# Generated at 2022-06-13 06:01:37.937707
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs(module, True, "temp") == ("temp and ownership, perms or SE linux context changed", True)


# Generated at 2022-06-13 06:01:47.789947
# Unit test for function check_file_attrs
def test_check_file_attrs():
    message_pass = "message1"
    message_fail = "message2"
    class TestModule():
        def __init__(self):
            self.changed = False
            self.params = {}
            self.fail_json = lambda msg, **kwargs: fail(msg)
            self.run_command = lambda cmd: (0, '', '')
            self.atomic_move = lambda src, dest: None
            self.load_file_common_arguments = lambda src: {}
            self.set_file_attributes_if_different = lambda src, dest, unsafe_writes = False: True
    module = TestModule()
    changed = False
    message, changed = check_file_attrs(module, changed, message_pass)
    if not changed:
        fail("Got unexpected result changed == False")

# Generated at 2022-06-13 06:01:58.647295
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    import ansible.module_utils.ansible_release
    import ansible.module_utils.six
    import platform
    import os
    import pwd
    import shutil
    import tempfile
    import time
    import pytest
    import json
    import string
    import random

    # Create temporary file
    TEST_DIR = tempfile.mkdtemp()

    TEST_FILE = os.path.join(TEST_DIR, "test_file")

    # Create temporary file with random content
    with open(TEST_FILE, "w") as f:
        f.write("".join([random.choice(string.ascii_letters) for i in range(10)]))

    # Set args

# Generated at 2022-06-13 06:02:11.548332
# Unit test for function write_changes
def test_write_changes():
    class TestModule(object):
        def __init__(self):
            self.params = {}
        def fail_json(self, **kwargs):
            self.exception = kwargs["msg"]
        def atomic_move(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c
        def run_command(self, cmd):
            self.command = cmd
            self.command_results = [0, "", ""]
            return self.command_results
    from io import BytesIO
    f = BytesIO()
    f.write("abcde12345")

    f.seek(0)
    module = TestModule()

# Generated at 2022-06-13 06:02:18.453728
# Unit test for function main
def test_main():
    # Create a module
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True, type='str'),
            regexp = dict(required=True, type='str'),
            replace = dict(required=False, default='', type='str'),
            after = dict(required=False, default=None, type='str'),
            before = dict(required=False, default=None, type='str'),
            backup = dict(required=False, default='no', type='bool'),
            validate = dict(required=False, default=None, type='str'),
            encoding = dict(required=False, default='utf-8', type='str'),
        )
    )
    module.run_command = MagicMock(return_value=(0, '', ''))
    module.backup_local = MagicMock

# Generated at 2022-06-13 06:02:29.160884
# Unit test for function write_changes
def test_write_changes():
    test_contents = '''
the quick brown fox jumps over
the lazy dog
'''
    test_file_name = '/tmp/test_file'
    f = open(test_file_name, 'wb')
    f.write(test_contents.encode())
    f.close()
    module = FakeModule()
    module.params['validate'] = 'cat %s'
    write_changes(module, b'Changed\n', test_file_name)
    assert (open(test_file_name, 'rb').readlines() == [b'Changed\n'])
    os.remove(test_file_name)



# Generated at 2022-06-13 06:02:36.032298
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module_mock = AnsibleModule({'path': '/test', 'owner': 'test'}, check_invalid_arguments=False)
    # Returns a mock object attributes are not correct
    module_mock.set_file_attributes_if_different = lambda x, y: y
    assert check_file_attrs(module_mock, True, "mock") == ("mock and ownership, perms or SE linux context changed", True)
    # Returns a mock object attributes are correct
    module_mock.set_file_attributes_if_different = lambda x, y: not y
    assert check_file_attrs(module_mock, True, "mock") == ("mock", True)
    assert check_file_attrs(module_mock, False, "mock") == ("mock", False)




# Generated at 2022-06-13 06:03:04.174980
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({
        'path': '/tmp/test/path',
        'validate': '/bin/echo %s',
        'unsafe_writes': True,
        '_ansible_tmpdir': '/tmp/test'})
    contents = 'test content\n'
    write_changes(module, contents, module.params['path'])
    with open(module.params['path']) as f:
        assert f.read() == 'test content\n'


# Generated at 2022-06-13 06:03:16.753651
# Unit test for function write_changes
def test_write_changes():
    from ansible.module_utils.six.moves import StringIO
    from ansible.module_utils import basic
    import ansible.module_utils.action_plugins.replace as replace_utils

    module = basic.AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
            regexp=dict(type='str', required=True),
            replace=dict(type='str', required=False, default=''),
            validate=dict(type='str', required=False),
            unsafe_writes=dict(type='bool', required=False, default=True)
        )
    )
    path = '/bin/foo'
    contents = b'foo bar test\nfoo'
    regexp = 'foo'
    replace = 'foo replaced'
    validate = 'true'



# Generated at 2022-06-13 06:03:19.242054
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:03:30.487906
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    
    fake_module = basic.AnsibleModule(
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
    main(fake_module)


# Generated at 2022-06-13 06:03:43.057256
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={
        'path': {'type': 'str', 'required': True},
        'validate': {'type': 'str'},
        'unsafe_writes': {'type': 'bool', 'default': False},
        })
    setattr(module, 'tmpdir', '/tmp')
    contents = b"0123456789"
    path = '/tmp/ansible_test_file'
    # test with a file that validates
    module.params.update({'validate': "test -f '%s'"})
    write_changes(module, contents, path)
    with open(path, 'rb') as f:
        for i, line in enumerate(f):
            assert(line == contents[i:i+1])
    os.remove(path)
   

# Generated at 2022-06-13 06:03:43.664606
# Unit test for function write_changes
def test_write_changes():
    pass



# Generated at 2022-06-13 06:03:47.039389
# Unit test for function check_file_attrs
def test_check_file_attrs():

    module = AnsibleModule(argument_spec={'path': {}})
    return



# Generated at 2022-06-13 06:03:54.693157
# Unit test for function main
def test_main():
    REQUEST_FUNC = 'ansible.modules.files.replace.main'
    class Request(object):
        def __init__(self, params):
            self.params = params

    class Module(object):
        def __init__(self, params):
            self.params = params

        def fail_json(self, *args, **kwargs):
            raise Exception('FAIL')

        def exit_json(self, *args, **kwargs):
            return

        def atomic_move(self, *args, **kwargs):
            return

        def set_file_attributes_if_different(self, *args, **kwargs):
            return False

        def load_file_common_arguments(self, *args, **kwargs):
            return {}


# Generated at 2022-06-13 06:04:03.166311
# Unit test for function main
def test_main():
    # The function main is located in the __main__ namespace. 
    # To test it we need to get it from there
    _main = globals().get('__main__')
    print(_main)
    # Now we can call it and pass the global variable __file__
    # which will be passed to the AnsibleModule
    _main.main(["-f", __file__, "-v", "-v", "-v"])

if __name__ == '__main__':
    # import sys
    # print(sys.argv)
    test_main()

# Generated at 2022-06-13 06:04:10.915140
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class ModuleStub(object):
        def __init__(self):
            self.params = dict(
                path='',
                mode=None,
                owner=None,
                group=None,
                seuser=None,
                serole=None,
                setype=None,
                selevel=None,
                unsafe_writes=None,
            )
            self.atomic_move = lambda x, y, z: None
            return None
        def fail_json(*args, **kwargs):
            return None
        def set_file_attributes_if_different(*args, **kwargs):
            return False
        def load_file_common_arguments(*args, **kwargs):
            return dict()
    module = ModuleStub()
    message, changed = check_file_attrs(module, False, '')

# Generated at 2022-06-13 06:05:03.589093
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class FakeModule:
        def __init__(self):
            self.params = {}
        def load_file_common_arguments(self,params):
            return params

    module_test = FakeModule()
    changed = True
    message = "content changed"
    module_test.params['owner'] = 'root'
    module_test.params['group'] = 'root'
    module_test.params['mode'] = '0640'
    module_test.params['selinux_spec_file'] = '/etc/ssh/sshd_config'
    module_test.params['selevel'] = 's0'
    message, changed = check_file_attrs(module_test, changed, message)
    assert (message == "content changed and ownership, perms or SE linux context changed")
    assert (changed == True)



# Generated at 2022-06-13 06:05:09.655204
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={})
    file_args = dict(
        path='/foo',
        mode='0755',
        owner='root',
        group='root'
    )
    module.set_file_attributes_if_different = lambda a, b: a == file_args and b is False
    check_file_attrs(module, True, "Test message")


# Generated at 2022-06-13 06:05:21.173421
# Unit test for function main
def test_main():
    # Imports
    import tempfile
    import os
    # Mocks
    class MockModule1(object):
        def __init__(self):
            self.params = {
                'after' : None,
                'backup' : False,
                'before' : None,
                'dest' : '/tmp/test',
                'name' : None,
                'path' : '/tmp/test',
                'regexp' : 'foo',
                'replace' : 'bar',
                'validate' : None,
            }
            self.tmpdir = tempfile.mkdtemp()
            self._diff = False
            self._ansible_module = None
        def fail_json(self, *args, **kwargs):
            raise Exception("fail_json called")

# Generated at 2022-06-13 06:05:32.486284
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(type='path', required=True),
            regexp = dict(type='str', required=True),
            replace = dict(type='str', required=True),
            owner = dict(type='str'),
            group = dict(type='str'),
            mode = dict(type='str'),
            seuser = dict(type='str'),
            serole = dict(type='str'),
            setype = dict(type='str'),
            selevel = dict(type='str'),
        )
    )
    changed = True
    message = "test"
    ret_msg, ret_changed = check_file_attrs(module, changed, message)
    assert ret_msg == "test and ownership, perms or SE linux context changed"
    assert ret_changed

# Generated at 2022-06-13 06:05:42.338578
# Unit test for function check_file_attrs
def test_check_file_attrs():

    class FakeModule():
        class FakeParams():
            changed = True
        class FakeFileCommonArguments():
            changed = True
        def __init__(self):
            self.params = self.FakeParams()
        def set_file_attributes_if_different(self, args, check_mode=False):
            return check_mode
        def load_file_common_arguments(self, params):
            return self.FakeFileCommonArguments()

    test_module = FakeModule()
    test_message = "Test Message"
    assert("Test Message and ownership, perms or SE linux context changed") == check_file_attrs(test_module, True, test_message)[0]
    test_module.params.changed = False

# Generated at 2022-06-13 06:05:56.150060
# Unit test for function main
def test_main():
    class TestModule(object):
        def __init__(self, params, path):
            self.params = params
            self.path = path
            self.run_command_calls = []

        def fail_json(self, msg, **kwargs):
            raise Exception(msg)

        def set_file_attributes_if_different(self, file_args, changed):
            return changed

        def load_file_common_arguments(self, params):
            return params

        def run_command(self, cmd):
            self.run_command_calls.append(cmd)
            return (0, "", "")

        def atomic_move(self, tmpfile, path, unsafe_writes=False):
            return True


# Generated at 2022-06-13 06:06:00.382737
# Unit test for function write_changes
def test_write_changes():
    contents = 'test contents'
    path = '/test/tmpfile'
    module = AnsibleModule({})
    module.tmpdir = '/test'
    module.atomic_move = lambda *args, **kargs: (path, None)
    module.run_command = lambda cmd: (0, '', '')
    write_changes(module, contents, path)
    assert os.path.exists(path)



# Generated at 2022-06-13 06:06:08.575862
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec = { 'path': {'type': 'str', 'required': True},
                                             'content': {'type': 'str', 'required': False},
                                             'owner': {'type': 'str', 'required': True},
                                             'group': {'type': 'str', 'required': True},
                                             'mode': {'type': 'str', 'required': True}
                                           })
    changed = False
    message = "Unit tests for function check_file_attrs"
    message, changed = check_file_attrs(module, changed, message)
    assert changed == True
    assert message == "Unit tests for function check_file_attrs and ownership, perms or SE linux context changed"


# Generated at 2022-06-13 06:06:18.594918
# Unit test for function write_changes
def test_write_changes():
    f = tempfile.NamedTemporaryFile()
    path = f.name
    f.close()
    m = AnsibleModule(argument_spec=dict(path=dict()))
    m.params = dict(path=path)
    m.check_mode = False
    m.atomic_move = lambda src, dest: os.rename(src, dest)
    write_changes(m, b"contents", path)
    assert os.path.isfile(path)
    with open(path, "rb") as f:
        contents = f.read()
    assert contents == b"contents"
    os.unlink(path)


# Generated at 2022-06-13 06:06:25.129397
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({'unsafe_writes': 'yes'})
    module.params['path'] = 'test'
    module.params['owner'] = 'test'
    module.params['group'] = 'test'
    module.params['mode'] = 'test'
    module.atomic_move = lambda src, dest, unsafe_writes: None
    test_module, test_changed, test_message = check_file_attrs(module,False,"test")
    assert(test_changed)
    assert(test_message == "ownership, perms or SE linux context changed")


# Generated at 2022-06-13 06:08:24.096540
# Unit test for function check_file_attrs
def test_check_file_attrs():
    m = AnsibleModule(argument_spec={})
    class FakeModule:
      def __init__(self, *args, **kwargs):
        self.params = {}
        self.tmpdir = '/tmp'
        self.atomic_move = lambda x, y, z: None
        self.run_command = lambda x: [0]
      def fail_json(self, **args):
        raise Exception(args['msg'])
    m._ansible_module = FakeModule()
            
    assert check_file_attrs(m,False,'') == ('ownership, perms or SE linux context changed', True)
    assert check_file_attrs(m,True,'foo') == ('foo and ownership, perms or SE linux context changed', True)


# Generated at 2022-06-13 06:08:35.771633
# Unit test for function write_changes
def test_write_changes():
    class TestModule:
        def fail_json(self, msg):
            raise AssertionError(msg)
        def atomic_move(self, tmpfile, path, unsafe_writes):
            pass
    path = '/tmp/test_file'
    contents = ['hello', 'this is my text file']
    val = 'my validator'
    test_module = TestModule()
    test_module.params = {
        'validate': val,
        'unsafe_writes': False,
        'tmpdir': '/tmp/',
    }
    test_module.run_command = test_run_command
    try:
        write_changes(test_module, contents, path)
    except AssertionError as e:
        raise AssertionError(e.message)


# Generated at 2022-06-13 06:08:37.098041
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:08:40.292651
# Unit test for function check_file_attrs
def test_check_file_attrs():
    #Check if module is created
    assert check_file_attrs(AnsibleModule, True, "file already exists")


# Generated at 2022-06-13 06:08:48.014864
# Unit test for function write_changes
def test_write_changes():

    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True, aliases=['dest', 'destfile', 'name']),
            tmpdir=dict(type='path'),
            unsafe_writes=dict(type='bool', default=False),
            validate=dict(type='str'),
        ),
    )

    path = os.path.realpath("/tmp/test")
    contents = to_bytes("test text")
    module.params["path"] = path
    write_changes(module, contents, path)
    assert os.path.isfile(path)
    with open(path) as f:
        assert f.read() == "test text"
    os.remove(path)

    # With validation
    module.params["validate"] = "/bin/true %s"

# Generated at 2022-06-13 06:08:52.987053
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={})
    module.exit_json = lambda **args: args

    res = main()
    assert res['msg'] == 'Path /etc/hosts is a directory !'

    res = main()
    assert res['changed'] == False
    assert res['msg'] == 'Path /etc/hosts does not exist !'


# Generated at 2022-06-13 06:08:59.757772
# Unit test for function check_file_attrs

# Generated at 2022-06-13 06:09:07.470839
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs(AnsibleModule(argument_spec={'path': {'type': 'path'}, 'mode': {'type': 'raw'}, 'owner': {'required': False},
                                                          'group': {'required': False}, 'seuser': {'required': False}, 'serole': {'required': False},
                                                          'setype': {'required': False}, 'selevel': {'required': False}, 'unsafe_writes': {'type': 'bool', 'required': False, 'default': False}}),
                                                          False, "") == ("ownership, perms or SE linux context changed", True)


# Generated at 2022-06-13 06:09:17.565551
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.module_utils.basic import AnsibleModule
    import errno
    try:
        os.makedirs('testdata')
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir('testdata'):
            pass
        else: raise

    with open('testdata/check_file_attrs', 'w') as f:
        f.write('test')
    os.chmod('testdata/check_file_attrs', 0o644)
    os.chown('testdata/check_file_attrs', 0, 0)
    changed = False
    msg = ""
    os.chown('testdata/check_file_attrs', 1, 1)

# Generated at 2022-06-13 06:09:26.790661
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True),
            regexp=dict(required=True),
            replace=dict(default=''),
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

    params['after'] = to_text(params['after'], errors='surrogate_or_strict', nonstring='passthru')