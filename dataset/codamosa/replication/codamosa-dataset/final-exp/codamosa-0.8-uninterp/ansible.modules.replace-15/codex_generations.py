

# Generated at 2022-06-13 05:59:52.002977
# Unit test for function check_file_attrs
def test_check_file_attrs():
    '''
    check_file_attrs test
    '''
    module = AnsibleModule(argument_spec = dict())
    module.params = {}
    module.params['path'] = None
    module.params['owner'] = None
    module.params['group'] = None
    module.params['mode'] = None
    module.atomic_move = None
    module.set_file_attributes_if_different = None
    module.fail_json = None

    # Testing changed = True and message = ''
    changed = True
    message = ''
    res_message, res_changed = check_file_attrs(module, changed, message)
    assert (res_changed is True) and (res_message == 'ownership, perms or SE linux context changed')
    # Testing changed = False and message = 'perms or SE linux

# Generated at 2022-06-13 05:59:52.982370
# Unit test for function main
def test_main():
   contents = "old.host.name"
if __name__ == '__main__':
   main()

# Generated at 2022-06-13 05:59:57.944864
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={'unsafe_writes':{'type':'bool'}})
    module.atomic_move = lambda a, b, c: None
    write_changes(module, 'new file contents'.encode(), '/does/not/matter')


# Generated at 2022-06-13 06:00:02.563762
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec = dict())
    changed = True
    message = "message"

    message, changed = check_file_attrs(module, changed, message)
    assert (message == "message")
    assert (changed)

# End of unit tests.



# Generated at 2022-06-13 06:00:11.169156
# Unit test for function write_changes
def test_write_changes():

    class DummyModule(object):
        params = dict()
        tmpdir = tempfile.mkdtemp(prefix='ansible-tmp-')
        def fail_json(self, msg):
            self.fail_msg = msg
        def atomic_move(self, tmpfile, path, unsafe_writes=None):
            assert unsafe_writes == False
            self.atomic_path = path
        def run_command(self, cmd):
            out = ''
            err = ''
            rc = 0
            if cmd.startswith('md5sum'):
                try:
                    md5sum = open(cmd.split()[1]).read().split()[0]
                except IOError:
                    err = 'No such file or directory'
                    rc = 1
                    return (rc, out, err)

# Generated at 2022-06-13 06:00:23.161786
# Unit test for function write_changes
def test_write_changes():
    # Note: tmpdir is a module variable set by the test framework.
    # It's not defined in the code itself.
    assert to_text(tmpdir, errors='surrogate_or_strict') != u''
    # Make a tmpfile in the tmpdir and write a bit of data to it
    filename = 'test.tmp'
    tmpfd, tmpfile = tempfile.mkstemp(dir=tmpdir)
    f = os.fdopen(tmpfd, 'wb')
    f.write('foo')
    f.close()
    # We'll just mock the atomic_move() function, since there is no
    # need to actually do it.
    atomic_move_orig = AnsibleModule.atomic_move

    def atomic_move(self, src, dest, unsafe_writes=True):
        pass

    # Now mock

# Generated at 2022-06-13 06:00:31.164837
# Unit test for function write_changes
def test_write_changes():
    contents = """
#Test Text
test
test second line
"""
    module = AnsibleModule(argument_spec={'unsafe_writes': dict(type='bool', default=True), 'validate': dict()})
    module.tmpdir = tempfile.gettempdir()
    tf = tempfile.NamedTemporaryFile(delete=False)
    tf.write(contents.encode())
    path = tf.name
    write_changes(module, contents.encode(), path)
    with open(path, 'rb') as f:
        assert f.read() == contents
        f.close()
    os.unlink(path)


# Generated at 2022-06-13 06:00:40.367848
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module_mock = AnsibleModule({})
    changed = True
    message = "something changed"

    class MockModule(object):
        pass

    file_args = MockModule()
    file_args.params = {}
    file_args.params['owner'] = 'root'
    file_args.params['group'] = 'root'
    file_args.params['mode'] = 'a+r'

    module_mock.params = file_args.params
    module_mock.set_file_attributes_if_different = lambda x, y: True

    assert(check_file_attrs(module_mock, changed, message) == ("something changed and ownership, perms or SE linux context changed", True))


# Generated at 2022-06-13 06:00:41.994989
# Unit test for function main
def test_main():
    assert 1


if __name__ == "__main__":
    main()

# Generated at 2022-06-13 06:00:52.982156
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec=dict(
        src=dict(required=True, type='path'),
        dest=dict(required=True, type='path'),
        content=dict(required=True),
        validate=dict(required=False, type='str'),
        create=dict(required=False, type='bool'),
        safe_file_operations=dict(required=False, type='bool'),
        force=dict(required=False, type='bool'),
        unsafe_writes=dict(required=False, default=False, type='bool'),
    ))
    message = "Hello"
    changed, message = check_file_attrs(module, False, message)
    return message, changed


