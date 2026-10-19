

# Generated at 2022-06-13 04:52:12.373088
# Unit test for function check_command
def test_check_command():
    def mywarn(msg):
        test.assertTrue(msg)
    class MyModule:
        def __init__(self):
            self.warn = mywarn
            self.params = {}
    m = MyModule()
    check_command(m, "curl google.com")



# Generated at 2022-06-13 04:52:24.410177
# Unit test for function main
def test_main():
    test_argv=['./test_command']
    test_args="./test_command"
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(),
            creates=dict(type='path'),
            removes=dict(type='path'),
            # The default for this really comes from the action plugin
            warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
        ),
        supports_check_mode=True,
    )
    shell = module.params['_uses_shell']
    ch

# Generated at 2022-06-13 04:52:26.929505
# Unit test for function main
def test_main():
    '''
    Unit test for main function
    '''
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:52:35.171762
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
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
        ),
        supports_check_mode=True,
    )
    shell = module

# Generated at 2022-06-13 04:52:39.799269
# Unit test for function check_command
def test_check_command():
    run_this = 'ls -la'
    mod = AnsibleModule({'command': run_this}, check_invalid_arguments=False, add_file_common_args=False)
    check_command(mod, run_this)

# Main module code

# Generated at 2022-06-13 04:52:45.847636
# Unit test for function main
def test_main():

    test_module_data_args = ["ping", "-c", "1", "localhost"]
    test_module_data_args_list =["ping", "-c", "1", "localhost"]
    test_module_data_chdir = "/home"
    test_module_data_creates ="/home/ansible"
    test_module_data_removes ="/home/ansible"
    test_module_data_warn ="True"
    test_module_data_shell ="True"
    test_module_data_stdin ="/home/ansible/linux_training_examples/test/test_from_main"
    test_module_data_stdin_add_newline ="True"
    test_module_data_strip ="True"

    result = []


# Generated at 2022-06-13 04:52:58.092820
# Unit test for function main
def test_main():
    from ansible import context
    from ansible.module_utils.common.file import trace_logs
    from ansible.module_utils.basic import load_params
    from ansible.module_utils.common.args import AnsibleModuleArgs
    from ansible.module_utils._text import to_bytes, to_native
    from ansible.module_utils.common._collections_compat import Mapping
    from ansible.module_utils.common.collections import MutableMapping

# Generated at 2022-06-13 04:53:11.037200
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(name='command', argument_spec={}, supports_check_mode=True)
    check_command(module, "chown foo")
    check_command(module, "chmod foo")
    check_command(module, "chgrp foo")
    check_command(module, "ln foo")
    check_command(module, "mkdir foo")
    check_command(module, "rmdir foo")
    check_command(module, "rm foo")
    check_command(module, "touch foo")
    check_command(module, "curl foo")
    check_command(module, "wget foo")
    check_command(module, "svn foo")
    check_command(module, "service foo")
    check_command(module, "mount foo")

# Generated at 2022-06-13 04:53:17.368049
# Unit test for function main
def test_main():
    args = dict(
        chdir=None,
        executable=None,
        creates=None,
        removes=None,
        warn=False,
        stdin=None,
        stdin_add_newline=True,
        strip_empty_ends=True,
        _raw_params='',
        _uses_shell=False,
        argv=None,
    )

    check_mode = False

# Generated at 2022-06-13 04:53:30.526807
# Unit test for function check_command
def test_check_command():
    mod = mock.Mock()
    check_command(mod, ['chmod', 'foo'])
    mod.warn.assert_called_with("Consider using the file module with mode rather than running 'chmod'.  "
                                "If you need to use 'chmod' because the file module is insufficient you can add "
                                "'warn: false' to this command task or set 'command_warnings=False' in "
                                "the defaults section of ansible.cfg to get rid of this message.")
    mod.reset_mock()
    check_command(mod, ['chown', 'foo'])

# Generated at 2022-06-13 04:53:54.615174
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 04:53:58.585042
# Unit test for function main
def test_main():
    # FIXME: Add test cases
    r = main()
    assert r['rc'] == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:54:07.209588
