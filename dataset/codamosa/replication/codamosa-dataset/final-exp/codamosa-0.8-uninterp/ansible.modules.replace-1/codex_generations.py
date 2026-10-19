

# Generated at 2022-06-13 05:59:52.432958
# Unit test for function main
def test_main():
  from ansible.module_utils import basic
  from ansible.module_utils._text import to_bytes
  m = AnsibleModule(argument_spec={'path':{'type':'path', 'required':True}, 'regexp':{'type':'str', 'required':True}, 'replace':{'type':'str', 'default':''}, 'backup':{'type':'bool', 'default':False, 'const':True, 'aliases':['__backup__']}, '__backup__':{'type':'bool', 'default':False, 'const':True, 'aliases':['backup']}, 'validate':{'type':'str'}, 'encoding':{'type':'str', 'default':'utf-8'}}, add_file_common_args=True, supports_check_mode=True)

# Generated at 2022-06-13 05:59:53.957368
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs(module, changed, message) is not None


# Generated at 2022-06-13 06:00:06.056551
# Unit test for function write_changes
def test_write_changes():
    class TmpFile:
        def __init__(self):
            self._inputs = []

        def write(self, buf):
            self._inputs.append(buf)

        def close(self):
            pass

    # Mock up module.atomic_move to capture inputs
    inputs = []
    def atomic_move(source, dest, **kwargs):
        inputs.append((source, dest))

    # Mock up module.run_command to always return success
    def run_command(cmd):
        return (0, "", "")

    # build module to test
    module = AnsibleModule(argument_spec={
            'path': {'type': 'str', 'required': True},
            'validate': {'type': 'str', 'required': False}
        }, supports_check_mode=True)
    module.atomic

# Generated at 2022-06-13 06:00:13.190352
# Unit test for function main
def test_main():
    module = AnsibleModule( argument_spec=dict( path=dict( type='path', required=True, aliases=[ u'dest', u'destfile', u'name' ] ), regexp=dict( type='str', required=True ), replace=dict( type='str', default='' ), after=dict( type='str' ), before=dict( type='str' ), backup=dict( type='bool', default=False ), validate=dict( type='str' ), encoding=dict( type='str', default=u'utf-8' ), ), add_file_common_args=True, supports_check_mode=True )

    params = module.params
    path = params['path']
    encoding = params['encoding']
    res_args = dict()


# Generated at 2022-06-13 06:00:20.208042
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module = AnsibleModule(argument_spec={})
    file_args = {'path': '/tmp/test.txt', 'owner': 'testowner', 'group': 'testgroup', 'mode': '0755'}
    test_input = (module, True, 'Replaced string')
    expected_output = ('Replaced string and ownership, perms or SE linux context changed', True)
    assert expected_output == check_file_attrs(*test_input)



# Generated at 2022-06-13 06:00:29.440906
# Unit test for function write_changes
def test_write_changes():
    '''
    Create a temporary file to which the module.atomic_move is expected to be called.
    Then verify that function worked as expected.
    '''
    import mock
    import os
    import tempfile

    test_data = "This is the data"
    dest_name = tempfile.mktemp()
    tmp_name = tempfile.mktemp()
    params = {
        'unsafe_writes': True,
        'validate': None
    }
    module = mock.Mock(
        params=params,
        tmpdir=tempfile.gettempdir(),
    )
    write_changes(module, test_data, dest_name)
    assert not os.path.exists(tmp_name)
    assert os.path.exists(dest_name)

# Generated at 2022-06-13 06:00:37.841760
# Unit test for function check_file_attrs
def test_check_file_attrs():
    M = DummyModule()
    M.params = {"unsafe_writes": True, "dest": "/var/tmp/foo"}
    M.fail_json = DummyFailJson()
    M.run_command = DummyRunCommand()
    M.set_file_attributes_if_different = DummySetFileAttrs()
    M.load_file_common_arguments = DummyFileCommonAttrs()

    msg, changed = check_file_attrs(M, True, "Foo changed")
    assert msg == "Foo changed and ownership, perms or SE linux context changed"
    assert changed is True
# END of unit test



# Generated at 2022-06-13 06:00:42.660361
# Unit test for function check_file_attrs
def test_check_file_attrs():

    module = type('', (object,), dict(params=dict(path='', unsafe_writes=True),
                                      set_file_attributes_if_different=lambda self,a,b: True,
                                      load_file_common_arguments=lambda self, a: dict()
                                      ))
    assert check_file_attrs(module, False, '')[0] == 'ownership, perms or SE linux context changed'