# Generated at 2022-06-13 06:01:08.956665
# Unit test for function check_file_attrs
def test_check_file_attrs():
    changed = False
    msg = "test"
    check_file_attrs(dict, changed, msg)
    changed = True
    msg = "test"
    check_file_attrs(dict, changed, msg)



# Generated at 2022-06-13 06:01:13.469591
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
    test_module.tmpdir = tempfile.gettempdir()

# Generated at 2022-06-13 06:01:23.567861
# Unit test for function main
def test_main():
    from ansible.module_utils import basic

    module = basic.AnsibleModule(
        argument_spec = dict(
            path = dict(type="path", required=True, aliases=['dest', 'destfile', 'name']),
            regexp = dict(type="str", required=True),
            replace = dict(type="str", default=''),
            after = dict(type="str"),
            before = dict(type="str"),
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
   

# Generated at 2022-06-13 06:01:28.607402
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import json
    import ansible.module_ansible_metrics_replace as amr

    with open('test_main.json', 'r') as file_data:
        amr.main()



# Generated at 2022-06-13 06:01:39.050289
# Unit test for function main
def test_main():
    import os

    from ansible.module_utils.basic import AnsibleModule

    from ansible.module_utils._text import to_bytes, to_text

    from ansible.module_utils.pycompat24 import get_exception

# Generated at 2022-06-13 06:01:48.120989
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.module_utils.basic import AnsibleModule
    import os

    validate = "/bin/true"
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(default='/tmp/testfile', aliases=['dest', 'name']),
            regexp=dict(required=True),
            replace=dict(default=""),
            validate=dict(default=validate),
            owner=dict(),
            group=dict(),
            mode=dict(),
            unsafe_writes=dict(default=True, type='bool'),
        ),
    )
    f = open(module.params['path'], "w")
    f.write("this is a test file\n")
    f.write("this is the second line\n")
    f.close()


# Generated at 2022-06-13 06:01:56.496324
# Unit test for function main
def test_main():
  data={}
  data['path']='/etc/hosts'
  data['backup']=False
  data['validate']=None
  data['unsafe_writes']=True
  data['replace']='  127.0.0.1 localhost.localdomain localhost\n'
  data['regexp']='^(?P<dctv>ListenAddress[   ]+)(?P<host>[^\n]+)$'
  main(data)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:02:07.977178
# Unit test for function main
def test_main():
    # File, file, str, str, bool, str, str
    module = AnsibleModule(argument_spec=dict(path=dict(type='path',required=True,aliases=['dest', 'destfile', 'name']),regexp=dict(type='str',required=True),replace=dict(type='str',default=''),after=dict(type='str'),before=dict(type='str'),backup=dict(type='bool',default=False),validate=dict(type='str'),encoding=dict(type='str',default='utf-8'),),add_file_common_args=True,supports_check_mode=True,)
    assert main() == "This is true"

# Generated at 2022-06-13 06:02:15.164459
# Unit test for function write_changes
def test_write_changes():
    contents = b"Testing write_changes"
    path = "testFile"
    module = AnsibleModule(argument_spec={})

    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)

    write_changes(module, contents, path)
    f = os.fdopen(tmpfd, 'wb')
    f.write(contents)
    f.close()

    valid = True
    if valid:
        module.atomic_move(tmpfile, path, unsafe_writes=module.params['unsafe_writes'])

    print (path)
    f = open(path, 'rb')
    new_contents = f.read()
    f.close()

    assert new_contents == contents
    os.remove(path)


# Generated at 2022-06-13 06:02:28.802865
# Unit test for function main

# Generated at 2022-06-13 06:03:01.973822
# Unit test for function write_changes
def test_write_changes():
    import sys
    import stat
    if sys.version_info[0] >= 3:
        from unittest.mock import patch, MagicMock
    else:
        from mock import patch, MagicMock
    module = MagicMock()
    module.params = {'validate': None, 'unsafe_writes': False}
    module.tmpdir = '/tmp'
    contents = to_bytes('test')
    path = '/tmp/test'

# Generated at 2022-06-13 06:03:09.633686
# Unit test for function main
def test_main():
  from ansible.module_utils.basic import AnsibleModule

  import os
  import sys
  import shutil
  import tempfile
  import re
  import json

  def get_exception():
    exc_type, exc_value, exc_traceback = sys.exc_info()
    error = repr(traceback.format_exception(exc_type, exc_value, exc_traceback))
    return error  