# Unit test for function main
def test_main():
    #Load module
    print("Test module import")

# Generated at 2022-06-13 04:54:19.828003
# Unit test for function main
def test_main():
    module_mock = create_autospec(AnsibleModule)
    module_mock.run_command.return_value = (0,'a test return string','')
    setattr(module_mock, 'params', {})
    module_mock.params['_uses_shell'] = False
    module_mock.params['_raw_params'] = 'echo hello'
    module_mock.params['creates'] = None
    module_mock.params['removes'] = None
    module_mock.params['executable'] = None
    module_mock.params['chdir'] = None
    module_mock.params['warn'] = True
    module_mock.params['stdin'] = None
    module_mock.params['stdin_add_newline'] = True
    module_m

# Generated at 2022-06-13 04:54:26.109201
# Unit test for function main
def test_main():
    # Mock module and command line arguments
    mock = MagicMock(return_value=dict(
        _uses_shell=False,
        argv=['ping', '-c', '1', 'localhost'],
        executable='/usr/bin/python',
        chdir='/Users/arunkhurana/workspace/tmp',
        creates='/tmp/myfile',
        removes='/tmp',
        warn=False,
        stdin='hello',
        stdin_add_newline=True,
        strip_empty_ends=True,
    ))
    module = mock.start()
    
    # Unit test for main
    main()
    
    # Stop the mock
    mock.stop()


# Generated at 2022-06-13 04:54:28.923716
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    commandline = '/bin/echo myvar=Hi'
    check_command(module, commandline)
    result = module.warnings[0]
    assert result == "Consider using the file module with state=touch rather than running '/bin/echo'."


# Generated at 2022-06-13 04:54:38.083322
# Unit test for function check_command
def test_check_command():

    class FakeModule:
        _warnings = []

        def warn(self, warning):
            self._warnings.append(warning)

        @property
        def warnings(self):
            return self._warnings

    m = FakeModule()
    check_command(m, 'chown')
    check_command(m, 'chmod')
    check_command(m, 'chgrp')
    check_command(m, 'cp')
    check_command(m, 'ln')
    check_command(m, 'mkdir')
    check_command(m, 'rm')
    check_command(m, 'rmdir')
    check_command(m, 'touch')
    check_command(m, 'curl')
    check_command(m, 'wget')
    check_command(m, 'svn')

# Generated at 2022-06-13 04:54:44.507277
# Unit test for function main

# Generated at 2022-06-13 04:54:51.830036
# Unit test for function main
def test_main():

  cm = AnsibleModule(argument_spec=dict(
    _raw_params=dict(),
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
  ), supports_check_mode=True)

# Generated at 2022-06-13 04:55:02.667995
# Unit test for function main

# Generated at 2022-06-13 04:55:30.846342
# Unit test for function main

# Generated at 2022-06-13 04:55:37.978650
# Unit test for function check_command
def test_check_command():
    commandline = ['/bin/chown']
    arguments = {'chown': 'owner', 'chmod': 'mode', 'chgrp': 'group',
                 'ln': 'state=link', 'mkdir': 'state=directory',
                 'rmdir': 'state=absent', 'rm': 'state=absent', 'touch': 'state=touch'}
    assert check_command(commandline) == arguments[commandline]


# Generated at 2022-06-13 04:55:48.363989
# Unit test for function main

# Generated at 2022-06-13 04:55:57.413930
# Unit test for function main
def test_main():
    result = dict(
        cmd=['/bin/true'],
        rc=0,
        stdout='',
        changed=False,
        stderr='',
        start='2017-09-29 22:03:48.083128',
        end='2017-09-29 22:03:48.084657',
        delta='0:00:00.001529'
    )
    test_main_result = main()
    assert result == test_main_result

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:05.568494
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule({})
    check_command(module, 'chown test:test /path')
    assert module.warnings[0] == "Consider using the file module with chown rather than running 'chown'.  If you need to use 'chown' because the file module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."
    module = AnsibleModule({})
    check_command(module, 'curl http://something.com')

