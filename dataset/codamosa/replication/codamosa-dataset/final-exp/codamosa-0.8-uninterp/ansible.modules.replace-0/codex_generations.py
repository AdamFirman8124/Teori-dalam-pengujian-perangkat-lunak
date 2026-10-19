

# Generated at 2022-06-13 05:59:51.193406
# Unit test for function write_changes
def test_write_changes():
    pass

# <<INCLUDE_ANSIBLE_MODULE_COMMON>>
ACTION_WARNINGS = [
    "The 'async' option has been replaced with 'poll' and 'poll_interval'",
]

BOOLEANS_TRUE = ['yes', 'on', '1', 'true', 1]
BOOLEANS_FALSE = ['no', 'off', '0', 'false', 0]
BOOLEANS = BOOLEANS_TRUE + BOOLEANS_FALSE

# Generated at 2022-06-13 05:59:58.837450
# Unit test for function main
def test_main():
    args = dict(
        path = '/etc/ansible/ansible.cfg',
        regexp = '^library',
        replace = '#library',
    )

# Generated at 2022-06-13 06:00:07.071307
# Unit test for function write_changes
def test_write_changes():
    class Module(object):
        pass
    module = Module()
    module.tmpdir = tempfile.mkdtemp()
    module.params = {
        'path': test_write_changes.__name__,
        'unsafe_writes': False
    }
    filepath = os.path.join(module.tmpdir, test_write_changes.__name__)
    contents = to_bytes("test")
    write_changes(module, contents, filepath)
    with open(filepath, 'rb') as f:
        file_contents = f.read()
    assert file_contents == contents


# Generated at 2022-06-13 06:00:16.019421
# Unit test for function write_changes
def test_write_changes():
    def test_write_changes(path):
        class AnsibleModule:
            def __init__(self):
                self.tmpdir = '/tmp'
                self.run_command = self.run_command_real
                self.atomic_move = self.atomic_move_real
                self.fail_json = self.atomic_move_real
                self.params = {}
                return None
            def run_command_real(self, cmd):
                print("cmd = %s" % (cmd))
                return (0, "", "")
            def atomic_move_real(self, tmpfile, path, unsafe_writes):
                print("tmpfile = %s path = %s unsafe_writes = %s" % (tmpfile, path, unsafe_writes))
                return None
        module = AnsibleModule()
        contents=b

# Generated at 2022-06-13 06:00:26.049502
# Unit test for function check_file_attrs
def test_check_file_attrs():
    my_module = AnsibleModule(argument_spec={'a': {'type': 'str'}})
    my_module.params['unsafe_writes'] = True
    my_module.params['path'] = '/tmp/foo'
    my_module.params['selevel'] = 's0'

    my_module.set_default_file_attributes = True
    my_module.set_file_attributes_if_different = True

    my_module.tmpdir = '/tmp'

    assert(check_file_attrs(my_module, True, 'Changed') == ('Changed and ownership, perms or SE linux context changed', True))
    assert(check_file_attrs(my_module, False, 'Unchanged') == ('ownership, perms or SE linux context changed', True))

# Generated at 2022-06-13 06:00:32.274282
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # Object creation
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    # Copy of the file's attributes
    file_args = module.load_file_common_arguments(module.params)
    # Test changing the file's attributes and see if function returned true
    module.set_file_attributes_if_different(file_args, False)
    assert check_file_attrs(module, False, "")[1]


# Generated at 2022-06-13 06:00:37.287835
# Unit test for function check_file_attrs
def test_check_file_attrs():

    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.check_mode = True
    path = module._tmpfile_()

    open(path, 'w').close()
    changed, msg = check_file_attrs(module, False, "")
    assert changed == False
    os.remove(path)



# Generated at 2022-06-13 06:00:49.712387
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible import context
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils.six import PY2

    # set up some fake data

# Generated at 2022-06-13 06:00:51.752591
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert isinstance(check_file_attrs(None, None, None), tuple)



# Generated at 2022-06-13 06:00:58.187176
# Unit test for function write_changes
def test_write_changes():
    """ test write_changes """
    module = tempfile.mkdtemp()
    tmpfile = tempfile.mkstemp(dir=module)
    f = os.fdopen(tmpfile[0], 'wb')
    f.write(b'foo')
    f.close()
    write_changes(module, b'bar', tmpfile[1])
    return True


