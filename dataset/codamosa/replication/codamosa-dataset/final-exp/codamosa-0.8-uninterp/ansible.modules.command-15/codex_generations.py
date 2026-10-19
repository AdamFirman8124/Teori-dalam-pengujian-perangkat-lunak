

# Generated at 2022-06-13 04:52:18.090145
# Unit test for function check_command
def test_check_command():
    testname = 'test_check_command'
    cmd = 'command'
    cmd_list = ['command']
    m = AnsibleModule(
        argument_spec = dict(
            warn = dict(type='bool', default=True)
        ),
        supports_check_mode=True
    )
    check_command(m, cmd)
    check_command(m, cmd_list)
    with pytest.raises(SystemExit):
        m.fail_json(msg='An error occurred')
    out = m.exit_json()

# Generated at 2022-06-13 04:52:29.251214
# Unit test for function main
def test_main():
    args = ["ansible-playbook", "-i", "inventories/test/hosts",
            "library/command-test/command-test.yml",
            "-e", "command=command",
            "--list-tasks"]

    # Capture the output of ansible-playbook.
    process = subprocess.Popen(args, stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)
    stdout, stderr = process.communicate()
    # Convert to str if needed.
    if isinstance(stdout, bytes):
        stdout = stdout.decode()
    if isinstance(stderr, bytes):
        stderr = stderr.decode()


# Generated at 2022-06-13 04:52:41.441149
# Unit test for function main
def test_main():
    test_dict = {
        "chdir": "../",
        "executable": None,
        "creates": "../some_file",
        "removes": "../some_file",
        "warn": False,
        "stdin": None,
        "stdin_add_newline": True,
        "strip_empty_ends": True
    }
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 04:52:46.698409
# Unit test for function main
def test_main():
    args = {}
    args.update({'executable': '/usr/bin/touch', 'removes': 'test/testfile', 'creates': 'test/testfile', '_raw_params': '-m', 'chdir': 'test'})
    module = AnsibleModule(argument_spec=args)
    idem_module = AnsibleModule(argument_spec=args)

    check_command(module, "touch -m")
    check_command(idem_module, "touch -m")

    x = main()
    assert x['changed'] is True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:52:49.630020
# Unit test for function check_command
def test_check_command():
    assert check_command(AnsibleModule, ['chown']) == None


# ===========================================
# Main control flow


# Generated at 2022-06-13 04:53:02.569621
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule({}, check_mode=True)
    assert check_command(module, '/bin/ls') is None
    assert check_command(module, '/bin/mv') is None
    assert check_command(module, '/bin/ln') is None
    assert check_command(module, '/bin/chown') is None
    assert check_command(module, '/bin/chgrp') is None
    assert check_command(module, '/bin/chmod') is None
    assert check_command(module, '/bin/mkdir') is None
    assert check_command(module, '/bin/rmdir') is None
    assert check_command(module, '/bin/rm') is None
    assert check_command(module, '/bin/touch') is None
    assert check_command(module, '/usr/bin/curl')

# Generated at 2022-06-13 04:53:06.675755
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec = {})
    check_command(module, "/usr/bin/chmod 644 {{ myfile }}")
    check_command(module, "/usr/bin/mkdir -p /etc/ansible/roles/")
    check_command(module, "/usr/bin/curl https://www.example.com")
    check_command(module, ["/usr/bin/curl", "https://www.example.com"])
    check_command(module, ["/usr/bin/curl", "https://www.example.com"])
    check_command(module, "/usr/bin/ln -sf /usr/bin/python3 /usr/bin/python")
    check_command(module, "/usr/bin/rpm -q --whatprovides systemd")

# Generated at 2022-06-13 04:53:17.718386
# Unit test for function main
def test_main():
    args = dict(
        args='ls'
    )
    result = {
        "rc": 0,
        "stdout": "skipped, since /tmp/foo does not exist",
        "end": "2018-04-09 15:36:38.560770",
        "cmd": "ls",
        "msg": "Did not run command since '/tmp/foo' does not exist",
        "stdout_lines": ["skipped, since /tmp/foo does not exist"],
        "changed": True,
        "start": "2018-04-09 15:36:38.560770",
        "delta": "0:00:00.000242"
    }
    res = main()
    assert res == result




if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 04:53:30.955123
# Unit test for function main
def test_main():
    import os
    import sys
    import platform
    import pytest
    from test.units.modules.utils import set_module_args

    if platform.system() != 'Windows':
        # Currently this test breaks on Windows, as it will copy a test file
        # To be fixed in future
        test_dir = os.path.dirname(os.path.dirname(__file__))
        sys.path.append(test_dir)
        test_file = os.path.normpath(os.path.join(test_dir, '../../lib/ansible/modules/packaging/os/yum.py'))
        set_module_args(dict(warn=True, argv=[test_file]))
        yum = pytest.importorskip('ansible.modules.packaging.os.yum')

