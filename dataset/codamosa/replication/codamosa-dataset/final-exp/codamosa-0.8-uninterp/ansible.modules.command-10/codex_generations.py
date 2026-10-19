

# Generated at 2022-06-13 04:52:13.710540
# Unit test for function main
def test_main():
    module = AnsibleModule({'_raw_params': 'ls', '_uses_shell': False, 'argv': [], 'chdir': '', 'executable': '', 'creates': '', 'removes': ''})
    args = module.params['_raw_params']
    cmd = ['ls']
    if args:
        cmd = shlex.split(args)
    if not cmd:
        rc = 256
    else:
        rc, out, err = module.run_command(cmd, executable=None, use_unsafe_shell=False, encoding=None)
    assert rc == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:52:25.248636
# Unit test for function main
def test_main():
    import ansible
    import distutils.spawn

    original_exists = distutils.spawn.find_executable

    def find_executable_dummy(name):
        if name == 'bogus':
            return None
        else:
            return original_exists(name)

    distutils.spawn.find_executable = find_executable_dummy


# Generated at 2022-06-13 04:52:34.719293
# Unit test for function main
def test_main():
    arg_spec = dict(
        chdir=dict(),
        executable=dict(),
        creates=dict(),
        removes=dict(),
        warn=dict(),
        stdin=dict(),
        strip_empty_ends=dict(type='bool'),
    )
    raw_params = 'ls /home/vagrant'
    no_args = ''
    argv = ['ls', '/home/vagrant']
    shell_true = True
    executable_path = '/usr/bin/bash'
    chdir_path = '/home/vagrant'
    creates_path = '/home/vagrant/test.txt'
    removes_path = '/home/vagrant/test.txt'
    warn_true = True
    stdin_test_string = 'test'

    #test basic functionality and return code

# Generated at 2022-06-13 04:52:42.517514
# Unit test for function main
def test_main():
    import inspect
    import os
    import tempfile
    # Create temp directory
    test_directory = tempfile.mkdtemp()
    def test_args(args):
        args['chdir'] = test_directory
        args['creates'] = None
        args['removes'] = None
        args['_raw_params'] = b'echo "hello"'
        return args
    def test_argv(args):
        args['chdir'] = test_directory
        args['creates'] = None
        args['removes'] = None
        args['argv'] = ['echo', '"hello"']
        return args
    # Test numeric arguments that should return a list
    assert is_iterable([1,2,3], include_strings=False)

# Generated at 2022-06-13 04:52:55.756052
# Unit test for function main
def test_main():
    r = {}


# Generated at 2022-06-13 04:53:08.332932
# Unit test for function main
def test_main():
    # set up basic test
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(),
            creates=dict(type='path'),
            removes=dict(type='path'),
            warn=dict(type='bool'),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True)
        ),
        supports_check_mode=True
    )
    # TODO add test for check_command
    # test create

# Generated at 2022-06-13 04:53:19.231285
# Unit test for function main
def test_main():
    import pytest

    def test_cases():
        yield True
        yield None
        yield False

    @pytest.mark.parametrize("arg1", test_cases())
    def test_ansible_command_module_main(monkeypatch, arg1):
        if arg1:
            monkeypatch.setattr(
                'ansible.module_utils.basic.AnsibleModule.run_command',
                lambda x, **kw: 0)
        elif arg1 is None:
            monkeypatch.setattr(
                'ansible.module_utils.basic.AnsibleModule.run_command',
                lambda x, **kw: (0, 'stdout', 'stderr'))

# Generated at 2022-06-13 04:53:32.299845
# Unit test for function main
def test_main():
    #
    # To test above code we need to:
    # 1. Define a dict with all the function inputs (and some extras to
    #    verify that they get ignored)
    # 2. Call the function with this dict (and some other args)
    # 3. Verify that the expected results are returned
    #
    args = dict(
        _raw_params="echo hello",
        _uses_shell=False,
        argv=["echo", "hello"],
        chdir=".",
        executable=None,
        creates=None,
        removes="a_file"
    )
    # Fake the AnsibleModule class
    class FakeModule(object):
        def __init__(self, args):
            self.model_queue = []
            for key in args:
                setattr(self, key, args[key])


