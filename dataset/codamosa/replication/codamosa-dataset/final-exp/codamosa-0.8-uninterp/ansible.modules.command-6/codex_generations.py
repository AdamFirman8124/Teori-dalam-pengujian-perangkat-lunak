

# Generated at 2022-06-13 04:52:18.001115
# Unit test for function main
def test_main():
    string = '{"changed": false, "stdout": "", "stderr": "", "rc": 1, "cmd": "echo hello", "start": null, ' \
             '"end": null, "delta": null, "msg": "non-zero return code", "warnings": ["Consider using the file ' \
             'module with state=directory rather than running \'mkdir\'.  If you need to use \'mkdir\' because the ' \
             'file module is insufficient you can add \'warn: false\' to this command task or set ' \
             '\'command_warnings=False\' in the defaults section of ansible.cfg to get rid of this message."]}'
    d = json.loads(string)
    assert(d == main())

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:52:21.133750
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleExitJson) as result:
        main()
    assert result.value.args[0]['rc'] == 0

# Generated at 2022-06-13 04:52:31.105242
# Unit test for function main
def test_main():
    import json
    import subprocess
    import sys
    import tempfile
    import time

    x = tempfile.mkdtemp()

    temp = tempfile.mkstemp()
    os.close(temp[0])
    tmpfilename = temp[1]

    olds = None
    old_stdin = None


# Generated at 2022-06-13 04:52:42.236533
# Unit test for function main
def test_main():
    args = dict(
        # _raw_params=dict(),
        _uses_shell=dict(type='bool', default=False),
        argv=dict(type='list', elements='str'),
        chdir=dict(type='path'),
        executable=dict(),
        creates=dict(type='path'),
        removes=dict(type='path'),
        # The default for this really comes from the action plugin
        warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
        stdin=dict(required=False),
        stdin_add_newline=dict(type='bool', default=True),
        strip_empty_ends=dict(type='bool', default=True),
    )
    result = {}

# Generated at 2022-06-13 04:52:42.788625
# Unit test for function check_command
def test_check_command():
    assert False



# Generated at 2022-06-13 04:52:52.716738
# Unit test for function main
def test_main():
    import platform
    import os

    argv = [
        "ansible-command",
        "id"
    ]
    # This code is really difficult to test on windows because it requires the
    # creation of a process, so we use a try except to skip the test on windows
    try:
        sys.argv = argv
        main()
    except Exception:
        if platform.system() == 'Windows':
            return
        else:
            raise
    finally:
        sys.argv = old_argv

# ansible requires this name to work
main()

# Generated at 2022-06-13 04:53:05.260249
# Unit test for function main

# Generated at 2022-06-13 04:53:16.654878
# Unit test for function check_command
def test_check_command():
    from ansible.utils.display import Display
    display = Display()

    class TestModule(object):
        def __init__(self):
            self.warnings = []
            self.params = {}

        def fail_json(self, **kwargs):
            output = kwargs['msg']
            errors = kwargs['exception'].args[0]
            raise RuntimeError(output, errors)

        def exit_json(self, *args, **kwargs):
            return

        def set_fact(self, *args, **kwargs):
            return

        def warn(self, msg):
            self.warnings.append(msg)

    module = TestModule()

    check_command(module, '/bin/bash')
    check_command(module, 'curl')
    check_command(module, 'wget')

# Generated at 2022-06-13 04:53:21.757879
# Unit test for function main
def test_main():
    fake_module = object()
    fake_command_line = ['/usr/bin/python', '/tmp/test_file.txt']
    main(fake_module, fake_command_line)

# Generated at 2022-06-13 04:53:33.561225
# Unit test for function main
def test_main():
    param_functions = {'make_module_args': make_module_args,
                       '_extract_arg_keys': _extract_arg_keys}
    module, exit_args_list, fail_args_list, skip_args_list = \
            control_flow_utils.get_function_arguments(main, param_functions)

    # Fail module when option 'creates' has value that is not present
    args = make_module_args(creates='/tmp/test', target_hosts='localhost')
    control_flow_utils.fail(module, exit_args_list, fail_args_list, args)

    # Fail module when option 'removes' has value that is not present
    args = make_module_args(removes='/tmp/test', target_hosts='localhost')
    control_flow

# Generated at 2022-06-13 04:53:58.913620
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='tail -3 /var/log/audit/audit.log',
        chdir=None,
        executable=None,
        creates=None,
        removes=None,
        warn=False,
        stdin=None,
        strip_empty_ends=True,
    )
    r = dict(
        cmd=['tail', '-3', '/var/log/audit/audit.log'],
        end=None,
        start=None,
        changed=False,
        delta=None,
        msg='non-zero return code',
        rc=None,
        stderr='',
        stdout='',
    )