# Generated at 2022-06-13 04:53:38.316751
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec=dict())
    check_command(module, "touch somefile")
    assert module.warnings[0].startswith("Consider using the file module with state=touch")
    # Reset warnings
    del module.warnings[:]
    check_command(module, "somefile")
    assert not module.warnings[0].startswith("Consider using the file module with state=touch")



# Generated at 2022-06-13 04:54:01.327866
# Unit test for function main
def test_main():
    main()

# Entry point for script
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:54:10.600790
# Unit test for function main
def test_main():
  arguments = {'_raw_params':'echo  "abc"', '_uses_shell':'False', 'argv':'[, echo ,"abc"]', 'chdir':'chdir/', 'executable':'executable/', 'creates':'creates/', 'removes':'removes/',  'warn':'False', 'stdin':'stdin/', 'stdin_add_newline':'True', 'strip_empty_ends':'True'}

# Generated at 2022-06-13 04:54:17.366335
# Unit test for function check_command
def test_check_command():
    m = AnsibleModule(
        argument_spec = dict(
            command = dict(required=True, type='str'),
        ),
        supports_check_mode=True,
    )
    result = check_command(m, ('/bin/yum', 'install'))
    assert result is None
    result = check_command(m, ['/bin/yum', 'install'])
    assert result is None



# Generated at 2022-06-13 04:54:25.506199
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    # The arguments that would be sent to the module
    module_args = dict(
        _raw_params='echo hello',
        _uses_shell=False,
        chdir='somedir/',
        executable=None,
        creates=None,
        removes=None,
        warn=True,
        stdin=None,
        stdin_add_newline=True,
        strip_empty_ends=True
    )
    # Instantiate our module, passing all but one of the parameters (that
    # one will be sent separately)
    module = AnsibleModule(**module_args)
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:54:37.743703
# Unit test for function main
def test_main():
    # Given
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
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
        supports_check_mode=True,
    )
    shell = module.params['_uses_shell']

# Generated at 2022-06-13 04:54:44.339825
# Unit test for function main
def test_main():
    # test 1
    r = main()
    assert r['msg'] == 'no command given'
    assert r['rc'] == 256

    # test 2
    r = main()
    assert r['msg'] == 'only command or argv can be given, not both'
    assert r['rc'] == 256

    # test 3
    r = main()
    assert r['msg'] == 'non-zero return code'
    assert r['rc'] == 0

    # test 4
    r = main()
    assert r['changed'] == True
    assert r['rc'] == 0

    # test 5
    r = main()
    assert r['msg'] == "Would not run command since '%s' exists" % creates
    assert r['rc'] == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:54:56.789152
# Unit test for function main

# Generated at 2022-06-13 04:55:07.560176
# Unit test for function main
def test_main():
    from ansible import context
    from ansible.utils.vars import combine_vars
    from ansible.utils.vars import combine_hash
    import ansible.module_utils.common.removed
    import ansible.module_utils.basic


# Generated at 2022-06-13 04:55:09.377299
# Unit test for function main
def test_main():
    """Unit test for function main"""
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:55:22.841577
# Unit test for function main

# Generated at 2022-06-13 04:55:51.868612
# Unit test for function check_command
def test_check_command():
    assert isinstance(check_command, object), 'check_command is not a function'


# Generated at 2022-06-13 04:56:02.214196
# Unit test for function main
def test_main():
    check_command(module, "/bin/mkdir -p /tmp/test")
    assert r['changed'] is True
    assert r['rc'] is 0
    assert r['cmd'] is ['/bin/mkdir', '-p', '/tmp/test']
    assert r['stdout'] is 'skipped, since /tmp/test does not exist'
    assert r['msg'] is 'Did not run command since \'/tmp/test\' does not exist'
    assert r['start'] is None
    assert r['end'] is None
    assert r['delta'] is None
    assert r['stderr'] is ''

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:15.190743
# Unit test for function main
def test_main():
    import sys
    import tempfile
    old_args, old_stdin = sys.argv, sys.stdin

    # We don't want to exit on failure as we are unit testing
    def exit_json(module, **args):
        return args

    # We don't want to exit on failure as we are unit testing
    def fail_json(module, **args):
        raise Exception(args['msg'])

    # Unit test this by checking that it tells us the correct shell to use
    def check_command(module, command):
        if 'cowsay' in command:
            raise Exception("cowsay not found")


# Generated at 2022-06-13 04:56:20.750530
# Unit test for function check_command
def test_check_command():
    class TestModule(object):
        def warn(self, msg):
            assert "file" in msg
            assert "chown" in msg

    test_command = "chown root /a/b/c"
    module = TestModule()
    check_command(module, test_command)



# Generated at 2022-06-13 04:56:29.716192
# Unit test for function main
def test_main():
    import mock
    import os
    import sys

    from ansible.module_utils.basic import AnsibleModule

    module = mock.MagicMock(spec=AnsibleModule)
    module.check_mode = False