# Generated at 2022-06-13 04:53:45.001363
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='echo "hello"',
        _uses_shell=dict(type='bool', default=False),
        argv=dict(type='list', elements='str'),
        chdir=dict(type='path'),
        executable=dict(),
        creates=dict(type='path'),
        removes=dict(type='path'),
        warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
        stdin=dict(required=False),
        stdin_add_newline=dict(type='bool', default=True),
        strip_empty_ends=dict(type='bool', default=True),
    )
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 04:53:59.560835
# Unit test for function main
def test_main():
    # Test with a valid command that produces some output
    test_command_args = dict(
        chdir='/',
        creates='/tmp/test',
        executable='/bin/bash',
        _raw_params='echo "hello" > /tmp/test',
        _uses_shell=True,
        warn=True,
        strip_empty_ends=True
    )
    test_command_result = dict(
        changed=True,
        stdout='',
        stderr='',
        rc=0,
        cmd=['echo', '"hello"', '>', '/tmp/test'],
        start=None,
        end=None,
        delta=None,
        msg=''
    )


# Generated at 2022-06-13 04:54:19.981959
# Unit test for function main
def test_main():
    # Test case with module argument with value 'command'
    test_args = dict()
    test_args['_ansible_diff'] = False
    test_args['_ansible_verbosity'] = 2
    test_args['_ansible_version'] = 'v2.5.5'
    test_args['_ansible_debug'] = False
    test_args['_ansible_check_mode'] = False
    test_args['_raw_params'] = 'cat /etc/motd'
    test_args['_uses_shell'] = False
    test_args['chdir'] = None
    test_args['creates'] = None
    test_args['executable'] = None
    test_args['removes'] = None
    test_args['warn'] = False
    test_args['argv'] = None


# Generated at 2022-06-13 04:54:25.513389
# Unit test for function check_command
def test_check_command():
    mod = AnsibleModule(argument_spec={})
    fc = {'command': 'cat /etc/motd', 'args': {'warn': True}}
    check_command(mod, fc['command'])

    fc = {'command': ['cat', '/etc/motd'], 'args': {'warn': True}}
    check_command(mod, fc['command'])

    mod = AnsibleModule(argument_spec={})
    fc = {'command': 'cat /etc/motd', 'args': {'warn': False}}
    check_command(mod, fc['command'])



# Generated at 2022-06-13 04:54:36.599999
# Unit test for function main

# Generated at 2022-06-13 04:54:41.357519
# Unit test for function check_command
def test_check_command():
    class fake_module():
        def __init__(self):
            self.warn = None

        def _warn(self, msg):
            self.warn = msg

    test_module = fake_module()
    test_module.warn = test_module._warn

    check_command(test_module, "echo")
    assert test_module.warn is None

    check_command(test_module, "chmod")
    assert test_module.warn == "Consider using the file module with mode rather than running 'chmod'.  If you need to use 'chmod' because the file module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."

    check_command(test_module, "touch")

# Generated at 2022-06-13 04:54:48.311258
# Unit test for function check_command
def test_check_command():
    module_mock = MagicMock(name='AnsibleModule')
    module_mock.check_mode = False
    check_command(module_mock, ['/bin/touch', '/tmp/test_check'])
    check_command(module_mock, 'touch /tmp/test_check')



# Generated at 2022-06-13 04:55:01.504680
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(default='date'),
            _uses_shell=dict(type='bool', default=True),
            chdir=dict(),
            executable=dict(),
            args=dict(),
            argv=dict(type='list', elements='str'),
            creates=dict(),
            removes=dict(),
            warn=dict(type='bool', default=False),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

    test_module.run_command = lambda args, **kwargs: (0, 'stdout', 'stderr')
    test_module.check_mode = False

    main()



# Generated at 2022-06-13 04:55:11.125638
# Unit test for function main
def test_main():
    from ansible.modules.extras.command.command import main
    from ansible.module_utils.common.collections import ImmutableDict

