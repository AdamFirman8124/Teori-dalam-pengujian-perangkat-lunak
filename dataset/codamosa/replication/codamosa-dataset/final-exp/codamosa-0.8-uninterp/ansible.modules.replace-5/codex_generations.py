

# Generated at 2022-06-13 05:59:51.885415
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
            regexp=dict(type='str', required=True),
            replace=dict(type='str', default=''),
            after=dict(type='str'),
            before=dict(type='str'),
            backup=dict(type='bool', default=False),
            validate=dict(type='str'),
        ),
        add_file_common_args=True,
        supports_check_mode=True
    )
    try:
        import __main__ as main
    except ImportError:
        main = sys.modules['__main__']
    main.ANSIBLE_MODULE_ARGS = ""
    main.ANSIBLE_MODULE_RETVALS = "0"
    main.ANSIBLE_

# Generated at 2022-06-13 06:00:04.545051
# Unit test for function main
def test_main():
    args = dict(
    path=dict(type='path', required=True, aliases=['dest', 'destfile', 'name']),
    regexp=dict(type='str', required=True),
    replace=dict(type='str', default=''),
    after=dict(type='str'),
    before=dict(type='str'),
    backup=dict(type='bool', default=False),
    validate=dict(type='str'),
    encoding=dict(type='str', default='utf-8'),
    )
    module = AnsibleModule(
        argument_spec=args,
        add_file_common_args=True,
        supports_check_mode=True,
    )
    params = module.params
    path = params['path']
    encoding = params['encoding']
    res_args = dict()

   

# Generated at 2022-06-13 06:00:09.159709
# Unit test for function main
def test_main():
    from ansible.modules.files.replace import main
    fd, path = tempfile.mkstemp()
    with open(path, 'w') as f:
        f.write('abc')
    m = AnsibleModule(
        argument_spec = dict(
            path = dict(type = 'path', required = True, aliases = ['dest', 'destfile', 'name']),
            regexp = dict(type='str', required=True),
            replace = dict(type='str', default=''),
            backup = dict(type='bool', default=False),
            encoding = dict(type='str', default='utf-8'),
        ),
        add_file_common_args = True,
        supports_check_mode = True,
    )
    m.params['path'] = path

# Generated at 2022-06-13 06:00:17.249860
# Unit test for function check_file_attrs
def test_check_file_attrs():

    tmpfile = tempfile.mkstemp()
    module = AnsibleModule(
        argument_spec=dict(
            content=dict(default="test"),
            path=dict(default=tmpfile[1]),
            owner=dict(default='root'),
            group=dict(default='root'),
            mode=dict(default='0644'),
            unsafe_writes=dict(default=False, type='bool'),
        ),
        supports_check_mode=True
    )
    changed = False
    message = "Message"
    return_message, return_changed = check_file_attrs(module, changed, message)
    assert return_changed == changed
    assert return_message == message
    module.exit_json(changed=changed, msg=message)



# Generated at 2022-06-13 06:00:19.083358
# Unit test for function main
def test_main():
    from ansible_collections.testns.testcollection.plugins.module_utils.ansible_module_replace import test_main

    test_main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:00:24.968711
# Unit test for function main
def test_main():
    args = dict(
        regexp='^(ListenAddress[ ]+)[^\n]+$',
        replace='\g<1>0.0.0.0',
        path='./test.txt'
    )
    result = dict(
        changed=True,
        after='\g<1>0.0.0.0\n',
        before='ListenAddress 127.0.0.1\n'
    )
    with open('./test.txt','w') as f:
        f.write(result['before'])
    main(args,result)
    with open('./test.txt','r') as f:
        assert result['after'] == f.read()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:00:28.551225
# Unit test for function check_file_attrs
def test_check_file_attrs():
    args = {}
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    _, changed = check_file_attrs(module, False, "message")
    assert not changed
    assert not module.check_mode


# Generated at 2022-06-13 06:00:30.382212
# Unit test for function write_changes
def test_write_changes():
    """
    Test function for function write_changes
    """
    pass