# Generated at 2022-06-13 04:56:37.188583
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule({'command': 'touch foo'})  # dummy module
    check_command(module, 'touch foo')
    check_command(module, 'tar xvf foo.tar')
    check_command(module, 'tar xvf foo.tar bar')
    check_command(module, 'echo "foo"')
    check_command(module, 'mkdir foo')
    check_command(module, 'rpm -Uvh foo.rpm')
    check_command(module, 'yum install foo')
    check_command(module, 'apt-get install foo')
    check_command(module, 'service foo restart')
    check_command(module, 'mount /dev/foo /mnt')
    check_command(module, 'mount /dev/foo /mnt -t auto -o loop,ro')
   

# Generated at 2022-06-13 04:56:46.441425
# Unit test for function main
def test_main():
    import sys
    import tempfile
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    # Generate a testable AnsibleModule

# Generated at 2022-06-13 04:56:57.182041
# Unit test for function main

# Generated at 2022-06-13 04:57:04.660649
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec=dict())
    result = check_command(module, "chown root foo")
    assert result is None
    result = check_command(module, "chmod o+r foo")
    assert result is None
    result = check_command(module, "chgrp bar foo")
    assert result is None
    result = check_command(module, "ln -s foo bar")
    assert result is None
    result = check_command(module, "mkdir foo")
    assert result is None
    result = check_command(module, "rmdir foo")
    assert result is None
    result = check_command(module, "rm -f foo")
    assert result is None
    result = check_command(module, "touch foo")
    assert result is None

# Generated at 2022-06-13 04:57:06.708395
# Unit test for function main
def test_main():
    assert True == True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:58:02.479894
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:58:08.175561
# Unit test for function main
def test_main():
    import json
    import pytest
    import root_path
    import os
    import os.path
    import shutil
    import pytest_httppretty
    from ansible.module_utils.six import PY3

    if not PY3:
        pytest.skip("pytest_httpretty only works on Python 3")

    # need a fake module that can be serialized
    from ansible.utils import context_objects as co

    class FakeModule(object):
        def __init__(self, *args, **kwargs):
            self.params = kwargs

    curr_path = os.path.dirname(__file__)
    file_path = os.path.join(curr_path, 'fixtures', 'main.json')
    with open(file_path) as test_file:
        test_

# Generated at 2022-06-13 04:58:09.777005
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    check_command(module, 'curl')


# Generated at 2022-06-13 04:58:12.313064
# Unit test for function main
def test_main():
    # Disabled for now, as it's not working.
    pass

# Generated at 2022-06-13 04:58:19.998071
# Unit test for function main
def test_main():
    import ansible.modules.command.command as command
    content = ["find /etc -type f -name '*.yml'","find /etc -type f -name '*.yml'" ]
    module = AnsibleModule(argument_spec={})
    module.warn = MagicMock()
    r = {}
    for args in content:
        result = command.check_command(module, args)
        assert result == None

# Generated at 2022-06-13 04:58:28.609311
# Unit test for function main
def test_main():
    import os
    import sys
    import platform
    # in case we want to test loading the module directly
    if 'ANSIBLE_LOAD_CALLBACK_PLUGINS' in os.environ:
        sys.path.append(os.environ['ANSIBLE_LOAD_CALLBACK_PLUGINS'])
    if 'ANSIBLE_LOAD_CALLBACK_PLUGINS' in os.environ:
        sys.path.append("%s/lib/python%s.%s/site-packages/" % (os.environ['ANSIBLE_LOAD_CALLBACK_PLUGINS'], platform.python_version_tuple()[0], platform.python_version_tuple()[1]))

# Generated at 2022-06-13 04:58:39.700343
# Unit test for function main

# Generated at 2022-06-13 04:58:49.882874
# Unit test for function main
def test_main():
    # chdir test for directory
    mock_module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(default="test_command"),
            _uses_shell=dict(type='bool', default=False),
            argv=dict(),
            chdir=dict(),
            executable=dict(),
            creates=dict(),
            removes=dict(),
            warn=dict(type='bool', default=False),
            stdin=dict(),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        ),
        supports_check_mode=True
    )
    mock_run = MockExec()
    mock_run.results['rc'] = 0
    mock_run.results['stdout'] = ''
   

# Generated at 2022-06-13 04:58:55.181814
# Unit test for function main
def test_main():
    import tempfile

# Generated at 2022-06-13 04:59:08.053678
# Unit test for function main

# Generated at 2022-06-13 05:01:33.261970
# Unit test for function main
def test_main():
    module = ansible.module_utils.basic.AnsibleModule
    ansible.module_utils.basic.AnsibleModule.run_command = lambda *args, **kwargs: (0, 'successfull command', '')

# Generated at 2022-06-13 05:01:44.490255
# Unit test for function main
def test_main():
    args = dict(
      _raw_params='',
      _uses_shell=False,
      argv=['', ''],
      chdir=None,
      executable=None,
      creates=None,
      removes=None,
      # The default for this really comes from the action plugin
      warn=False,
      stdin=None,
      stdin_add_newline=True,
      strip_empty_ends=True
    )

# Generated at 2022-06-13 05:01:53.026484
# Unit test for function main
def test_main():
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import is_iterable
    command = "command"