# Generated at 2022-06-13 04:54:07.443499
# Unit test for function main
def test_main():
    args = dict(
        command = '/bin/echo "hello world"',
        register = 'my_cmd'
    )
    r = ansible_runner.run(ansible_runner.CommandLine('command', 'ansible-runner.tests.unit.test_command_module', 'unittest'),
                           private_data_dir='data',
                           job_vars=args,
                           )
    assert r.private_data_dir is not None
    assert r.is_successful()
    assert r.event_data == {'stdout': 'hello world\n', 'stdout_lines': ['hello world'], 'stderr': '', 'stderr_lines': [], 'rc': 0, 'changed': True, 'msg': 'non-zero return code', 'cmd': '/bin/echo "hello world"'}


# Generated at 2022-06-13 04:54:19.907558
# Unit test for function main

# Generated at 2022-06-13 04:54:27.113761
# Unit test for function main
def test_main():
    # Mock class used to mock the ansible module and it's results
    class AnsibleModuleMock():
        # mock params
        def __init__(self, argument_spec=None, check_invalid_arguments=None,
                     bypass_checks=None, no_log=None,
                     check_extras=None, mutually_exclusive=None,
                     required_together=None, required_one_of=None,
                     add_file_common_args=None, supports_check_mode=None,
                     required_if=None, required_by=None):
            self.params = {}
            self.check_mode = False

        # mock fail_json
        def fail_json(self, **kwargs):
            self.exit_args = kwargs
            self.exit_args['failed'] = True

# Generated at 2022-06-13 04:54:28.512606
# Unit test for function check_command
def test_check_command():
    args = ["/bin/foo"]
    command = os.path.basename(args[0])
    assert command == "foo"



# Generated at 2022-06-13 04:54:34.722159
# Unit test for function main
def test_main():
    # If you need to setup additional things...
    # If you need to remove the files created by main()
    # Remove if not needed
    # look at the below
    # filelist = glob.glob(os.path.join(os.environ.get('HOME'),'test'))
    # for f in filelist:
    #     os.remove(f)
    # call the function with the args and kwargs you want
    main()


# Generated at 2022-06-13 04:54:43.709820
# Unit test for function main
def test_main():
    r = {'changed': False, 'stdout': '', 'stderr': '', 'rc': None, 'cmd': None, 'start': None, 'end': None, 'delta': None, 'msg': ''}
    args = ['/bin/echo', '-n', 'hello']
    check_command('command', args)
    assert args == ['/bin/echo', '-n', 'hello']
    args = ['sudo', 'apt-get', 'install', 'python3-numpy']
    check_command('command', args)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:54:45.934740
# Unit test for function check_command
def test_check_command():
    assert check_command == '1'


# Generated at 2022-06-13 04:54:57.567893
# Unit test for function main

# Generated at 2022-06-13 04:55:08.072811
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils.common.collections import is_iterable
    import inspect
    import json
    import os
    import pip
    import shutil
    import subprocess
    import sys
    import time
    import traceback
    import yaml

    try:
        from __main__ import display
    except ImportError:
        from ansible.utils.display import Display
        display = Display()

    # Find the test directory
    test_dir = os.path.dirname(os.path.realpath(__file__))
    test_data_dir = os.path.join(test_dir, 'test_data')

# Generated at 2022-06-13 04:55:25.016705
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(default="command test"),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(),
            creates=dict(type='path'),
            removes=dict(type='path'),
            warn=dict(type='bool', default=False),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        ),
        supports_check_mode=True
    )


# Generated at 2022-06-13 04:55:38.286571
# Unit test for function main
def test_main():
    test_module_data = dict(
        _raw_params='/bin/echo hello',
        argv=dict(type='list', elements='str'),
        chdir=dict(type='path'),
        executable=dict(),
        creates=dict(type='path'),
        removes=dict(type='path'),
        # The default for this really comes from the action plugin
        warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
        stdin=dict(required=False),
        stdin_add_newline=dict(type='bool', default=True),
        strip_empty_ends=dict(type='bool', default=True),
    )

# Generated at 2022-06-13 04:55:48.535406
# Unit test for function check_command
def test_check_command():
    # command line is a list
    command1 = ['/usr/bin/wget', 'www.getansible.com']
    #command line is a string
    command2 = '/usr/bin/wget www.getansible.com'
    command3 = 'svn co http://svn.apache.org/repos/asf/httpd/httpd/trunk/docs/'
    command4 = 'yum clean all'
    command5 = 'dnf clean all'
    command6 = 'zypper ref'
    command7 = 'rpm -q httpd'
    command8 = 'apt-get install nginx'
    command9 = 'tar xfz foo.tar.gz'
    command10 = 'unzip foo.zip'
    command11 = 'sed -i s/foo/bar/g file1'