# Generated at 2022-06-13 06:00:43.148819
# Unit test for function write_changes
def test_write_changes():
    pass



# Generated at 2022-06-13 06:00:48.730671
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # Test 1:
    #   test for change
    module = AnsibleModule(argument_spec={'unsafe_writes': {'type': 'bool', 'default': False, 'version_added': '2.3'}})
    module.params['path'] = 'file'
    module.params['mode'] = '0644'
    module.params['owner'] = 'root'
    module.params['group'] = 'root'
    module.params['seuser'] = 'user_u'
    module.params['serole'] = 'user_r'
    module.params['setype'] = 'user_t'
    module.params['selevel'] = ''
    changed = True
    message = ''
    result = check_file_attrs(module, changed, message)

# Generated at 2022-06-13 06:01:07.042135
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

# Generated at 2022-06-13 06:01:15.972245
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule({'tmpdir':'/tmp'})
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.params['tmpdir'])
    # Write the contents to the file
    f = os.fdopen(tmpfd, 'wb')
    f.close()
    # Set the valid status to True
    valid = True
    # Call write_changes function
    write_changes(module, "content", tmpfile)
    # Check for the return code of write_changes
    if os.path.exists(tmpfile):
        rc = 0
    else:
        rc = 1

    # Fail the module if return code is not 0

# Generated at 2022-06-13 06:01:17.481463
# Unit test for function write_changes
def test_write_changes():
    pass

# <<INCLUDE_ANSIBLE_MODULE_COMMON>>

# Generated at 2022-06-13 06:01:26.065149
# Unit test for function check_file_attrs
def test_check_file_attrs():
    m = AnsibleModule(argument_spec={})
    changed = True
    m.check_file_attrs = check_file_attrs

    m.params = dict(path='/tmp/foo', owner='bob', group='bob', mode='0700', seuser='unconfined_r')
    m.load_file_common_arguments = lambda x: x
    m.set_file_attributes_if_different = lambda x,y: True

    message = 'changed'
    expected_message = 'changed and ownership, perms or SE linux context changed'
    message, changed = m.check_file_attrs(m, changed, message)
    assert message == expected_message
    assert changed == True

    message = 'changed'
    expected_message = 'changed'
    message, changed = m.check_file

# Generated at 2022-06-13 06:01:29.350003
# Unit test for function check_file_attrs
def test_check_file_attrs():
    module_args = dict(
        path="/some/file",
        mode="0644",
        owner="jdoe",
        group="jdoe"
    )
    module = AnsibleModule(argument_spec={})
    module.params = module_args
    message = "some message"
    changed = False
    result = check_file_attrs(module, changed, message)
    assert result == ("some message and ownership, perms or SE linux context changed", True)



# Generated at 2022-06-13 06:01:35.739636
# Unit test for function check_file_attrs
def test_check_file_attrs():
    testmodule = AnsibleModule(argument_spec={})
    testmodule.params = {
        'path': '/etc/file',
        'owner': 'root',
        'group': 'root',
        'mode': '0644'
    }

    changed = False
    message = "message"

    message, changed = check_file_attrs(testmodule, changed, message)

    assert message == "message and ownership, perms or SE linux context changed"
    assert changed is True



# Generated at 2022-06-13 06:01:38.796297
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # Implementing unit test
    module = AnsibleModule(argument_spec={})
    message = ""
    changed = False
    assert check_file_attrs(module, changed, message) == (message, changed)


# Generated at 2022-06-13 06:01:45.333455
# Unit test for function main
def test_main():
    args = dict(
        dest='/var/log/access.log',
        regexp='(?P<client>\d+\.\d+\.\d+\.\d+)[^"]*"[^"]*"[^"]*"[^"]*"\s+(?P<statuscode>\d{3})\s+(?P<bytessent>\d+)\s+"[^"]*"\s+"[^"]*"\s+"[^"]*"\s+"(?P<referer>[^"]*)"\s+"(?P<agent>[^"]*)"'
    )
    res = main(args)
    assert res['changed']
    assert res['backup_file'] is not None

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:01:56.944582
# Unit test for function main
def test_main():
    import ansible.module_utils.ansible_release
    import ansible.module_utils.basic
    import ansible_collections.ansible.builtin.plugins.module_utils.ansible_module_common



