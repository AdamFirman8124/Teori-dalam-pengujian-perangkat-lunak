

# Generated at 2022-06-13 05:59:51.689239
# Unit test for function check_file_attrs
def test_check_file_attrs():

    old_args = {
        'content': '# comment1\n# comment2',
        'path': '/tmp/test-file',
        'backup': 'yes',
        'unsafe_writes': True,
        'follow': False,
        'show_diff': False,
        'check_mode': True,
        'encoding': 'utf-8',
        'other_attributes': None
    }


# Generated at 2022-06-13 05:59:59.441533
# Unit test for function write_changes
def test_write_changes():
    contents = "[apache2]\nlisten_port = 8080\n"
    path = "/tmp/test_write_changes"
    module = AnsibleModule(
        argument_spec=dict(
            unsafe_writes=dict(type="bool", default="no")
        )
    )
    write_changes(module, contents, path)
    assert os.path.exists(path)
    assert open(path).read() == contents


# Generated at 2022-06-13 06:00:09.306269
# Unit test for function check_file_attrs
def test_check_file_attrs():
    test_module = AnsibleModule({'path': "/foo/bar", 'owner': "baz"})
    test_module.set_file_attributes_if_different = MagicMock()
    set_file_attributes_if_different_return = (True, {})
    test_module.set_file_attributes_if_different.return_value = set_file_attributes_if_different_return
    test_module._diff_peek = MagicMock()
    test_module._diff_peek.return_value = True
    test_changed = True
    test_message = "test message"
    test_result_message, test_result_changed = check_file_attrs(test_module, test_changed, test_message)

# Generated at 2022-06-13 06:00:15.114200
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


# Generated at 2022-06-13 06:00:24.089836
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec=dict())
    path = tempfile.mkdtemp()
    contents_orig = "this is a test"
    contents_new = "this is a test\nthis is another test"
    path_file = path + "/test.txt"
    f = open(path_file, 'wb')
    f.write(contents_orig)
    f.close()
    # test validate = None
    write_changes(module, contents_new, path_file)
    f = open(path_file, 'r')
    contents = f.read()
    if contents != contents_new:
        module.fail_json(msg="Failed to write new contents: %s" % contents_new)
    f.close()
    # test validate = "cat %s"

# Generated at 2022-06-13 06:00:34.611229
# Unit test for function main

# Generated at 2022-06-13 06:00:43.236291
# Unit test for function check_file_attrs
def test_check_file_attrs():

    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='path', required=True),
            regexp=dict(type='str'),
            replace=dict(type='str'),
            after=dict(type='str'),
            before=dict(type='str'),
            backup=dict(type='bool', default=False),
            encoding=dict(type='str', default='utf-8'),
            unsafe_writes=dict(type='bool', default=False),
        ),
    )
    path = module.params['path']
    regexp = module.params['regexp']
    replace = module.params['replace']
    after = module.params['after']
    before = module.params['before']
    encoding = module.params['encoding']
    changed = False
    message = ''

   

# Generated at 2022-06-13 06:00:54.921638
# Unit test for function main
def test_main():
    # Mock
    class ModuleMock:
        def __init__(self, **kwargs):
            self.params = kwargs
            self.fail_json = lambda message: quit()
            self.exit_json = lambda **kwargs: quit()
            self.run_command = lambda command: [0, '', '']
            self.tmpdir = ''
            self.atomic_move = lambda src, dst, unsafe_writes: quit()
            self.set_file_attributes_if_different = lambda file_args, changed: quit()
            self.backup_local = lambda path: ''
            self.load_file_common_arguments = lambda params: {}


        def fail_json(self, **kwargs):
            quit()

        def exit_json(self, **kwargs):
            quit()


    module