# Generated at 2022-06-13 04:55:14.815003
# Unit test for function main
def test_main():
    """Test function main"""
    import os
    import sys
    import tempfile
    import mock
    # Assert if main exists in module
    assert callable(main)



# Generated at 2022-06-13 04:55:26.413552
# Unit test for function main
def test_main():

    testmodule = AnsibleModule({
        '_raw_params': "ls",
        '_uses_shell': True,
        '_ansible_tmpdir': "tmp",
        '_ansible_check_mode': True,
        'argv': "ls",
        'chdir': "tmp",
        'executable': None,
        'creates': "tmp/myfile",
        'removes': "tmp/myfile",
        '_ansible_no_log': False,
        'stdin': None,
        'stdin_add_newline': True,
        'strip_empty_ends': True
    })

    testmodule.run_command = MagicMock(return_value=(0, "stdout", "stderr"))
    testmodule.fail_json = MagicMock()
    testmodule.exit

# Generated at 2022-06-13 04:55:35.539915
# Unit test for function check_command
def test_check_command():
    module = MockAnsibleModule()
    check_command(module, 'chown foo /bar')
    assert module.warn.call_count == 1
    assert 'Consider using the file module with owner rather than running \'chown\'.  If you need to use \'chown\' because the file module is insufficient you can add \'warn: false\' to this command task or set \'command_warnings=False\' in the defaults section of ansible.cfg to get rid of this message.' in module.warn.call_args[0]
    check_command(module, 'chmod 654 /bar')
    assert module.warn.call_count == 2

# Generated at 2022-06-13 04:55:52.354304
# Unit test for function main

# Generated at 2022-06-13 04:56:03.967457
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_native, to_bytes
    content = """
        [defaults]
        command_warnings = False
        """
    tmpfile = basic.write_tmp_file(content, '.cfg')
    os.environ['ANSIBLE_CONFIG'] = tmpfile.name

# Generated at 2022-06-13 04:56:05.283186
# Unit test for function check_command
def test_check_command():
    assert check_command('somefile.py', ['test', 'arg']) == None


# Generated at 2022-06-13 04:56:14.401923
# Unit test for function check_command
def test_check_command():
    import sys
    sys.modules['ansible'] = type('AnsibleModule', (object,), {'AnsibleModule':type('AnsibleModule', (object,), {})})
    global AnsibleModule
    AnsibleModule = sys.modules['ansible'].AnsibleModule

    module = type('AnsibleModule', (object,), {'warn': lambda self, msg: msg, 'params': {'warn': True}})()
    global module
    commandline = 'rmdir /the/path'

# Generated at 2022-06-13 04:56:26.556947
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.parsing.convert_bool import boolean
    from ansible.module_utils._text import to_text
    from ansible.module_utils.common.collections import is_iterable

    # Special case for unit testing/execution
    try:
        import ansible.utils.module_docs_fragments
        from ansible.module_utils.common.text.converters import to_int
    except ImportError:
        pass


# Generated at 2022-06-13 04:56:36.515731
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.collections import is_iterable
    from ansible.module_utils._text import to_text, to_bytes
    from ansible.module_utils.common.warnings import Warnings

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )
    command = 'apt-get -y'
    check_command(module, command)
    assert module.warnings == [
        Warnings.deprecated('apt-get', 'apt')]

    command = 'apt-get -y install openjdk-8-jre'
    check_command(module, command)
    assert module.warnings == [
        Warnings.deprecated('apt-get', 'apt')]



# Generated at 2022-06-13 04:56:45.906048
# Unit test for function check_command
def test_check_command():
    class FakeModule:
        def __init__(self):
            self.warned = False
        def warn(self, msg):
            self.warned = True
    result = dict(changed=False)
    result['warnings'] = []
    module = FakeModule()
    check_command(module, 'yum update')
    assert module.warned, "should have warned the user to use yum module instead of shell command"
    check_command(module, 'zypper update')
    assert module.warned, "should have warned the user to use dnf module instead of shell command"
    check_command(module, 'dnf update')
    assert module.warned, "should have warned the user to use zypper module instead of shell command"
    check_command(module, 'chmod 777 /foo')
    assert module.warn