# Generated at 2022-06-13 06:02:08.388795
# Unit test for function write_changes
def test_write_changes():
    '''
    Test write_changes function with a valid temp file
    '''
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True),
            validate=dict(required=False),
            unsafe_writes=dict(required=False, default=False),
            tmpdir=dict(required=False, default='/tmp')
        )
    )
    contents = 'Hello World.'
    path = '/tmp/test_write_changes'
    write_changes(module, contents, path)

    f = open(path,'r')
    data = f.read()
    f.close()
    assert data == 'Hello World.'



# Generated at 2022-06-13 06:02:39.389755
# Unit test for function check_file_attrs
def test_check_file_attrs():
    test_module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    test_module.params = {'path': '/tmp', 'owner': 'root', 'group': 'wheel', 'mode': '644', 'unsafe_writes': True }
    return_message, changed = check_file_attrs(test_module, True, 'changed')
    assert changed == True
    assert return_message == 'changed and ownership, perms or SE linux context changed'


# Generated at 2022-06-13 06:02:48.190785
# Unit test for function write_changes
def test_write_changes():
    import sys
    import os
    if sys.version_info >= (3, 0):
        from io import StringIO
    else:
        from StringIO import StringIO

    class FakeModule(object):
        def __init__(self, tmpdir):
            self.tmpdir = tmpdir
            self.params = {}

        def fail_json(self, msg):
            raise AssertionError(msg)

        def atomic_move(self, tmpfile, path, unsafe_writes):
            old_path = path + '.old'
            if os.path.exists(path):
                if unsafe_writes:
                    if os.path.exists(old_path):
                        os.unlink(old_path)
                os.rename(path, old_path)

            os.rename(tmpfile, path)
           

# Generated at 2022-06-13 06:02:59.299745
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # good
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(type='str', required=True),
            mode=dict(type='str', required=False),
            owner=dict(type='str', required=False),
            group=dict(type='str', required=False),
        ),
        supports_check_mode=True
    )
    module.params['path'] = '/tmp/test_file'
    module.params['mode'] = '0755'
    module.params['owner'] = 'root'
    module.params['group'] = 'root'
    changed = False
    message = ''
    actual = check_file_attrs(module, changed, message)
    desired = ('ownership, perms or SE linux context changed', True)
    assert actual == desired

    # bad


# Generated at 2022-06-13 06:03:08.346997
# Unit test for function main
def test_main():

    import tempfile

    my_path = tempfile.mktemp()
    os.makedirs(os.path.dirname(my_path))

    argv=['ansible.builtin.replace',
            'path', my_path,
            'regexp', 'old\.host\.name',
            'replace', 'new.host.name']

    # Write out a dummy host file
    with open(my_path, 'w') as f:
        f.write('127.0.0.1 localhost\n')
        f.write('127.0.0.1 old.host.name\n')

    with open(my_path, 'r') as f:
        for l in f:
            print (l, end='')

    # Run the module
    print (argv)

# Generated at 2022-06-13 06:03:13.743280
# Unit test for function main
def test_main():
    with open('/tmp/testfile5','w') as fh:
        fh.write('a\nb\nc\nd\n')
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

    params = module

# Generated at 2022-06-13 06:03:21.437554
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert(check_file_attrs(AnsibleModule(
        argument_spec={
            'mode': dict(type='str', default=None),
            'owner': dict(type='str', default=None),
            'group': dict(type='str', default=None),
            'seuser': dict(type='str', default=None),
            'serole': dict(type='str', default=None),
            'setype': dict(type='str', default=None),
            'selevel': dict(type='str', default=None),
            'unsafe_writes': dict(type='bool', default=False, aliases=['dangerous_mode']),
        },
    ), True, "something") == ("something and ownership, perms or SE linux context changed", True))


# Generated at 2022-06-13 06:03:31.062319
# Unit test for function check_file_attrs

# Generated at 2022-06-13 06:03:39.056953
# Unit test for function write_changes
def test_write_changes():
    class TestModule(object):
        def __init__(self):
            self.params = {'unsafe_writes': True}
            self.path = 'test.file'
            self.tmpdir = None
        def run_command(self, cmd, check_rc=True):
            pass
        def fail_json(self, msg):
            raise Exception(msg)
        def atomic_move(self, src, dest, unsafe_writes=True):
            pass