# Generated at 2022-06-13 06:00:56.370441
# Unit test for function main
def test_main():
    assert True
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:01:05.109631
# Unit test for function write_changes
def test_write_changes():
    import tempfile
    from ansible.module_utils.basic import AnsibleModule
    test_contents = 'this is a test'
    (fd, test_path) = tempfile.mkstemp()
    f = os.fdopen(fd, 'wb')
    f.write(test_contents)
    f.close()
    test_module = AnsibleModule(argument_spec=dict())
    test_module.atomic_move = lambda src, dest: True
    test_module.params = {}
    test_module.params['unsafe_writes'] = False
    write_changes(test_module, to_bytes(test_contents + '\r\n'), test_path)

# Generated at 2022-06-13 06:01:27.178153
# Unit test for function main
def test_main():
    # Create a test module
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
    # Set up module input parameters

# Generated at 2022-06-13 06:01:37.989696
# Unit test for function check_file_attrs
def test_check_file_attrs():

    path = "/test/path"
    module_params = {
        'owner': 'me',
        'group': 'me',
        'mode': '0755',
        'unsafe_writes': False
    }
    module = AnsibleModule(argument_spec={})
    module.params = module_params
    module.check_mode = True

    # Test file exists
    os.makedirs(os.path.dirname(path))
    file = open(path, "w")
    os.chown(path, 0, 0)
    os.chmod(path, 0000)
    changed = False
    message = ""

    module._diff_files = False
    message, changed = check_file_attrs(module, changed, message)
    assert message == "ownership, perms or SE linux context changed"
   

# Generated at 2022-06-13 06:01:46.893290
# Unit test for function main
def test_main():
    """
        Test the main function, this should return good stuff
    """
    # This is a unit test, don't reach out to the internet
    utils.REACHABLE_SVCS = []

    # The params we will pass to the module, used for all tests
    module_params = {
        "path": "/etc/foo.conf",
        "regexp": "(\s+)old\.host\.name(\s+.*)?$",
        "replace": "\1new.host.name\2",
    }

    # The test wants this module to exit, just like Ansible
    # Would do so, it is required for the unit test
    sys.exit = lambda x: None

    # This will create an instance of the AnsibleModule class

# Generated at 2022-06-13 06:01:49.388716
# Unit test for function main
def test_main():
    main()


# import module snippets
from ansible.module_utils.basic import *

main()

# Generated at 2022-06-13 06:01:57.576011
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({'tmpdir': '/tmp', 'validate': None})
    test_input = '{"input_1": ["foo", "bar"]}'
    test_input_bytes = to_bytes(test_input, errors='surrogate_or_strict')
    test_output = '/tmp/test_output'
    create_dir(test_output)
    contents = to_bytes(test_input, errors='surrogate_or_strict')
    path = test_output
    write_changes(module, contents, path)
    assert isequal(test_input, path)


# Generated at 2022-06-13 06:02:08.984963
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(type='str', required=True),
            contents = dict(type='str', required=True),
            validate = dict(type='str')
        ),
        supports_check_mode=True
    )

    module.run_command = lambda *args, **kwargs: (0, '', '')
    module.atomic_move = lambda a, b, c: (a, b)
    module.tmpdir = '/tmp/'
    path = '/tmp/test_file'

    results = write_changes(module, 'test_contents', path)
    assert results == (path, path)



# Generated at 2022-06-13 06:02:15.880312
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec = {})
    contents = "updated contents"
    path = "example_path"
    module.atomic_move = mock_move
    module.run_command = mock_run_command
    write_changes(module, contents, path)

    rc, out, err = module.run_command.call_args[0]
    assert rc == 0
    assert out == b"validate output"
    assert err == b"validate error"
    new_path, old_path, unsafe_writes = module.atomic_move.call_args[0]
    assert new_path == path
    assert old_path == path
    assert unsafe_writes == False

# unit test for function run_command

# Generated at 2022-06-13 06:02:19.492659
# Unit test for function main
def test_main():
    pass #TODO: This is a stub.

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:02:26.503548
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={})
    msg, changed = check_file_attrs(module, False, 'test_message')
    assert msg == 'test_message and ownership, perms or SE linux context changed'
    assert changed
    msg, changed = check_file_attrs(module, True, 'test_message')
    assert msg == 'test_message and ownership, perms or SE linux context changed'
    assert changed
    path = tempfile.mkstemp()
    os.close(path[0])
    file_args = {'dest': path[1]}
    result = module.set_file_attributes_if_different(file_args, False)
    assert not result