# Generated at 2022-06-13 06:03:15.447420
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible_collections.ansible.builtin.plugins.module_utils.basic import AnsibleModule
    from ansible_collections.ansible.builtin.plugins.modules.files import check_file_attrs
    assert check_file_attrs(AnsibleModule, False, "foobar") == ("foobar", False)


# Generated at 2022-06-13 06:03:28.301813
# Unit test for function check_file_attrs
def test_check_file_attrs():

    class FakeModule(object):
        def __init__(self):
            self.changed = False
            self.params = dict(
                src='/tmp/file.txt'
            )
            self.file_args = dict(
                path='/tmp/file.txt',
                mode=None,
                owner=None,
                group=None,
                seuser=None,
                serole=None,
                selevel=None,
                setype=None,
            )

        def load_file_common_arguments(self, params):
            return self.file_args

        def set_file_attributes_if_different(self, file_args, changed):
            self.changed = True
            return self.changed

    m = FakeModule()
    ret = check_file_attrs(m, False, 'hello')

# Generated at 2022-06-13 06:03:37.599184
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
  check_file_attrs
  check_file_attrs(module=module,changed=True,message="xxx")


# Generated at 2022-06-13 06:03:48.298568
# Unit test for function main
def test_main():
    os = MockOS()
    module = MockModule()

    with patch('os.path.isdir', os.path.isdir):
        assert_raises(AnsibleFailJson, main, module)


# Generated at 2022-06-13 06:03:56.503377
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={})
    path = "/tmp/foo"
    contents = "bar"
    write_changes(module, contents, path)
    try:
        with open(path, "r") as f:
            txt = f.read()
        assert txt == "bar"
        os.remove(path)
    except:
        os.remove(path)
        raise

# ===========================================
# Main control flow


# Generated at 2022-06-13 06:04:07.307230
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class ModuleArgs(object):
        def __init__(self):
            self.params = {}
            self.params['unsafe_writes'] = False
            self.params['backup'] = False
            self.params['group'] = 'root'
            self.params['owner'] = 'root'
            self.params['mode'] = '0644'

    class FakeModule(object):
        def __init__(self):
            self.check_mode = False
            self.debug = False
            self.diff = False
            self.params = ModuleArgs()
            self.tmpdir = None

        def fail_json(self, **kwargs):
            raise Exception(kwargs['msg'])

        def run_command(self, *args, **kwargs):
            return (0, "Output", "Error")


# Generated at 2022-06-13 06:04:19.312570
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
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:04:20.776213
# Unit test for function write_changes
def test_write_changes():
    # We could actually test this, but the test would be longer than the function
    # and would still require mocking and we'd end up running run_command anyway
    return True



# Generated at 2022-06-13 06:05:14.092509
# Unit test for function write_changes
def test_write_changes():
    class FakeAnsibleModule:
        def __init__(self):
            self.fail_json = lambda: None
            self.run_command = lambda x: None
            self.atomic_move = lambda x, y, z: None
            self.tmpdir = '/tmp'
    assert write_changes(FakeAnsibleModule(),'some contents','/some/path') is None


# Generated at 2022-06-13 06:05:25.576780
# Unit test for function main
def test_main():
    import os
    os.system("printf 'test_test_test\n' > testfile")
    res_args = dict()
    res_args['msg'] = "test_test_test"
    res_args['changed'] = True

# Generated at 2022-06-13 06:05:35.620423
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import crypto as crypto_utils
    from ansible.module_utils._text import to_bytes
    import os
    import sys

    if not crypto_utils.pycrypto_ok:
        print('SKIPPING AS CRYPTOGRAPHY UNAVAILABLE')
        sys.exit()


# Generated at 2022-06-13 06:05:36.304709
# Unit test for function write_changes
def test_write_changes():
    pass


# Generated at 2022-06-13 06:05:43.923800
# Unit test for function check_file_attrs
def test_check_file_attrs():
    def mytest(test_args, test_result):
        temp_module = AnsibleModule(argument_spec={})
        temp_module.params = test_args
        temp_module.atomic_move = lambda x, y: None
        res_msg, res_changed = check_file_attrs(temp_module, True, "")
        assert (res_msg == test_result[0] and res_changed == test_result[1])
    myargs = dict(path="/foo", owner="root", group="root", mode="0644")
    mymsg, mychanged = "ownership, perms or SE linux context changed", True
    mytest(myargs, (mymsg, mychanged))