# Generated at 2022-06-13 06:01:17.048875
# Unit test for function main
def test_main():
  contents = "hello world\n"
  regexp = "(hello)\s+world"
  replace = "\1\1"
  result = re.subn(regexp, replace, contents, 0)
  assert result[1] == 1 and result[0] == replace + "\n"

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:01:22.552931
# Unit test for function main
def test_main():
  # Replace function main with our unit test function
  global main
  main = test_ansible_module_replace.test_main
  params = {'regexp': '^(NameVirtualHost|Listen)\s+80\s*$', 'path': '/etc/apache/ports', 'replace': '\g<1> 127.0.0.1:8080'}
  ansible_module_replace.main()


# Generated at 2022-06-13 06:01:26.838045
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class FakeModule:
        def __init__(self):
            self.params = {}
            self.changed = True
            self.tmpdir = ''

        def fail_json(self, *args, **kwargs):
            pass

        def set_file_attributes_if_different(self, fileargs, changed):
            if changed:
                return True
            return False

        def load_file_common_arguments(self, params):
            return {}

    module = FakeModule()
    module.params['unsafe_writes'] = True
    message, module.changed = check_file_attrs(module, module.changed, "")
    assert not module.changed
    module.changed = True
    message, module.changed = check_file_attrs(module, module.changed, "")
    assert module.changed



# Generated at 2022-06-13 06:01:37.850724
# Unit test for function check_file_attrs
def test_check_file_attrs():

    class AnsibleModule(object):

        def __init__(self, *args, **kwargs):
            self.params = args[0]
            self.changed = False

        def set_file_attributes_if_different(self, file_args, changed):
            if file_args:
                self.changed = True
            return self.changed

        def load_file_common_arguments(self, params):
            return params

    # No change
    m = AnsibleModule(dict(
        owner='bob',
        path='/some/path',
        group='users',
        mode='0644',
    ), supports_check_mode=True)
    attr_msg, changed = check_file_attrs(m, False, "")
    assert changed is False
    assert attr_msg == ""

    # Set

# Generated at 2022-06-13 06:01:44.975544
# Unit test for function write_changes
def test_write_changes():
    from ansible.module_utils.basic import AnsibleModule
    tmpfd, tmpfile = tempfile.mkstemp()

    module = AnsibleModule({'backup': 'yes'})
    f = os.fdopen(tmpfd, 'wb')
    f.write(b"Hello")
    f.close()
    path = tmpfile
    contents = b"Hi"

    def run_command_mock(self, cmd):
        return 0, "", ""

    def fail_json_mock(self, **kwargs):
        pass

    def atomic_move_mock(self, src, dest, **kwargs):
        f = os.fdopen(tmpfd, 'wb')
        f.write(contents)
        f.close()
        os.remove(tmpfile)

    module.run_command = run

# Generated at 2022-06-13 06:01:55.888345
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = type('', (), {})()
    module.params = {'path': 'test_path', 'owner': 'test_owner', 'group': 'test_group', 'mode': 'test_mode', 'selevel': 'test_selevel', 'serole': 'test_serole', 'setype': 'test_setype'}
    module.set_file_attributes_if_different = lambda *args, **kwargs: True

    changed = False
    message = ""
    changed_out = True
    message_out = "ownership, perms or SE linux context changed"
    changed, message = check_file_attrs(module, changed, message)
    assert changed == changed_out
    assert message == message_out



# Generated at 2022-06-13 06:02:09.337031
# Unit test for function main
def test_main():
    import json
    import os
    import pytest
    with open('/tmp/testfile', 'wb') as f:
        f.write(b'foo bar baz\n')
        f.write(b'foo bar foz\n')
        f.write(b'foo bar toz\n')
        f.write(b'foo bar quz\n')
        f.write(b'foo bar muz\n')
    module = AnsibleModule({
        'path':'/tmp/testfile',
        'regexp':r'^foo bar (.*?)\n',
        'replace':r'foo bar \1\n',
        'backup':False,
        'check_mode':True,
        'encoding':'ascii',
    })
    main()

# Generated at 2022-06-13 06:02:16.609048
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

# Generated at 2022-06-13 06:02:29.766796
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

# Generated at 2022-06-13 06:02:30.620602
# Unit test for function write_changes
def test_write_changes():  # added by developer
    pass