# Generated at 2022-06-13 06:02:34.276008
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.module_utils._text import to_bytes
    from ansible.compat.tests import unittest
    from ansible.compat.tests.mock import patch


# Generated at 2022-06-13 06:03:03.494959
# Unit test for function write_changes
def test_write_changes():
    contents = '''
ListenAddress 1.2.3.4
ListenAddress 5.6.7.8
'''
    tmpfd, tmpfile = tempfile.mkstemp(dir='/tmp')
    f = os.fdopen(tmpfd, 'wb')
    f.write(contents)
    f.close()

    valid = True

# Generated at 2022-06-13 06:03:07.872228
# Unit test for function write_changes
def test_write_changes():
    test_module_args = {
        'path': '/tmp/testfile',
        'unsafe_writes': False,
    }
    module = AnsibleModule(**test_module_args)
    file_contents = "this is a test"
    write_changes(module, file_contents, test_module_args['path'])
    with open(test_module_args['path'], 'r') as test_file:
        assert test_module_args['path'] == test_module_args['path']
        assert test_file.read() == file_contents
    os.remove(test_module_args['path'])



# Generated at 2022-06-13 06:03:14.292684
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({'tmpdir': 'testdir/'})
    path = 'testdir/toto'
    contents = b'1234567890'
    write_changes(module, contents, path)
    assert os.path.isfile(path)
    f = open(path, 'rb')
    assert f.read() == contents
    os.remove(path)


# Generated at 2022-06-13 06:03:20.422833
# Unit test for function check_file_attrs
def test_check_file_attrs():
    testmodule = MockAnsibleModule()

    testmodule.set_file_attributes_if_different = Mock(return_value=True)
    testmodule.load_file_common_arguments = Mock(return_value=True)

    module = AnsibleModule(
        argument_spec = dict(
            ansible_module_args
        )
    )
    assert module.check_file_attrs(module, True, 'message') == ('message and ownership, perms or SE linux context changed', True)
    assert module.check_file_attrs(module, False, 'message') == ('ownership, perms or SE linux context changed', True)



# Generated at 2022-06-13 06:03:25.325570
# Unit test for function main
def test_main():
	universal_newlines = False
	def run_command(self, cmd, tmpfile=None, environ_update=None, check_rc=False, data=None, binary_data=False, path_prefix=None, cwd=None, use_unsafe_shell=False, prompt_regex=None, environ=None):
		cwd = None
		if check_rc:
			rc, out, err = 0, '', ''
			return rc, out, err
		else:
			rc, out, err = 0, '', ''
			return rc, out, err
			pass
		pass
	def _debug(self, msg, prefix=''):
		pass
	AnsibleModule.run_command = run_command
	AnsibleModule._debug = _

# Generated at 2022-06-13 06:03:36.000216
# Unit test for function write_changes
def test_write_changes():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils.six import StringIO
    from ansible.module_utils.six import b
    from ansible.module_utils._text import to_bytes
    import tempfile
    import os
    import sys

    # Create an ansible module
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(required=True),
            validate = dict(type='str'),
            contents = dict(required=True)
        )
    )
    module.tmpdir = tempfile.mkdtemp()
    captured = StringIO()
    sys.stdout = captured