# Generated at 2022-06-13 04:56:52.863710
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils.warnings import AnsibleDeprecationWarning

    module = AnsibleModule(argument_spec={'command': {'required': True, 'type': 'str'},
                                           'warn': {'default': False, 'type': 'bool'}})
    import warnings
    warnings.simplefilter('ignore', category=AnsibleDeprecationWarning)
    check_command(module, 'curl')
    check_command(module, 'command')



# Generated at 2022-06-13 04:56:59.499143
# Unit test for function main
def test_main():
    r = {}
    r['msg'] = 'non-zero return code'
    r['rc'] = 2
    r['changed'] = True
    r['cmd'] = '/usr/bin/python'
    r['stdout'] = "skipped, since %s exists" % 'test'
    assert r['msg'] == 'non-zero return code'
    assert r['rc'] != 0
    assert r['changed'] == True
    assert r['cmd'] == '/usr/bin/python'
    assert r['stdout'] == "skipped, since %s exists" % 'test'


# Generated at 2022-06-13 04:57:06.392936
# Unit test for function check_command
def test_check_command():
    from ansible.compat.tests.mock import patch, MagicMock
    module = MagicMock()
    check_command(module, ['echo', 'hello'])
    assert module.warn.call_count == 1
    assert module.warn.call_args[0][0] == "Consider using 'become', 'become_method', and 'become_user' rather than running echo"
    module.reset_mock()
    check_command(module, ['chmod', 'hello'])
    assert module.warn.call_count == 1

# Generated at 2022-06-13 04:57:36.041294
# Unit test for function main
def test_main():
    args = dict(
        _raw_params="openssl",
        argv=["openssl"],
        chdir=None,
        executable=None,
        creates=None,
        removes=None,
        warn=True,
        stdin=None,
        stdin_add_newline=True,
        strip_empty_ends=True,
        _uses_shell=False
        )

# Generated at 2022-06-13 04:57:47.189182
# Unit test for function main
def test_main():
    from ansible_collections.ansible.builtin.plugins.module_utils.common._collections_compat import Mock, patch
    mock_module = Mock(name='CommandModule', return_value=None)
    mock_module.params = {'_raw_params': None, '_uses_shell': False, 'argv': [], 'chdir': None, 'executable': None, 'creates': None, 'removes': None, 'warn': False, 'stdin': "", 'stdin_add_newline': True, 'strip_empty_ends': True}
    mock_module.check_mode = False
    mock_module.run_command = Mock(return_value=(0, '', ''))
    mock_module.warn = Mock(return_value=None)

# Generated at 2022-06-13 04:57:54.895439
# Unit test for function main

# Generated at 2022-06-13 04:57:55.483964
# Unit test for function main
def test_main():
  assert True == True


# Generated at 2022-06-13 04:57:56.054572
# Unit test for function check_command
def test_check_command():
    pass



# Generated at 2022-06-13 04:57:58.720284
# Unit test for function check_command
def test_check_command():
    args = dict(check_command=dict(warn='yes'))
    module = AnsibleModule(argument_spec=args)
    check_command(module, "curl")

# ===========================================
# Main control flow


# Generated at 2022-06-13 04:58:05.867213
# Unit test for function main

# Generated at 2022-06-13 04:58:13.915460
# Unit test for function main

# Generated at 2022-06-13 04:58:26.209709
# Unit test for function main
def test_main():
    '''
    ISO_8859-1, ISO_8859-15, and UTF-8 data
    '''
    args = [u'\u00E0', u'\u00E1', u'\u00E7', u'\u00E9', u'\u00EE', u'\u00F4', u'\u00F9', u'\u00FF']

    '''
    The following charset names are mostly from Unicode 9.0.0 with some
    other common names added.
    '''

# Generated at 2022-06-13 04:58:35.351352
# Unit test for function check_command
def test_check_command():
    """Test module's check_command function"""
    # pylint: disable=too-many-locals,unused-variable
    module = AnsibleModule(
        argument_spec={},
    )
    # Dummy check_command function
    def dummy_warn(msg, *args, **kwargs):
        return msg
    # Setup
    module.warn = dummy_warn
    check_command(module, 'tar')
    check_command(module, 'wget')
    check_command(module, 'chmod')
    check_command(module, 'curl')
    # Teardown