# Generated at 2022-06-13 06:03:49.266627
# Unit test for function write_changes
def test_write_changes():
    import shutil
    path = '/tmp/replace_test'
    original_content = b"Just some random text\nAnother random line\nA line with random in it\n"
    original_content_path = '/tmp/replace_test_original_content'
    open(original_content_path, 'wb').write(original_content)
    shutil.copyfile(original_content_path, path)
    test_content = b"Just some random text\nAnother random line\nA line with replaced in it\n"
    module_args = {'validate': None, 'path': '/tmp/replace_test', 'unsafe_writes': True}
    module = AnsibleModule(argument_spec={}, **module_args)
    write_changes(module, test_content, path)

# Generated at 2022-06-13 06:03:55.705031
# Unit test for function check_file_attrs
def test_check_file_attrs():
    # Test execution
    module = AnsibleModule({},check_mode=True)
    changed = 'true'
    message = 'test_message'
    result = check_file_attrs(module,changed,message)
    assert result == 'test_message and ownership, perms or SE linux context changed'


# Generated at 2022-06-13 06:04:48.409895
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={'path': {'required': True},'validate': {'default': None},'unsafe_writes': {'type': 'bool','required': 'no','default': False}})
    module.params['path'] = '/my/dest/file'
    module.params['validate'] = 'echo "Validate" "%s"'
    module.params['unsafe_writes'] = True
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils.basic import AnsibleModule
    (rc, out, err) = write_changes(module,'Test',module.params['path'])



# Generated at 2022-06-13 06:04:58.474877
# Unit test for function write_changes
def test_write_changes():
    """ Test function to verify the write_changes function.
    """
    module = AnsibleModule(argument_spec = dict())
    rc = None
    out = None
    err = None

    tmpfile = None
    contents = None

# Generated at 2022-06-13 06:05:06.286897
# Unit test for function check_file_attrs
def test_check_file_attrs():
    from ansible.modules.files.replace import check_file_attrs

# Generated at 2022-06-13 06:05:14.450086
# Unit test for function check_file_attrs
def test_check_file_attrs():
    contents = """#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2013, Evan Kaufman <evan@digitalflophouse.com
# Copyright: (c) 2017, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type
"""
    tempfd, tempfile = tempfile.mkstemp(dir="/tmp")
    f = os.fdopen(tempfd, 'wb')
    f.write(contents)
    f.close()

# Generated at 2022-06-13 06:05:23.110394
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec = dict(path=dict(type='path', required=True),
                             contents=dict(type='str', required=True),
                             validate=dict(type='str'))
    )
    path = module.params['path']
    validate = module.params.get('validate', None)
    if validate:
        if "%s" not in validate:
            module.fail_json(msg="validate must contain %%s: %s" % (validate))
    contents = module.params['contents']
    write_changes(module, contents, path)
    


# Generated at 2022-06-13 06:05:24.926377
# Unit test for function write_changes
def test_write_changes():
    '''
    Test function write_changes
    '''

# Generated at 2022-06-13 06:05:35.176760
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text