# Generated at 2022-06-13 06:02:58.444951
# Unit test for function write_changes
def test_write_changes():
    with tempfile.TemporaryDirectory() as temp_dir:
        module = MockModule(tmpdir=temp_dir)
        os.makedirs(module.params['path'])
        write_changes(module, b'hello world', module.params['path'])
        assert open(module.params['path'], 'rb').read() == b'hello world'


# Generated at 2022-06-13 06:03:07.310581
# Unit test for function write_changes
def test_write_changes():
    # This is a really really really really really annoying hack
    class tmp_mod(object):
        def __init__(self):
            self.params = {}
            self.tmpdir = os.path.dirname(__file__)
        def atomic_move(self, old, new, unsafe_writes=None):
            open(new, 'w').write(open(old, 'r').read())
        def run_command(self, cmd):
            return (0, "", "")
        def fail_json(self, **kwargs):
            pass

    test_mod = tmp_mod()
    write_changes(test_mod, "test", os.path.join(test_mod.tmpdir, "test_replace_test"))


# Generated at 2022-06-13 06:03:15.105470
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec=dict(file=dict(type='str')),
                       supports_check_mode=True)

    changed = False
    msg = ''
    test_check_file_attrs = check_file_attrs(module, changed, msg)
    assert test_check_file_attrs[0] == "ownership, perms or SE linux context changed"
    assert test_check_file_attrs[1] == True



# Generated at 2022-06-13 06:03:27.323413
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

# Generated at 2022-06-13 06:03:38.307064
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.module_utils.common._collections_compat import Mapping
    class TestModule(object):
        def __init__(self):
            self.fail_json = lambda x: False
            self.params = {
                'mode': '0777',
                'unsafe_writes': True,
                'owner': 'a',
                'group': 'a',
            }
        def atomic_move(self,x,y,z):
            pass
        def load_file_common_arguments(self, args):
            return args
        def set_file_attributes_if_different(self,file_args, x):
            pass
    tm = TestModule()
    changed = "aaa"
    message = "bbb"
    result = check_file_attrs(tm,changed,message)
   

# Generated at 2022-06-13 06:03:39.305108
# Unit test for function main
def test_main():
    print(main())

# Generated at 2022-06-13 06:03:47.663072
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module=AnsibleModule(argument_spec=dict(path=dict(type='path', required=True), regexp=dict(type='str', required=True), replace=dict(type='str', required=True), backup=dict(type='bool', required=True), before=dict(type='str'), after=dict(type='str', required=True), encoding=dict(type='str', required=True)), supports_check_mode=True)
    file_args = module.load_file_common_arguments(module.params)
    module.set_file_attributes_if_different(file_args, False)

# Generated at 2022-06-13 06:03:55.116535
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
   

# Generated at 2022-06-13 06:04:06.569071
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
    return module

# Unit test case
if __name__ == '__main__':
    module = test_main()
    main()

# Generated at 2022-06-13 06:04:18.763277
# Unit test for function write_changes
def test_write_changes():
    testModule = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True),
            validate=dict(required=True)
        )
    )
    testModule.tmpdir = 'tmp/'
    testModule.run_command = lambda x: (0, '', '')

    testContents = "Test contents"
    testPath = '/test/path'

    write_changes(testModule, to_bytes(testContents), testPath)

    with open(testPath, 'rb') as f:
        fileContents = f.read().decode('utf-8')

    assert(fileContents == testContents)
    os.remove(testPath)



# Generated at 2022-06-13 06:05:22.217372
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class TestModule(object):
        pass
    module = TestModule()
    args = dict(path='/', backup=False, unsafe_writes=False)
    no_args = dict(path='/', backup=False, unsafe_writes=False)
    module.params = args
    module.set_file_attributes_if_different = lambda x, y: True
    module.load_file_common_arguments = lambda x: args
    message = ""
    changed = False
    new_message, new_changed = check_file_attrs(module, changed, message)
    assert message == 'ownership, perms or SE linux context changed'
    module.set_file_attributes_if_different = lambda x, y: False

# Generated at 2022-06-13 06:05:33.323808
# Unit test for function check_file_attrs
def test_check_file_attrs():

    m = AnsibleModule({
        "path": "/tmp/test.txt",
        "regexp": 'test',
        "replace": "test",
        "owner": "test",
        "group": "test",
        "mode": "test",
        "unsafe_writes": False,
        "selevel": "test",
        "serole": "test",
        "setype": "test",
        "seuser": "test",
    }, check_invalid_arguments=False)