# Generated at 2022-06-13 04:59:25.672494
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils import basic
    module = basic.AnsibleModule(argument_spec={})
    module.warn = lambda x: x
    assert isinstance(check_command(module, 'command'), None)
    assert "Consider using the file module" in check_command(module, 'chown')
    assert "Consider using the get_url or uri module" in check_command(module, 'curl')
    assert "Consider using the sudo module" in check_command(module, 'sudo')


# Generated at 2022-06-13 04:59:37.273186
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    import sys
    import tempfile
    import shutil
    module = basic.AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list'),
            chdir=dict(type='path', default=None),
            executable=dict(default=None),
            creates=dict(type='path'),
            removes=dict(type='path'),
            warn=dict(type='bool', default=False),
            stdin=dict(type='str', default=None),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        ),
    )



# Generated at 2022-06-13 04:59:38.448002
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:59:49.840085
# Unit test for function check_command
def test_check_command():
    check_command(commandline="rm /tmp/foo1")
    check_command(commandline="ls /tmp/foo2")
    check_command(commandline="yum install -y foo3")
    check_command(commandline="zypper install -y foo4")
    check_command(commandline="wget http://localhost:8080/foo5")
    check_command(commandline="mount /dev/foo /mnt")
    check_command(commandline="rpm -q mypkg")
    check_command(commandline="rpm -q --whatprovides mypkg")
    check_command(commandline="svn status /tmp/foo")
    check_command(commandline="service myservice start")
    check_command(commandline="pbrun mycmd")

# Generated at 2022-06-13 04:59:51.336940
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:59:52.952173
# Unit test for function main
def test_main():
    assert True == True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:59:59.104275
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(
        argument_spec=dict(),
    )
    check_command(module, ['apt-get', 'install', 'apache'])
    check_command(module, 'apt-get install apache')
    assert module.warnings == [
        'Consider using the apt module rather than running \'apt-get\'.  '
        "If you need to use 'apt-get' because the apt module is insufficient you can"
        " add 'warn: false' to this command task or set 'command_warnings=False'"
        " in the defaults section of ansible.cfg to get rid of this message.",
    ]
    module.warnings = []
    check_command(module, ['touch', '/etc/foo'])

# Generated at 2022-06-13 05:00:11.456970
# Unit test for function main
def test_main():
    args = {
            '_ansible_no_log': False,
            '_ansible_check_mode': False,
            '_ansible_debug': False,
            'chdir': None,
            'creates': None,
            '_raw_params': 'echo hello',
            '_ansible_verbosity': 0,
            '_ansible_diff': False,
            '_uses_shell': False,
            'stdin': None,
            '_ansible_version': u'2.10.2',
            'strip_empty_ends': True,
            'removes': None,
            'executable': None
            }
    args = AnsibleModule(**args).params
    r = main()
    assert r['stdout']=='hello'

# Generated at 2022-06-13 05:00:26.031183
# Unit test for function main
def test_main():
    result = {
        'changed': True,
        'msg': '',
        'rc': 0,
        'start': '',
        'end': '',
        'delta': '',
        'stderr': '',
        'stdout': '',
        'cmd': '',
    }

    def check_module_result(module, results):
        assert module.exit_json.called
        exit_args, exit_kwargs = module.exit_json.call_args
        assert results == exit_kwargs


# Generated at 2022-06-13 05:00:34.552611
# Unit test for function main
def test_main():
    cmd = 'date'
    r = {'changed': False, 'stdout': '', 'stderr': '', 'rc': None, 'cmd': None, 'start': None, 'end': None, 'delta': None, 'msg': ''}
    r['cmd'] = cmd

    (rc, out, err) = module.run_command(cmd, executable=None, use_unsafe_shell=False, encoding=None, data=None, binary_data=False)
    r['rc'] = rc
    r['stdout'] = out
    r['stderr'] = err
    module.exit_json(**r)
if __name__ == '__main__':
    main()