# Generated at 2022-06-13 06:00:40.368277
# Unit test for function main
def test_main():
    s = [u'\n', u'#foo bar', u'http://ansible.com/', u'[foo]',
         u'bar=baz', u'roger=dodger', u'\n', u'# foo bar',
         u'http://example.com/', u'[foo]', u'bar=baz',
         u'roger=dodger', u'\n', u'# foo bar\n', u'[foo]\n',
         u'bar=baz\n', u'roger=dodger\n']


# Generated at 2022-06-13 06:00:52.820012
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={'unsafe_writes': {'type': 'bool', 'required': True, 'default': False}})
    # Handle case where os.fdopen is mocked
    module.atomic_move = lambda x, y, **kwargs: None
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
    os.fdopen(tmpfd, 'wb').close()
    path = 'dest_file'
    module.run_command = lambda x: (0, '', '')
    write_changes(module, 'test', path)

    module.run_command = lambda x: (1, '', '')
    try:
        write_changes(module, 'test', path)
    except Exception:
        pass

# Generated at 2022-06-13 06:01:08.793781
# Unit test for function main
def test_main():
    pass


# import module snippets
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:01:14.508721
# Unit test for function main
def test_main():
    '''
    Function to test the main function with different inputs
    '''
    src_path = os.path.realpath(__file__)
    src_dir = os.path.dirname(src_path)
    test_dir = os.path.join(src_dir, 'test_ansible_replace')
    if os.path.exists(test_dir):
      shutil.rmtree(test_dir)

    print('[INFO] Creating a test directory '+test_dir)
    os.mkdir(test_dir)
    os.chdir(test_dir)
    print('[INFO] Testing for valid input')
    path='sample.txt'
    file_sample=open("sample.txt", "w")

# Generated at 2022-06-13 06:01:16.060013
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert False, 'TODO: Unit test for check_file_attrs'



# Generated at 2022-06-13 06:01:25.180390
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
    module.params['path'] = '/etc/hosts'

# Generated at 2022-06-13 06:01:33.187866
# Unit test for function check_file_attrs
def test_check_file_attrs():

    module = AnsibleModule(argument_spec={})
    current = dict(path='/file/path', state='file', mode='0644')
    module.params = dict(path='/file/path', state='file', mode='0755', *current.items())

    changed = False
    message = 'changed'
    message, changed = check_file_attrs(module, changed, message)

    assert changed == True
    assert message == "changed and ownership, perms or SE linux context changed"



# Generated at 2022-06-13 06:01:34.179298
# Unit test for function check_file_attrs
def test_check_file_attrs():
    pass
# END MOCK test



# Generated at 2022-06-13 06:01:38.198597
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({})
    path = '/tmp/something'
    contents = 'a'*100
    write_changes(module, contents, path)
    assert os.path.exists(path) and open(path, 'rb').read() == contents



# Generated at 2022-06-13 06:01:45.181462
# Unit test for function main
def test_main():
    # create a mock module
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

    # create a mock object
    class MockContents():
        encoding=  "utf-8"
    # the module input parameters
    path

# Generated at 2022-06-13 06:01:55.381072
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={
        'path': {'type': 'str', 'required': True},
        'validate': {'type': 'str', 'default': None},
        'unsafe_writes': {'type': 'bool', 'default': False}
    })
    contents = "contents"
    path = "path"
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
    f = os.fdopen(tmpfd, 'wb')
    f.write(contents)
    f.close()

    validate = None
    valid = True
    module.atomic_move(tmpfile, path)



# Generated at 2022-06-13 06:02:02.172535
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({}, {}, [])
    file_args = module.load_file_common_arguments(module.params)
    changed, message = False, ''
    test_changed, test_message = check_file_attrs(module, changed, message)
    assert test_changed is False
    assert test_message == message


# Generated at 2022-06-13 06:02:25.912791
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec = dict(
            validate = dict(required=False, type='str', default=None),
            path = dict(required=True, type='str'),
            contents = dict(required=True, type='bytes')
        )
    )
    contents = b'Contents of test file'
    test_file = '/tmp/test_write_changes'
    write_changes(module, contents, test_file)
    f = open(test_file, 'rb')
    assert f.read() == contents
    f.close()
    os.remove(test_file)