# Generated at 2022-06-13 06:03:47.211435
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_native
    from ansible.module_utils.pycompat24 import get_exception
    import os
    import sys
    import subprocess
    import tempfile
    import shutil
    from Queue import Queue
    from threading import Thread

    def _exec(cmd, sudoable=False):
        """ghetto exec method"""
        p = subprocess.Popen(cmd, shell=isinstance(cmd, basestring),
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        return (p.returncode, cmd, stdout, stderr)

   

# Generated at 2022-06-13 06:03:48.624579
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs(module, changed, message) == message, changed



# Generated at 2022-06-13 06:04:01.256279
# Unit test for function check_file_attrs
def test_check_file_attrs():

    class TestModule(object):
        def __init__(self):
            self.params = {
                'path': '/etc/ansible/tmp',
                'owner': 'ansible',
                'group': 'ansible',
                'mode': '0644',
            }

        def fail_json(self, msg):
            raise Exception(msg)

        def set_file_attributes_if_different(self, file_args, changed):
            return True

        def load_file_common_arguments(self, params):
            return file_args

    class MockActionModule(object):
        def __init__(self):
            self.tmpdir = None
            self.params = {}
            self.check_mode = False
            self.atomic_move = False

    module = TestModule()
    action = MockActionModule()



# Generated at 2022-06-13 06:04:10.143492
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
    isinstance(main(), AnsibleModule)
    
# Standard Unit test execution

# Generated at 2022-06-13 06:05:05.049450
# Unit test for function check_file_attrs
def test_check_file_attrs():
    path = "/tmp/test.txt"
    module = MockModule(params=dict(path=path, owner='root', group='root', mode='0644', seuser=None, serole=None, setype=None, selevel=None))
    module.run_command = Mock(return_value=0)
    module.load_file_common_arguments = Mock(return_value=dict(path=path, owner='root', group='root', mode='0644', seuser=None, serole=None, setype=None, selevel=None))
    module.set_file_attributes_if_different = Mock(return_value=True)
    changed = False
    message = ""
    message, changed = check_file_attrs(module, changed, message)

# Generated at 2022-06-13 06:05:11.996183
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # Mock module and message
    import collections
    class MockedModule:
        set_file_attributes_if_different = lambda self, args: True
    mocked_module = MockedModule()
    message = "test"
    # Expected result
    expected = ("test and ownership, perms or SE linux context changed", True)

    # Call function and check result
    result = check_file_attrs(mocked_module, False, message)
    assert isinstance(result, collections.Sequence)
    assert result == expected



# Generated at 2022-06-13 06:05:20.107411
# Unit test for function check_file_attrs
def test_check_file_attrs():
    test_module = {
        'set_file_attributes_if_different':
            lambda file_args, no_follow: (True, "changed")
    }

    result = check_file_attrs(test_module, False, "")
    assert result == ("changed", True), "Result was %s" % result

    result = check_file_attrs(test_module, True, "fake message")
    assert result == ("fake message and changed", True), "Result was %s" % result



# Generated at 2022-06-13 06:05:29.909194
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.module_utils.basic import AnsibleModule
    import time
    args_dict = {
        'path': '/tmp/foo',
        'owner': 'root',
        'group': 'root',
        'mode': '600',
        'unsafe_writes': 'yes',
    }
    m = AnsibleModule(argument_spec={}, supports_check_mode=True)
    m.params.update(args_dict)
    changed_message, changed = check_file_attrs(m, True, "test")
    assert changed
    assert "ownership" in changed_message or "perms" in changed_message or "SE linux context" in changed_message



# Generated at 2022-06-13 06:05:30.610077
# Unit test for function main
def test_main():
    assert 1 == 2

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:05:38.666207
# Unit test for function write_changes
def test_write_changes():
    # Create a file with fake contents
    contents = '# contents of test file\n'
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
    f = os.fdopen(tmpfd, 'wb')
    f.write(contents)
    f.close()
    # Run the function
    path = tmpfile
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
    f = os.fdopen(tmpfd, 'wb')
    f.write('this is the input file to test against')
    f.close()
    contents = open(tmpfile, 'rb').read()
    #
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
    f = os.fdopen(tmpfd, 'wb')
   

# Generated at 2022-06-13 06:05:53.328385
# Unit test for function check_file_attrs

# Generated at 2022-06-13 06:06:01.972013
# Unit test for function check_file_attrs
def test_check_file_attrs():
    class TestMod(object):
        def __init__(self):
            self.params = dict(
                path='',
                owner='',
                group='',
                mode='',
                seuser='',
                serole='',
                setype='',
                selevel=''
                )
            self.tmpdir = ''
        def set_file_attributes_if_different(self, file_args, changed):
            return changed
        def load_file_common_arguments(self, params):
            return []
    testobj = TestMod()

    testobj.params['owner'] = 'user'
    testobj.changed = False
    testobj.msg = ''
    testobj.changed, testobj.msg = check_file_attrs(testobj, testobj.changed, testobj.msg)
    assert testobj

# Generated at 2022-06-13 06:06:02.629665
# Unit test for function write_changes
def test_write_changes():
    return True


# Generated at 2022-06-13 06:06:12.036523
# Unit test for function main
def test_main():
    import tempfile
    import shutil

    tmpdir = tempfile.mkdtemp()
    path = os.path.join(tmpdir, 'test')

    open(path, 'a').close()

# Generated at 2022-06-13 06:08:12.361609
# Unit test for function write_changes
def test_write_changes():
    pass



# Generated at 2022-06-13 06:08:21.379791
# Unit test for function main
def test_main():
    test_path = os.path.dirname(os.path.realpath(__file__))
    fixture = os.path.join(test_path, 'default_tests.yml')
    os.environ['ANSIBLE_INVENTORY'] = os.path.join(test_path, 'inventory.ini')
    os.chdir(test_path)

# Generated at 2022-06-13 06:08:33.328763
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common._collections_compat import Mapping


# Generated at 2022-06-13 06:08:44.627029
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # Test file loaded as str
    modstr = AnsibleModule(argument_spec={'path':{'type':'str'},'mode':{'type':'str'},'owner':{'type':'str'},'group':{'type':'str'},'unsafe_writes':{'type':'bool'}})
    modstr.params = {'path':'/tmp/test_replace.txt', 'mode':'0777', 'owner':'root', 'group':'root', 'unsafe_writes':False}
    modstr.load_file_common_arguments = lambda x: {'path': '/tmp/test_replace.txt'}
    modstr.set_file_attributes_if_different = lambda x, y: True
    modstr.params['follow'] = True
    changed = False
   

# Generated at 2022-06-13 06:08:54.688043
# Unit test for function check_file_attrs
def test_check_file_attrs():
# doc_check_file_attrs
    import ansible.module_utils.basic
    main_arg_spec = dict(
        path=dict(),
        regexp=dict(required=True),
        replace=dict(),
        encoding=dict(default='utf-8'),
        unsafe_writes=dict(default=False, type='bool')
    )
    module_args = dict(
        regexp = r'\b(localhost)(\d*)\b',
        replace = r'\1\2.localdomain\2 \1\2',
        path = "/tmp/test_check_file_attrs"
    )

    def set_file_attributes_if_different(self, file_args, changed):
        return True


# Generated at 2022-06-13 06:09:06.206403
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec=dict({}))
    changed = True

    # stub module funcs
    class module_funcs:
        def __init__(*args, **kwargs):
            self.params = {}
        def fail_json(*args, **kwargs):
            pass
        def atomic_move(*args, **kwargs):
            pass

        def set_file_attributes_if_different(*args, **kwargs):
            return True

        def load_file_common_arguments(*args, **kwargs):
            return {}

    module.atomic_move = module_funcs.atomic_move
    module.fail_json = module_funcs.fail_json
    module.set_file_attributes_if_different = module_funcs.set_file_attributes_if_different

# Generated at 2022-06-13 06:09:11.842732
# Unit test for function main
def test_main():
    content = """
listen_addresses = '*'

[1]
test
test2
"""
    content_in_bytes = content.encode('utf-8')

# Generated at 2022-06-13 06:09:16.627093
# Unit test for function main
def test_main():
    # From Ansible 2.9, we can only test with required args.
    # The function was previously tested with all args in Ansible 2.8. 
    data = dict(
        path='/test/path',
        regexp='/test/regexp',
        backup=False,
        encoding='utf-8'
    )


# Generated at 2022-06-13 06:09:26.729808
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