# Generated at 2022-06-13 04:56:12.953637
# Unit test for function main
def test_main():
    args = ['ls', '/']
    to_text_a = ['ls', '/']
    module = AnsibleModule(argument_spec=dict())
    module.params.update({ '_raw_params': '', '_uses_shell': 'False', 'argv': ['ls', '/'], 'chdir': '', 'executable': '', 'creates': '', 'removes': '', 'warn': 'False', 'stdin': '', 'stdin_add_newline': 'True', 'strip_empty_ends': 'True'})
    main()


# Generated at 2022-06-13 04:56:25.543929
# Unit test for function main
def test_main():
    cmd_module = AnsibleModule(
        argument_spec=dict(
            args=dict(type='str'),
            chdir=dict(type='str'),
            executable=dict(type='str'),
            creates=dict(type='str'),
            removes=dict(type='str'),
            strip=dict(type='bool'),
        ),
        supports_check_mode=True
    )
    cmd_module.run_command = Mock(return_value=(0,"",""))
    cmd_module.exit_json = Mock()
    cmd_module.fail_json = Mock()

    # Invalid args
    assert_raises(AnsibleAssertionError, main, cmd_module)

    # Happy path
    cmd_module.params['args'] = "foo"
    main(cmd_module)
    assert cmd_module.run_

# Generated at 2022-06-13 04:56:36.454806
# Unit test for function main
def test_main():
    import mock
    res = mock.Mock()
    res.return_code = 0
    res.stdout = b'hello\n'
    res.stderr = b'error\n'
    with mock.patch.object(AnsibleModule, 'run_command', return_value=(res.return_code, res.stdout, res.stderr)):
        with mock.patch.object(AnsibleModule, 'exit_json') as exit_json:
            main()

# Generated at 2022-06-13 04:56:39.242559
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec=dict(), supports_check_mode=True)
    check_command(module, u'/bin/chmod 755 /tmp/not/a/real/path')


# Generated at 2022-06-13 04:56:46.570199
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={
        'argv': {'type': 'list', 'elements': 'str'},
        'free_form': {'type': 'str'},
        'warn': {'type': 'bool', 'default': False},
    })
    check_command(module, 'curl')
    check_command(module, ['curl'])
    check_command(module, 'yum')
    check_command(module, 'chown')
    check_command(module, 'ln')
    check_command(module, 'chmod')
    check_command(module, 'chgrp')


# Generated at 2022-06-13 04:57:35.152280
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule({})
    commandline = 'ls -la'
    check_command(module, commandline)
    commandline = ['ls', '-la']
    check_command(module, commandline)


# Generated at 2022-06-13 04:57:36.197459
# Unit test for function main
def test_main():
    assert main() is None
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:57:38.385070
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='/usr/bin/make_database.sh db_user db_name creates=/path/to/database',
        _uses_shell=False
    )
    module = AnsibleModule(**args)
    main()


# Generated at 2022-06-13 04:57:48.604995
# Unit test for function main
def test_main():
    args = 'echo "hello world"'

    result = main()
    assert result['hello world']


if __name__ == '__main__':
    main()

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.six import iteritems
from ansible.module_utils.six.moves import shlex_quote
from ansible.module_utils._text import to_bytes, to_native, to_text
from ansible.module_utils.six import PY2

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.common.collections import is_iterable
from ansible.module_utils.pycompat24 import get_exception
from ansible.module_utils.urls import open_url, ConnectionError, SSLValidationError


# Generated at 2022-06-13 04:57:59.788528
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 04:58:06.377543
# Unit test for function main
def test_main():
    """
    Unit test for function main
    """

# Generated at 2022-06-13 04:58:14.048511
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(),
            creates=dict(type='path'),
            removes=dict(type='path'),
            warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
            stdin=dict(required=False),
        ),
        supports_check_mode=True,
    )
    module.params['_raw_params'] = 'echo hello'
    main()
    module.params['_raw_params'] = 'echo hello world'
    main()
   