# Generated at 2022-06-13 06:02:29.572593
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule()
    test = write_changes(module, b'abc', '/a/b/c')
    assert test == None, "test_write_changes() should return None"


# Generated at 2022-06-13 06:02:36.272116
# Unit test for function check_file_attrs

# Generated at 2022-06-13 06:02:43.599196
# Unit test for function check_file_attrs
def test_check_file_attrs():
    args = dict(remote_src=True,
                mode=None,
                owner="root",
                group="root",
                seuser="role",
                serole="role")
    module = AnsibleModule(argument_spec=args)
    changed, message = False, ""
    (message_return, changed_return) = check_file_attrs(module, changed, message)
    assert message == ""
    assert changed == False
    assert isinstance(changed_return, bool)
    assert isinstance(message_return, str)




# Generated at 2022-06-13 06:02:48.220679
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule({})
    message = 'foo'
    changed = True

    result = check_file_attrs(module, changed, message)
    assert result == ('foo and ownership, perms or SE linux context changed', True), result



# Generated at 2022-06-13 06:02:57.374892
# Unit test for function check_file_attrs
def test_check_file_attrs():  # pylint: disable=missing-docstring
    from ansible.compat.tests.mock import patch

    class FakeModule(object):

        def __init__(self):
            self.atomic_move = lambda *a, **k: None
            self.fail_json = lambda *a, **k: None
            self.load_file_common_arguments = lambda *a, **k: {}
            self.params = {'unsafe_writes': False}

        def set_file_attributes_if_different(self, file_args, changed):
            return True

    module = FakeModule()
    return check_file_attrs(module, False, "")



# Generated at 2022-06-13 06:03:07.347722
# Unit test for function write_changes
def test_write_changes():
    in_contents = b'original contents of file'
    out_contents = b'updated contents of file'
    path = '/test/file/path'

    class Module:
        def __init__(self, params):
            self.params = params
            self.tmpdir = '/test/tmpdir'

        def fail_json(self, msg):
            raise Exception(msg)

        def run_command(self, cmd):
            if cmd == '/test/validator %s' % path:
                return (0, b'', b'')
            else:
                return (1, b'', b'')

        def atomic_move(self, src, dest, unsafe_writes=False):
            assert src.startswith(self.tmpdir)
            assert dest == path
            assert not unsafe_writes

# Generated at 2022-06-13 06:03:18.284271
# Unit test for function check_file_attrs

# Generated at 2022-06-13 06:03:24.252809
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class MockModule():
        def load_file_common_arguments(self, params):
            return {}

        def set_file_attributes_if_different(self, args, changed):
            return True, changed

    module = MockModule()
    changed, msg = False, "msg"
    try:
        msg, changed = check_file_attrs(module, changed, msg)
    except:
        pass
    assert changed



# Generated at 2022-06-13 06:03:35.054035
# Unit test for function write_changes
def test_write_changes():
    from ansible.module_utils import basic

    module = basic.AnsibleModule(argument_spec={
        'tmpdir': dict(type='path', default='/tmp'),
        'unsafe_writes': dict(type='bool', default=False),
        'validate': dict(type='str'),
    })

    path = "/tmp/foo.txt"
    contents = b"blah\r\n"

    tmpfile = "/tmp/ansible_replace_tmp_file.tmp"
    f = open(path, "w")
    f.write("foo\n")
    f.close()

    write_changes(module, contents, path)
    assert os.path.exists(path)
    assert not os.path.exists(tmpfile)

# Generated at 2022-06-13 06:04:09.834105
# Unit test for function main
def test_main():
    try:
        import ansible.modules.files.ansible.builtin.replace
    except ImportError:
        # We don't have ansible modules available, so we simply
        # mock AnsibleModule
        import sys
        from contextlib import contextmanager
        from StringIO import StringIO

        @contextmanager
        def mock_streams():
            old_stdout, old_stderr = sys.stdout, sys.stderr
            sys.stdout = sys.stderr = StringIO()
            try:
                yield sys.stdout, sys.stderr
            finally:
                sys.stdout, sys.stderr = old_stdout, old_stderr