# Generated at 2022-06-13 04:55:55.392579
# Unit test for function main
def test_main():

    from ansible_collections.ansible.builtin.tests.unit.compat.mock import patch, Mock
    from ansible_collections.ansible.builtin.tests.unit.modules.utils import set_module_args


# Generated at 2022-06-13 04:56:03.421907
# Unit test for function main
def test_main():
    m = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(type='str', default='echo hi'),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(type='str'),
            creates=dict(type='path'),
            removes=dict(type='path'),
            warn=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
    )
    try:
        main()
    except SystemExit as e:
        print(e)
    return

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:08.042208
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module.check_mode = False
    import sys
    if sys.version_info[0] < 3:
        module.run_command = lambda args, **kwargs: (0, "", "")
    else:
        module.run_command = lambda args, **kwargs: (0, b"", b"")
    assert module.check_mode == False
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:15.104692
# Unit test for function main
def test_main():
    test_args = ['test/test-units/test_command/test_command_no_parameters.json']
    with test_lib.mocked_call(glob, 'glob', None):
        with test_lib.mocked_call(os, 'chdir', None):
            with test_lib.mocked_call(datetime, 'datetime', None):
                with test_lib.mocked_call(os, 'get_exe_link', b'/bin/bash'):
                    with test_lib.mocked_call(os, 'path', None):
                        test_lib.run_ansible_module(test_args)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:26.766154
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(
        argument_spec = dict(),
    )
    assert check_command(module, 'touch /tmp/test_file') == None
    assert check_command(module, 'service mysqld start') == None
    assert check_command(module, 'cp /tmp/test_file /etc/test_file') == None
    assert check_command(module, 'mount /dev/sdb1 /mnt/mysdb') == None
    assert check_command(module, 'rpm -Uvh package.rpm') == None
    assert check_command(module, 'zypper install -y mysql') == None
    assert check_command(module, 'su -c id') == None
    assert check_command(module, 'sed -i s/foo/bar/g /tmp/test_file') == None



# Generated at 2022-06-13 04:56:36.545963
# Unit test for function main
def test_main():
    import inspect
    import sys
    import tempfile

    # Include parent directory for AnsibleModule
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
    from ansible_module import AnsibleModule

    # Fake args
    args = {}
    args['executable'] = None
    args['argv'] = None
    args['creates'] = None
    args['removes'] = None
    args['warn'] = False

    module_args = "echo hello"

    # Create temp file
    tmp_fd, tmp_pathname = tempfile.mkstemp()

    # Write to temp file
    tmp_file = os.fdopen(tmp_fd, 'w+')
    tmp_file.write("hello")
    tmp_file.close()

   

# Generated at 2022-06-13 04:56:45.941123
# Unit test for function main
def test_main():
    args = {}
    if sys.platform == 'win32':
        args['_raw_params'] = 'dir'
    else:
        args['_raw_params'] = 'ls'
        args['executable'] = '/bin/echo'
    result = main(args)
    assert type(result) is dict
    assert result['changed'] == True
    assert result['cmd'] == args['_raw_params']
    if sys.platform.startswith("linux"):
        assert result['rc'] == os.EX_OK
    else:
        assert result['rc'] == 0
    assert result['start'] is not None
    assert result['end'] is not None
    assert result['delta'] is not None
    assert result['stdout'] is not None
    assert result['stderr'] == ''


# Generated at 2022-06-13 04:57:02.462150
# Unit test for function main
def test_main():
  args = { '_raw_params': '', '_uses_shell': True, 'argv': [ '/usr/bin/echo', 'hello' ], 'chdir': '/tmp', 'executable': None, 'creates': '', 'removes': '', 'warn': True, 'stdin': '', 'stdin_add_newline': True, 'strip_empty_ends': True}
  r = main(args)
  print (r)


if __name__ == '__main__':
  test_main()

# Generated at 2022-06-13 04:57:12.517177
# Unit test for function main

# Generated at 2022-06-13 04:57:19.001495
# Unit test for function check_command
def test_check_command():
    args = dict(free_form="foo bar", warn=True)
    module = AnsibleModule(argument_spec=args)
    check_command(module, ["foo", "bar"])
    assert len(module.warnings) == 1
    assert 'Ansible is maintaining this command as a deprecated feature' in module.warnings[0]
    check_command(module, ["foo", "bar"])
    assert len(module.warnings) == 1