# Generated at 2022-06-13 06:05:41.181337
# Unit test for function main
def test_main():
  test_module = AnsibleModule(
      argument_spec=dict(
          path=dict(type='str', required=True, aliases=['dest', 'destfile', 'name']),
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
      check_invalid_arguments=False,
      no_log=True,
  )
  test_module.params['path'] = 'test'
  test_

# Generated at 2022-06-13 06:05:52.215476
# Unit test for function check_file_attrs
def test_check_file_attrs():
    """Unit test to cover the test_check_file_attrs.

    """
    this_test = {}
    this_test['file_args'] = {
        'path': '/tmp/test',
        'owner': 'john',
        'group': 'john',
        'mode': '0600',
        }
    this_test['changed'] = False
    this_test['message'] = 'Test message'

    # Not checking for module.set_file_attributes_if_different
    # since it exercises os.chmod, os.chown and os.chown

    # Test
    message, changed = check_file_attrs(this_test['module'], this_test['changed'], this_test['message'])

    # Asserts
    assert this_test['changed'] is changed

# Generated at 2022-06-13 06:05:57.089963
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(argument_spec={'path':{'type':'str'},'validate':{'type':'str'},'unsafe_writes':{'type':'bool'}})
    path = '/tmp/test_write_changes'
    contents = to_text(b'hi')
    module.atomic_move = lambda src, dest: None
    write_changes(module, contents, path)


# Generated at 2022-06-13 06:07:49.739238
# Unit test for function check_file_attrs
def test_check_file_attrs():
    mock_module = AnsibleModule(argument_spec={'path': dict(type='path', required=True),
                                               'owner': dict(), 'group': dict(), 'mode': dict(),
                                               'seuser': dict(), 'serole': dict(), 'setype': dict(),
                                               'selevel': dict()})
    # mock_module.atomic_move = dict()
    mock_module.set_file_attributes_if_different = dict()
    # mock_module.params = dict()
    mock_module.load_file_common_arguments = dict()
    mock_module.fail_json = dict()

    # changed = dict()
    # message = dict()
    # assert check_file_attrs(mock_module, changed, message) is not None



# Generated at 2022-06-13 06:07:57.003027
# Unit test for function write_changes
def test_write_changes():
    # Mock-up module object to run the module code
    module = AnsibleModule(argument_spec=dict(
        path=dict(required=True),
        regexp=dict(required=True),
        replace=dict(required=False),
        after=dict(required=False),
        before=dict(required=False),
        unsafe_writes=dict(required=False, default=True),
        validate=dict(required=False)
    ))

    # Call the module
    test_contents = "This is a test file"
    test_path = "/tmp/testfile"
    write_changes(module, test_contents, test_path)

    # Validate the contents of the temp file
    testfile = open(test_path, 'r')

# Generated at 2022-06-13 06:08:09.158160
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

# Generated at 2022-06-13 06:08:21.812501
# Unit test for function check_file_attrs
def test_check_file_attrs():
    """Unit test for function check_file_attrs"""
    class FakeModule(object):
        def __init__(self):
            self.params = dict()
            self.changed = False
            self.exit_args = None

        def load_file_common_arguments(self, _):
            return dict(path='/tmp/dummy')

        def set_file_attributes_if_different(self, args, _):
            if self.params['seuser'] == 'error':
                raise OSError('simulated fail')
            self.changed = self.params['seuser'] == 'changed'
            return self.changed

        def exit_json(self, *args):
            self.exit_args = args

        def fail_json(self, *args):
            self.exit_args = args


# Generated at 2022-06-13 06:08:27.362462
# Unit test for function main
def test_main():

    # create a mock module
    module = AnsibleModule(argument_spec = dict(path = dict(required = True), regexp = dict(required = True), replace = dict(), after = dict(), before = dict(), backup = dict(type = 'bool'), validate = dict(), encoding = dict(type = 'str')))

    module.run_command = Mock(return_value=(0, "stdout", "stderr"))

    module.check_mode = False
    module._diff = True
    module.params = {'path': '/test/path', 'regexp': 'test regexp', 'replace': 'test replace', 'backup': False, 'encoding': 'utf-8'}

    # create a mock file module
    file_module = Mock()
    

# Generated at 2022-06-13 06:08:28.945285
# Unit test for function check_file_attrs
def test_check_file_attrs():
    assert check_file_attrs('', False, '') == ('', True)



# Generated at 2022-06-13 06:08:37.500094
# Unit test for function write_changes
def test_write_changes():
    module = AnsibleModule(
        argument_spec = dict(
            path = dict(type='path', required=True),
            contents = dict(),
            validate = dict(),
            unsafe_writes = dict(type='bool', default=False),
        ),
        add_file_common_args=True,
        supports_check_mode=True,
    )
    path = module.params['path']
    contents = module.params['contents']
    validate = module.params['validate']
    tmpfd, tmpfile = tempfile.mkstemp(dir=module.tmpdir)
    f = os.fdopen(tmpfd, 'wb')
    f.write(contents)
    assert(os.path.isfile(tmpfile))
    os.remove(tmpfile)

# Generated at 2022-06-13 06:08:41.773719
# Unit test for function check_file_attrs

# Generated at 2022-06-13 06:08:48.676103
# Unit test for function check_file_attrs

# Generated at 2022-06-13 06:08:55.173178
# Unit test for function check_file_attrs
def test_check_file_attrs():

    omodule = AnsibleModule({}, check_mode=False)
    omodule.params = {'path': '/path/to/file', 'owner': 'somebody', 'group': 'somebodyelse', 'mode': '0600', 'unsafe_writes': False}
    omodule.set_file_attributes_if_different = lambda x, y: True
    changed, msg = check_file_attrs(omodule, True, "something")
    assert changed
    assert msg == 'something and ownership, perms or SE linux context changed'