# Generated at 2022-06-13 06:04:22.340319
# Unit test for function write_changes
def test_write_changes():
    # create a tempfile
    tmpfile, contents_before = tempfile.mkstemp()
    contents_after = contents_before + '.after'

    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
            after=dict(type='str'),
            before=dict(type='str'),
            backup=dict(type='bool', default=False),
            regexp=dict(type='str', required=True),
            replace=dict(type='str', default=''),
            validate=dict(type='str'),
        ),
        supports_check_mode=True,
    )
    module.params['path'] = tmpfile
    write_changes(module, contents_after, tmpfile)

    assert contents_after == open(tmpfile, 'rb').read()
   

# Generated at 2022-06-13 06:04:27.684248
# Unit test for function write_changes
def test_write_changes():
    tmpfd, tmpfile = tempfile.mkstemp()
    f = os.fdopen(tmpfd, 'wb')
    f.write(contents)
    f.close()
    module = AnsibleModule()
    module.atomic_move(tmpfile, path, unsafe_writes=module.params['unsafe_writes'])


# Generated at 2022-06-13 06:04:32.590499
# Unit test for function write_changes
def test_write_changes():
    tmpfile = '/tmp/test_write_changes'
    contents = b'contents'
    f = open(tmpfile, 'wb')
    f.write(contents)
    f.close()
    write_changes(module, '/tmp/test_write_changes')
    assert open(f, 'r').read() == contents



# Generated at 2022-06-13 06:04:39.281540
# Unit test for function write_changes
def test_write_changes():
    contents = to_bytes('changed_contents')
    path='/data/server.conf'
    tmp_file= tempfile.NamedTemporaryFile(suffix='.conf', dir='/tmp', delete=False)
    tmp_file.write(contents)
    tmpfile = tmp_file.name
    validate = 'cat '+ tmpfile +'| grep -E "^[a-zA-Z0-9]+$"'
    module = AnsibleModule({
        'backup': True,
        'validate': validate,
        'unsafe_writes': True,
        'tmpdir': '/tmp'
    })
    write_changes(module,contents,path)
    with open(path,'r') as infile, open(tmpfile,'r') as temp:
        orig_file_contents = infile

# Generated at 2022-06-13 06:04:49.322484
# Unit test for function main
def test_main():
    import os
    import sys
    import shutil
    import tempfile
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 06:04:57.124397
# Unit test for function check_file_attrs
def test_check_file_attrs():
    test_module = dict(
        set_file_attributes_if_different=lambda a, b: True,
        tmpdir='',
        fail_json=lambda a:None,
        atomic_move=lambda a, b, c:None,
        load_file_common_arguments=lambda a: dict(),
        params=dict()
    )
    assert ('ownership, perms or SE linux context changed', True) == check_file_attrs(test_module, False, "")
    assert ('test and ownership, perms or SE linux context changed', True) == check_file_attrs(test_module, True, "test")


# Generated at 2022-06-13 06:05:02.531417
# Unit test for function write_changes
def test_write_changes():
    """ Unittest for function write_changes """

    contents = "test contents"
    path = "/tmp/test_write_changes"
    module = AnsibleModule(argument_spec={})
    write_changes(module, contents, path)
    with open(path, 'r') as f:
        output = f.read()
    os.remove(path)
    assert output == contents


# Generated at 2022-06-13 06:05:07.465789
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
    os.path.realpath = MagicMock(return_value = "/root/test/unit.py")

# Generated at 2022-06-13 06:05:18.065946
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    import os

    # If path exists, remove it to make sure we do not have it
    b_path = to_bytes(path, errors='surrogate_or_strict')
    try:
        os.remove(b_path)
    except:
        pass
    with open(b_path, 'wb') as f:
        f.write(to_bytes(contents, errors='surrogate_or_strict', encoding='utf-8'))

    module_args = dict(
        path=path,
        regexp=regexp,
        replace=replace,
        backup=True
    )