# Generated at 2022-06-13 04:57:32.607404
# Unit test for function main

# Generated at 2022-06-13 04:57:41.500783
# Unit test for function main

# Generated at 2022-06-13 04:57:48.759051
# Unit test for function main
def test_main():
    class MockModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs

        def fail_json(self, **kwargs):
            pass

        def exit_json(self, **kwargs):
            pass

        def run_command(self, *args, **kwargs):
            return 0, 'Skipped', ''

        def warn(self, *args, **kwargs):
            pass

    m = MockModule(args='foo', _raw_params='echo foo', _uses_shell=False)
    main()
    main()
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:57:55.490755
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    for command in ['chown', 'chmod', 'chgrp']:
        check_command(module, [command])
        check_command(module, command)
    for command in ['ln', 'mkdir', 'rmdir', 'rm', 'touch']:
        check_command(module, [command])
        check_command(module, command)
    for command in ['curl', 'wget']:
        check_command(module, [command])
        check_command(module, command)
    for command in ['svn']:
        check_command(module, [command])
        check_command(module, command)
    for command in ['service']:
        check_command(module, [command])
        check_command(module, command)

# Generated at 2022-06-13 04:58:06.505131
# Unit test for function main
def test_main():
    import os

    import tempfile

    mydir = os.path.dirname(os.path.realpath(__file__))
    print(mydir)
    file = open(mydir + '/test.yml', 'w')
    file.write('---\n- hosts: localhost\n  tasks:\n    - name: Return motd to registered var\n      ansible.builtin.command: cat /etc/motd\n      register: mymotd')
    file.close()
    file = open(mydir + '/test_ansible.cfg', 'w')
    file.write('[defaults]\nhost_key_checking = False\nforks = 1')
    file.close()
    file = open(mydir + '/test_hosts', 'w')
    file.write('localhost')
    file

# Generated at 2022-06-13 04:58:14.152384
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(type='str'),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(type='list', elements='str'),
            chdir=dict(type='path'),
            executable=dict(),
            creates=dict(type='path'),
            removes=dict(type='path'),
            # The default for this really comes from the action plugin
            warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 04:58:26.372934
# Unit test for function main

# Generated at 2022-06-13 04:58:45.633347
# Unit test for function main
def test_main():
    test = {
        "params": {
            "_raw_params": "ls",
            "argv": "ls",
            "chdir": ".",
            "creates": ".",
            "executable": ".",
            "removes": ".",
            "_uses_shell": False,
            "msg": "",
            "rc": 0,
            "start": None,
            "end": None,
            "delta": None,
            "stdout": "",
            "stderr": ""
        },
        "_ansible_check_mode": False
    }
    try:
        main()
    except SystemExit as e:
        assert e.code == 0

# Generated at 2022-06-13 04:58:46.824955
# Unit test for function main
def test_main():
    # Put unit tests for main here
    assert True

# Generated at 2022-06-13 04:58:54.875006
# Unit test for function main
def test_main():
    test_name = "test_main"
    global module, shell, chdir, executable, args, argv, creates, removes, warn, stdin, stdin_add_newline, strip
    r = {}
    # tests of the function main
    module.warn("As of Ansible 2.4, the parameter 'executable' is no longer supported with the 'command' module. Not using '%s'." % executable)

    r['rc'] = 0
    r['cmd'] = args
    if warn:
        # nany telling you to use module instead!
        check_command(module, args)

    if chdir:
        chdir = to_bytes(chdir, errors='surrogate_or_strict')
    # check_mode partial support, since it only really works in checking creates/removes

# Generated at 2022-06-13 04:59:07.704372
# Unit test for function main

# Generated at 2022-06-13 04:59:20.385873
# Unit test for function main
def test_main():
    # Pulls in the real AnsibleModule due to the way that unittest works
    # pylint: disable=redefined-outer-name
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 04:59:25.701793
# Unit test for function check_command
def test_check_command():
    fake = {'warn' : lambda *args: None}
    check_command(fake, "chown")
    check_command(fake, ["chown", "/some/path"])
    check_command(fake, "tar")
    check_command(fake, ["tar", "zxvf", "/some/path"])
    check_command(fake, "chown")
    check_command(fake, ["chown", "/some/path"])
    check_command(fake, "tar")
    check_command(fake, ["tar", "zxvf", "/some/path"])


# Generated at 2022-06-13 04:59:37.311926
# Unit test for function main
def test_main():
    failed = False
    args = {"_uses_shell": False,
            "_raw_params": "ls -al /var/log/",
            "chdir": "",
            "executable": None,
            "creates": "",
            "removes": "",
            "warn": False,
            "stdin": None,
            "stdin_add_newline": True,
            "strip_empty_ends": True,
            "argv": []}