# Generated at 2022-06-13 06:05:57.230163
# Unit test for function main
def test_main():
    args = dict()

    set_module_args(args)
    main()

    # Basic test
    args['path'] = './tests/files/replace'
    args['regexp'] = 'item'
    args['replace'] = 'item2'
    args['backup'] = True

    set_module_args(args)
    main()

    # Test no backup
    args['path'] = './tests/files/replace'
    args['regexp'] = 'item'
    args['replace'] = 'item2'
    args['backup'] = False

    set_module_args(args)
    main()

    # Test after, before and after + before
    args['path'] = './tests/files/replace2'
    args['regexp'] = 'item'

# Generated at 2022-06-13 06:06:08.742877
# Unit test for function write_changes
def test_write_changes():
    module = MockModule()
    contents = 'old contents'
    path = '/path/to/file'
    write_changes(module, contents, path)
    assert module.params['unsafe_writes'] == False
    assert module.tmpdir == '/tmp'
    assert module.atomic_move.called
    assert module.atomic_move.call_args == call('/tmp/tmpPQoiaw', '/path/to/file', unsafe_writes=False)
    module.atomic_move.reset_mock()
    module.params['unsafe_writes'] = True
    write_changes(module, contents, path)
    assert module.atomic_move.called

# Generated at 2022-06-13 06:06:12.080994
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule({'owner': 'root'})
    message = ''
    changed = False

# Compares new and old content, returns changed and message

# Generated at 2022-06-13 06:06:17.391834
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    if __name__ == '__main__':
        basic._ANSIBLE_ARGS = ['test']
        main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:06:25.953236
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

    path = params['path']
    res

# Generated at 2022-06-13 06:08:25.176983
# Unit test for function write_changes
def test_write_changes():
    """
    Its a unit test for verify if the write of the changes is correct.
    :return:
    """



# Generated at 2022-06-13 06:08:27.391069
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # TODO: Test this
    pass
    return


# Generated at 2022-06-13 06:08:36.930051
# Unit test for function main
def test_main():
    return_msg = '''
  msg: ''
  changed: False
'''
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
    module.exit_json(msg='', changed=False)

# Generated at 2022-06-13 06:08:41.601536
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs(None, True, "message") == ('message and ownership, perms or SE linux context changed', True)
    assert check_file_attrs(None, False, "message") == ('ownership, perms or SE linux context changed', True)


# Generated at 2022-06-13 06:08:48.573184
# Unit test for function write_changes
def test_write_changes():
    class MockModule(object):
        def __init__(self):
            self.check_mode = False
            self.tmpdir = 'tmpdir'
            self.params= {}
        def fail_json(self, **kwargs):
            raise Exception(kwargs['msg'])
        def run_command(self, cmd):
            if cmd == '/bin/false tmpdir/tmpfile':
                return (1, '', '')
            elif cmd == '/bin/true tmpdir/tmpfile':
                return (0, '', '')
            else:
                raise Exception(cmd)
        def atomic_move(self, tmpfile, path, unsafe_writes):
            if unsafe_writes:
                return (1, '', '')
            else:
                return (0, '', '')
    f = tempfile.N

# Generated at 2022-06-13 06:08:50.281298
# Unit test for function write_changes
def test_write_changes():
    # code
    pass



# Generated at 2022-06-13 06:08:58.165326
# Unit test for function check_file_attrs
def test_check_file_attrs():

    # pretend module and one changed file
    # check that the right message is delivered
    # call the function and check result
    msg = "msg"
    module = MockModule()
    change = True
    result = check_file_attrs(module, change, msg)

    # test function result
    if not result[1]:
        raise AssertionError("Error: check_file_attrs: changed=False when it should be True")
    if result[0] != "msg and ownership, perms or SE linux context changed":
        raise AssertionError("Error: check_file_attrs: message wrong, got: %s" % result[0])

    # pretend module and one changed file
    # check that the right message is delivered
    change = False
    result = check_file_attrs(module, change, msg)

    # test

# Generated at 2022-06-13 06:08:59.344693
# Unit test for function write_changes
def test_write_changes():
    assert hasattr(write_changes, '__call__')


# Generated at 2022-06-13 06:09:03.564626
# Unit test for function check_file_attrs
def test_check_file_attrs():
    contents = "hello"
    p = module_args.copy()
    p.update(dict(
        path=tmpfile,
        encoding=None,
    ))

    module = AnsibleModule(
        argument_spec=p
    )    
    


# Generated at 2022-06-13 06:09:07.561901
# Unit test for function check_file_attrs
def test_check_file_attrs():
    changed = False
    message = ""
    module = AnsibleModule(argument_spec=dict())
    module.params["path"] = "/path/to/testfile"
    file_args = module.load_file_common_arguments(module.params)
    if file_args["owner"] != "root":
        changed = True
        message += "ownership changed"
    return message, changed