# Generated at 2022-06-13 06:06:10.777629
# Unit test for function write_changes
def test_write_changes():

    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True, type='path'),
            regexp = dict(required=True, type='str'),
            replace = dict(required=True, type='str'),
            after = dict(required=True, type='str'),
            before = dict(required=True, type='str'),
            backup = dict(required=False, type='bool', default=False),
            others = dict(required=True, type='str'),
            encoding = dict(required=True, type='str', default='utf-8'),
            validate = dict(required=True, type='str'),
            unsafe_writes = dict(required=True, type='bool'),
            tmpdir = dict(required=True, type='str')
        )
    )

# Generated at 2022-06-13 06:06:21.546639
# Unit test for function write_changes
def test_write_changes():
    tmpdir = '/tmp/'
    # mock module
    module = AnsibleModule({'params': {'check_mode': False, 'unsafe_writes': False}}, tmpdir, 'WRITE')
    module.atomic_move = lambda src, dest: dest

    # test regular file
    write_changes(module, 'replace content', '/tmp/replace.txt')
    with open('/tmp/replace.txt', 'r') as f:
        assert 'replace content' == f.read()

    # test validate
    try:
        write_changes(module, 'replace content', '/tmp/replace.txt')
    except SystemExit as e:
        assert 'failed to validate' in str(e)


# Generated at 2022-06-13 06:06:23.273761
# Unit test for function main
def test_main():
  module = AnsibleModule(argument_spec_for_main())
  module.exit_json = exit_json
  main()


# Generated at 2022-06-13 06:06:31.790438
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.params['unsafe_writes'] = False
    file_args = {
        'path': '/path/to/file',
        'attribute_owner': 'root',
        'attribute_group': 'root',
        'attribute_mode': '0644'
    }
    module.set_file_attributes_if_different = Mock(return_value=True)
    message, changed = check_file_attrs(module, True, "my message")
    assert changed == True
    assert message == "my message and ownership, perms or SE linux context changed"
    assert module.set_file_attributes_if_different.call_count == 1

# Generated at 2022-06-13 06:06:44.354461
# Unit test for function write_changes
def test_write_changes():
    import pwd
    import grp
    import os

# Generated at 2022-06-13 06:06:52.087821
# Unit test for function main
def test_main():
    path = "some/path.yml"
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
    res_args = dict()
    res_args['msg'], res_args['changed'] = check_file_

# Generated at 2022-06-13 06:07:03.389519
# Unit test for function main
def test_main():
    """
    Let's test main function
    """
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
    module.tmpdir = os.path.dirname(os.path.realpath(__file__))
   

# Generated at 2022-06-13 06:07:10.311779
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.text.converters import to_bytes
    from ansible.module_utils.common.text.converters import to_text
    params = {
        u'path': u'/home/zhanghaoran/ansible_module_dev/ansible/ansible/1_module_os_replace/tmp/test',
        u'regexp': u'^#(.+)$',
        u'replace': u'"#"',
        u'backup': False,
        u'encoding': u'utf-8',
        u'unsafe_writes': True
    }
    check_mode = False

    # Module "builtin" is deprecated
    # module = AnsibleModule(argument_spec=module_args, check_invalid_

# Generated at 2022-06-13 06:07:14.184449
# Unit test for function write_changes
def test_write_changes():
    with tempfile.NamedTemporaryFile() as tmpfd:
        contents = "This should be replaced"
        path = tmpfd.name
        validate = None
        module = AnsibleModule(argument_spec={'path': {'type': 'path'}, 'validate': {'type': 'str'}, 'unsafe_writes': {'type': 'bool', 'default': True}})
        write_changes(module, contents, path)
        with open(path) as f:
            if f.read() != contents:
                assert False, "File not written correctly"
        tmpfd.close()
# End unit test



# Generated at 2022-06-13 06:07:20.141423
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={})
    module.params = {'path': '/path/to/file', 'unsafe_writes': True}
    module.set_file_attributes_if_different = lambda x, y: True
    changed, message = False, "message"
    result = check_file_attrs(module, changed, message)
    assert result == ('message and ownership, perms or SE linux context changed', True)
    # Error case
    module.set_file_attributes_if_different = lambda x, y: False
    changed, message = False, "message"
    result = check_file_attrs(module, changed, message)
    assert result == ('message', False)