# Generated at 2022-06-13 04:59:41.837600
# Unit test for function main
def test_main():
    args = {'chdir': '', 'executable': '', 'args': '/usr/bin/make_database.sh db_user db_name',
        'creates': '/path/to/database', 'removes': '', 'warn': False, 'stdin': '',
        'stdin_add_newline': True, 'strip_empty_ends': True}


# Generated at 2022-06-13 04:59:51.434367
# Unit test for function main
def test_main():
    # Test module arguments
    module_args_0 = dict(
        executable='/bin/sh',
        _raw_params='/etc/init.d/apache2 restart',
        chdir='/etc/init.d',
        creates='/tmp/logfile',
        removes='/etc/init.d/apache2'
    )
    module_args_1 = dict(
        executable='/bin/sh',
        argv='/etc/init.d/apache2 restart',
        chdir='/etc/init.d',
        creates='/tmp/logfile',
        removes='/etc/init.d/apache2'
    )

# Generated at 2022-06-13 04:59:57.252741
# Unit test for function main
def test_main():
    import sys
    import os
    import pytest
    import tempfile
    TEST = """
- name: Return motd to registered var
  ansible.builtin.command: cat /etc/motd
  register: mymotd
"""
    with tempfile.NamedTemporaryFile(mode='w+') as temp_file:
        temp_file.write(TEST)
        temp_file.seek(0)
        sys.argv.append('--args')
        sys.argv.append('@{}'.format(temp_file.name))
        import ansible.modules.commands.command as command
        command.main()


# Generated at 2022-06-13 05:00:31.655820
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
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
    result

# Generated at 2022-06-13 05:00:40.354273
# Unit test for function main
def test_main():
    # test for checking the error messages
    module = AnsibleModule(
        argument_spec={
            "_raw_params": {'required': False, 'type': 'str'},
            "argv": {'required': False, 'type': 'list', 'elements': 'str'},
        }
    )
    # args and argv both given
    with pytest.raises(SystemExit):
        main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:00:48.902206
# Unit test for function main
def test_main():
    import os, sys, shutil
    test_dir = os.path.join(os.path.dirname(__file__), '..', 'test')
    test_proj_dir = os.path.join(test_dir, 'test-ansible-projects')
    shutil.copytree(os.path.join(test_dir, 'test-ansible-projects-source'), test_proj_dir)
    test_playbook_path = os.path.join(test_proj_dir, 'test-playbook.yml')
    os.chdir(test_proj_dir)

    # Import global
    from ansible.module_utils.basic import AnsibleModule, HAS_SELINUX, syslog


# Generated at 2022-06-13 05:00:55.411215
# Unit test for function main

# Generated at 2022-06-13 05:00:55.934973
# Unit test for function check_command
def test_check_command():
    assert True



# Generated at 2022-06-13 05:01:07.445299
# Unit test for function main
def test_main():
    from ansible.modules.commands.command import main


# Generated at 2022-06-13 05:01:14.516955
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
            # The default for this really comes from the action plugin
            warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        )
    )
   

# Generated at 2022-06-13 05:01:16.184895
# Unit test for function main
def test_main():
    out = main()
    assert out is None

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:01:23.202004
# Unit test for function main
def test_main():
    import doctest
    from ansible.module_utils import glob
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import env_fallback
    from ansible.module_utils.six import BytesIO
    import difflib
    import os
    import re
    import sys
    import time
    import datetime
    import json

    if not AnsibleModule:
        print("network module not supported in this ansible version")
        exit()

    sys.path.append("utils")
    import ansible_helpers
    import ansible_mod_init

    test_dir = os.path.dirname(__file__)
    if test_dir == '':
        test_dir = '.'
    test_dir += '/tests'

# Generated at 2022-06-13 05:01:31.879542
# Unit test for function main
def test_main():
    args = {}
    args['_raw_params'] = 'echo hello'
    args['_uses_shell'] = False
    args['argv'] = ['echo', 'hello']
    args['chdir'] = '/'
    args['executable'] = None
    args['creates'] = None
    args['removes'] = None
    args['warn'] = False
    args['stdin'] = None
    args['stdin_add_newline'] = True
    args['strip_empty_ends'] = True
    r = {}
    r['changed'] = False
    r['stdout'] = ''
    r['stderr'] = ''
    r['rc'] = None
    r['cmd'] = None
    r['start'] = None
    r['end'] = None
    r['delta'] = None
    r