# Generated at 2022-06-13 06:05:38.829194
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({'path': 'foo.bar'})
    module.exit_json = lambda x: x
    module.atomic_move = lambda x, y: { 'changed': True, 'path': y }
    module.run_command = lambda x: (0, '', '')
    contents = 'foo'
    path = 'bar'
    write_changes(module, contents, path)


# Generated at 2022-06-13 06:05:53.395693
# Unit test for function check_file_attrs
def test_check_file_attrs():
    tests = list()
    from ansible.module_utils._text import to_bytes

    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    module.exit_json = lambda a: False
    module.fail_json = lambda a: False
    tests.append(dict(
        desc='File attributes',
        module=module,
        file_args={'path': 'test'},
        changed=True,
        message='ownership, perms or SE linux context changed',
    ))
    module.params['seuser'] = None
    module.params['serole'] = None
    module.params['setype'] = None
    module.params['selevel'] = None

# Generated at 2022-06-13 06:06:02.044432
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
            regexp=dict(type='str', required=True),
            replace=dict(type='str'),
            before=dict(type='str'),
            after=dict(type='str'),
            owner=dict(type='str'),
            group=dict(type='str'),
            mode=dict(type='str'),
            seuser=dict(type='str'),
            serole=dict(type='str'),
            setype=dict(type='str'),
            selevel=dict(type='str')
        )
    )
    # check_file_attrs() return changed, message
    # both should be same in our case

# Generated at 2022-06-13 06:06:09.618204
# Unit test for function write_changes
def test_write_changes():
    import shutil
    import time
    import sys
    from io import open

    if sys.version_info >= (2, 6):
        import json
    else:
        import simplejson as json

    class Args(object):
        def __init__(self, **kw):
            self.__dict__.update(kw)

    class AnsibleModule(object):
        def __init__(self, *args, **kw):
            pass
        def exit_json(self):
            pass
        def fail_json(self, **kw):
            pass
        def run_command(self, cmd):
            return 0
        @staticmethod
        def atomic_move(tmpfile, path, unsafe_writes = False):
            shutil.move(tmpfile, path)
        def check_mode(self):
            return False

   

# Generated at 2022-06-13 06:06:21.678936
# Unit test for function main
def test_main():
  import sys
  import os
  import tempfile
  import shutil

# Generated at 2022-06-13 06:06:30.996928
# Unit test for function write_changes
def test_write_changes():
    contents = to_bytes("insights")
    tempfile = os.path.join('/var/tmp', 'test-ansible-replace')
    with open(tempfile, 'wb') as wb:
        wb.write(contents)
    module = AnsibleModule(argument_spec={
        'check_mode': {'default': False, 'type': 'bool'},
        'path': {'type': 'path', 'required': True},
        'mode': {'default': None, 'type': 'raw'},
        'unsafe_writes': {'default': None, 'type': 'bool'},
    })
    module.params['path'] = tempfile
    module.atomic_move = atomic_move
    module.run_command = run_command
    write_changes(module, contents, tempfile)
   

# Generated at 2022-06-13 06:06:32.826369
# Unit test for function main
def test_main():
    assert True is True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:06:33.606039
# Unit test for function check_file_attrs
def test_check_file_attrs():
    return



# Generated at 2022-06-13 06:09:09.699250
# Unit test for function check_file_attrs
def test_check_file_attrs():
    random_file_path = '/tmp/random_file_path'

# Generated at 2022-06-13 06:09:18.140187
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
            regexp=dict(type='str', required=True),
            replace=dict(type='str'),
            after=dict(type='str'),
            before=dict(type='str'),
            backup=dict(type='bool', default=False),
            encoding=dict(type='str', default='utf-8'),
            follow=dict(type='bool', default=False),
            force=dict(type='bool', default=False, aliases=['thirsty']),
            validate=dict(type='str'),
            other=dict(),
        )
    )
    setattr(module, 'set_file_attributes_if_different', True)

   

# Generated at 2022-06-13 06:09:22.977117
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={'path':{'type':'path'},'test':{'type':'str'},'validate':{'type':'str'},'unsafe_writes':{'required':False,'type':'bool','default':True}})
    module.run_command = lambda: [0, 'out', 'err']
    module.atomic_move = lambda x,y,z: None
    test_string = 'test'
    write_changes(module, test_string, 'testpath')
    assert module.run_command.call_count == 1
    assert module.atomic_move.call_count == 1