# Generated at 2022-06-13 04:58:26.306915
# Unit test for function check_command
def test_check_command():
    m = AnsibleModule(
        argument_spec = dict(
            remote_user = dict(required=False),
        ),
    )

# Generated at 2022-06-13 04:58:27.991346
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:58:32.912923
# Unit test for function main
def test_main():
    testcases = [('echo hello',
                  {'_raw_params': 'echo hello',
                   'argv': None,
                   'chdir': None,
                   'command': None,
                   'creates': None,
                   'executable': None,
                   'removes': None,
                   'stdin': None,
                   'stdin_add_newline': True,
                   'strip_empty_ends': True,
                   'warn': False,
                   '_uses_shell': False})]

    for cmd, params in testcases:
        with mock.patch.object(AnsibleModule, 'run_command') as mock_command:
            mock_command.return_value = (0, '', '')
            with mock.patch.object(AnsibleModule, 'exit_json') as mock_exit:
                mock_exit

# Generated at 2022-06-13 04:59:46.397709
# Unit test for function main
def test_main():
    assert True


# Generated at 2022-06-13 04:59:54.217569
# Unit test for function main

# Generated at 2022-06-13 05:00:01.352618
# Unit test for function main
def test_main():
    '''
    unit testing for main function
    '''
    r = {'changed': False, 'stdout': '', 'stderr': '', 'rc': None, 'cmd': None, 'start': None, 'end': None, 'delta': None, 'msg': ''}
    assert main(r) == None

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:00:03.911176
# Unit test for function main
def test_main():
    assert callable(main)


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:00:06.174370
# Unit test for function main
def test_main():
    # run main function (for coverage)
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:00:16.139915
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='cat /etc/motd',
        chdir='/',
        executable="/bin/sh -c"
    )
    result = dict(
        changed=False,
        cmd="cat /etc/motd",
        delta='0:00:00.001529',
        end='2017-09-29 22:03:48.084657',
        rc=0,
        start='2017-09-29 22:03:48.083128',
        stderr='',
        stdout='Clustering node rabbit@slave1 with rabbit@master …'
    )
    module = AnsibleModule(**args)
    assert main() == result


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:00:29.172372
# Unit test for function main
def test_main():
    #def run_command(self, cmd, executable=None, use_unsafe_shell=False, encoding=None, data=None, binary_data=False):

    #case 1: module called without any parameter
    empty_instance = AnsibleModule(argument_spec={})
    #unit test for path_exists_glob()
    #path_exists_glob() returns true if the path exists.
    #unit test for argv and args are empty, then rc should be 256
    args = ""
    argv = ""
    assert main(empty_instance, argv, args)['rc'] == 256, "test case 1 failed"
    
    #case 2: module called with argv
    argv_instance = AnsibleModule(argument_spec=dict(argv=dict(type='list', elements='str')))
    #unit

# Generated at 2022-06-13 05:00:35.622978
# Unit test for function check_command
def test_check_command():
    module = ansible.module_utils.basic.AnsibleModule('command', '')
    for command in ['chmod', 'chown', 'chgrp', 'ln', 'mkdir', 'rmdir', 'rm', 'touch', 'curl', 'wget', 'svn', 'service', 'mount', 'rpm', 'yum', 'apt-get', 'tar', 'unzip', 'sed', 'dnf', 'zypper', 'sudo', 'su', 'pbrun', 'pfexec', 'runas', 'pmrun', 'machinectl']:
        check_command(module, command.split())



# Generated at 2022-06-13 05:00:46.706864
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule({}, check_mode=False)

    check_command(module, "/path/to/mkdir arg1 arg2 arg3")
    assert module.deprecations == ["Consider using the file module with state=directory rather than running 'mkdir'"]

    module = AnsibleModule({}, check_mode=False)

    check_command(module, "/path/to/tar arg1 arg2 arg3")
    assert module.deprecations == ["Consider using the unarchive module rather than running 'tar'"]

    module = AnsibleModule({}, check_mode=False)

    check_command(module, ["command", "arg1", "arg2"])
    assert module.deprecations == []


# Generated at 2022-06-13 05:00:54.078500
# Unit test for function main