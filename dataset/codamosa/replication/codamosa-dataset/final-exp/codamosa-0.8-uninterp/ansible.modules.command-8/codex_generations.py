

# Generated at 2022-06-13 04:52:23.140832
# Unit test for function check_command
def test_check_command():
    from units.compat import mock

    def argv_check_command(*args, **kwargs):
        return args

    def bytes_check_command(*args, **kwargs):
        return args


# Generated at 2022-06-13 04:52:32.590999
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
    main

# Generated at 2022-06-13 04:52:41.201912
# Unit test for function main
def test_main():
    def assert_equal(t1, t2):
        assert t1 == t2
    def assert_not_equal(t1, t2):
        assert t1 != t2
    def assert_is_instance(t, cls):
        assert isinstance(t, cls)
    def assert_true(t1):
        assert t1
    def assert_false(t1):
        assert not t1
    class AnsiColorsMock():
        def __init__(self):
            self.black = Mock(return_value="black")
            self.red = Mock(return_value="red")
            self.green = Mock(return_value="green")
            self.yellow = Mock(return_value="yellow")
            self.blue = Mock(return_value="blue")

# Generated at 2022-06-13 04:52:54.691430
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

# Generated at 2022-06-13 04:53:01.672790
# Unit test for function main
def test_main():
    args = {"_raw_params": "find /tmp", "_uses_shell": False, "argv": "find /tmp", "chdir": None, "executable": None, "creates": None, "removes": None, "warn": False, "stdin": None, "stdin_add_newline": True, "strip_empty_ends": True}

# Generated at 2022-06-13 04:53:12.172574
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import common
    from ansible.module_utils import connection
    from ansible.module_utils import helpers
    from ansible.module_utils import module_utils_loader
    import ansible.module_utils.network
    # print(ansible.module_utils.network)
    ansible.module_utils.network = None
    import ansible.module_utils.system
    # print(ansible.module_utils.system)
    ansible.module_utils.system = None
    import ansible.module_utils.urls
    ansible.module_utils.urls = None
    import ansible.module_utils.firewall
    # print(ansible.module_utils.firewall)
    ansible.module_utils.firewall = None
   

# Generated at 2022-06-13 04:53:24.121870
# Unit test for function main
def test_main():
    # Replace list of args with mock
    import sys
    import StringIO
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO.StringIO()

    test = AnsibleModule(
        argument_spec=dict(
            free_form=dict(),
            chdir=dict(),
            executable=dict(),
            creates=dict(),
            removes=dict(),
            warn=dict(type='bool', default=False),
            strip_empty_ends=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )

# Generated at 2022-06-13 04:53:35.663808
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule({})
    check_command(module, 'chown user /tmp/foo')
    check_command(module, 'chmod u+rwx /tmp/foo')
    check_command(module, 'chgrp group /tmp/foo')
    check_command(module, 'ln -s /tmp/foo /tmp/bar')
    check_command(module, 'mkdir -p /foo/bar')
    check_command(module, 'rmdir /tmp/foo')
    check_command(module, 'rm -rf /tmp/foo')
    check_command(module, 'curl http://example.com')
    check_command(module, 'wget http://example.com')
    check_command(module, 'svn co http://example.com')

# Generated at 2022-06-13 04:53:36.270575
# Unit test for function check_command
def test_check_command():
    return



# Generated at 2022-06-13 04:53:42.131335
# Unit test for function main
def test_main():
    args = [
        "/bin/strlen",
        "something"
    ]

# Generated at 2022-06-13 04:54:02.396360
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={})
    module.params = {
        'chdir': '~',
        'executable': '/usr/bin/python',
        '_raw_params': 'echo hello',
        'creates': '/tmp/a',
        'removes': '/tmp/b',
        'warn': True,
        'stdin': 'data',
        'stdin_add_newline': True,
        'strip_empty_ends': True,
    }

    r = {
        'changed': False,
        'rc': None,
        'start': None,
        'end': None,
        'delta': None,
    }

    assert(r == main())

# Generated at 2022-06-13 04:54:13.304230
# Unit test for function main
def test_main():
    myContent = {
        "msg": "",
        "start": None,
        "end": None,
        "delta": None,
        "stdout": "",
        "stderr": "",
        "rc": 0,
        "cmd": [],
        "changed": False,
    }
    result = {"ansible_facts": {}, "changed": True, "failed": True, "msg": "Unsupported parameters for (command) module: executable"}
    # default param
    ret = main()
    assert ret == result, "Failure test_main"

# Generated at 2022-06-13 04:54:15.095932
# Unit test for function main
def test_main():
    args = {'_raw_params': 'otherstuff'}
    result = main(args)
    assert result['cmd'] == 'otherstuff'


# Generated at 2022-06-13 04:54:24.532869
# Unit test for function main
def test_main():
    """
    Unit test for function main
    """
    class AnsibleModule:
        def __init__(self, argument_spec=None, supports_check_mode=False):
            self.argument_spec = argument_spec
            self.supports_check_mode = supports_check_mode
            self.check_mode = False
            self.params = {'_raw_params': '', 'argv': '', 'chdir': '', 'creates': '', 'removes': '', 'warn': False, 'stdin': '', 'stdin_add_newline': True, 'strip_empty_ends': True, '_uses_shell': False}

        def fail_json(self, rc, msg):
            if rc == 0:
                print('[PASS]')
            else:
                print('[FAIL]')
               

# Generated at 2022-06-13 04:54:36.133608
# Unit test for function main
def test_main():
    my_args = dict(
        chdir='tests',
        args="echo Hello"
    )
    import tempfile
    in_dir = tempfile.mkdtemp(prefix="test_ansible_")
    os.mkdir(os.path.join(in_dir, "tests"))
    with open(os.path.join(in_dir, "test_ansible_command.py"), "w") as f:
        f.write("""from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.modules.commands.command import main

if __name__ == '__main__':
    main(args={}, new_stdin=None)""".format(my_args))
    from ansible.plugins.loader import action_loader

# Generated at 2022-06-13 04:54:40.887741
# Unit test for function main
def test_main():
    # get the module so we can monkey patch output for unit tests
    module = AnsibleModule(argument_spec=dict(
        _raw_params=dict(),
        _uses_shell=dict(type='bool', default=False),
        argv=dict(type='list', elements='str'),
        chdir=dict(type='path'),
        executable=dict(),
        creates=dict(type='path'),
        removes=dict(type='path'),
        warn=dict(type='bool', default=False),
    ))
    # monkey patching so we don't get a SystemExit
    module.exit_json = lambda **kwargs: kwargs
    module.fail_json = lambda **kwargs: kwargs

    # test with just command
    output = main()
    assert output['rc'] == 256

# Generated at 2022-06-13 04:54:45.582122
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils.basic import AnsibleModule
    check_command(AnsibleModule({}), ['ls'])



# Generated at 2022-06-13 04:54:57.299812
# Unit test for function main
def test_main():
    sample_args = {'_raw_params': 'cat /etc/motd', '_uses_shell': False, 'argv': ['cat', '/etc/motd'], 'chdir': '/etc', 'executable': '', 'creates': '', 'removes': '', 'warn': False, 'stdin': '', 'stdin_add_newline': True, 'strip_empty_ends': True}

# Generated at 2022-06-13 04:55:08.013427
# Unit test for function main

# Generated at 2022-06-13 04:55:21.882258
# Unit test for function main

# Generated at 2022-06-13 04:55:50.099666
# Unit test for function main
def test_main():
    testargs = dict(
        _raw_params="cd /tmp && ls -l",
        _uses_shell=False,
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
    print(main(testargs))

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:55:56.118290
# Unit test for function main
def test_main():
  # Arrange
  args = {
            "_raw_params": "",
            "_uses_shell": False,
            "argv": "cat /etc/motd",
  }

# Generated at 2022-06-13 04:56:04.435155
# Unit test for function main

# Generated at 2022-06-13 04:56:10.602356
# Unit test for function main

# Generated at 2022-06-13 04:56:22.371282
# Unit test for function main

# Generated at 2022-06-13 04:56:30.655887
# Unit test for function check_command
def test_check_command():
    import ansible.module_utils.basic
    args = dict(
        cmd="echo",
    )

# Generated at 2022-06-13 04:56:33.469027
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True,
    )
    # This is the internal name of the command module
    # Just make sure we can pass it through the module framework
    main()
    main()

# Generated at 2022-06-13 04:56:44.250407
# Unit test for function main
def test_main():
    args = 'hostname'

# Generated at 2022-06-13 04:56:50.556518
# Unit test for function main
def test_main():
    print('Function main called with argument: %s' % sys.argv[1])
    print('Unit test for function main, test_main()')
    print('Argument validation done')
    print('If clause executed: %s' % sys.argv[1])
    print('Variable shell is created and initialized with value: %s' % sys.argv[1])
    print('Variable chdir is created and initialized with value: %s' % sys.argv[2])
    print('Variable executable is created and initialized with value: %s' % sys.argv[3])
    print('Variable args is created and initialized with value: %s' % sys.argv[4])
    print('Variable argv is created and initialized with value: %s' % sys.argv[5])

# Generated at 2022-06-13 04:56:59.185834
# Unit test for function main
def test_main():
    with tempfile.NamedTemporaryFile() as command_output:
        with tempfile.NamedTemporaryFile() as command_env:
            test_command_output = command_output.name
            test_command_env = command_env.name
            command_output.close()
            command_env.close()
            with open(test_command_env, 'w') as f:
                f.write('{"changed": false, "rc": 0, "stderr": "", "stdout": "Hello world"}')

# Generated at 2022-06-13 04:57:41.326334
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    check_command(module, "foo")
    check_command(module, ["foo"])



# Generated at 2022-06-13 04:57:47.742746
# Unit test for function check_command
def test_check_command():
    """This is a test for check_command"""
    module = AnsibleModule(argument_spec=dict())
    assert check_command(module, ["curl"]) is None
    assert check_command(module, "curl") is None
    assert check_command(module, "sudo curl") is None
    assert check_command(module, ["sudo", "curl"]) is None
    assert check_command(module, "curl --fail -s -f 'http://localhost:8080/' -o /dev/null") is None

# ===========================================
# Main control flow


# Generated at 2022-06-13 04:57:49.446366
# Unit test for function main
def test_main():
    assert True  # TODO: Implement unit test for function main

# Generated at 2022-06-13 04:58:00.615909
# Unit test for function check_command
def test_check_command():
    # stub module to pass to check_command
    class ModuleStub(object):

        def __init__(self):
            self.warnings = []

        def warn(self, msg):
            self.warnings.append(msg)

    module = ModuleStub()

    # Test individual commands
    check_command(module, 'chown')
    assert len(module.warnings) == 1
    assert 'Consider using the file module with owner rather than' in module.warnings[0]

    module = ModuleStub()
    check_command(module, 'chmod')
    assert len(module.warnings) == 1
    assert 'Consider using the file module with mode rather than' in module.warnings[0]

    module = ModuleStub()
    check_command(module, 'chgrp')

# Generated at 2022-06-13 04:58:04.749973
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    check_command(module, ['curl', 'http://www.example.com/'])
    assert len(module.warnings) == 1
    check_command(module, ['ln', '-s', 'source', 'dest'])
    assert len(module.warnings) == 2
    check_command(module, ['sudo', 'su'])
    assert len(module.warnings) == 3


# Generated at 2022-06-13 04:58:05.530211
# Unit test for function check_command
def test_check_command():
    pass



# Generated at 2022-06-13 04:58:13.722019
# Unit test for function main
def test_main():
    # Test the case where try:
    #     os.chdir(chdir)
    # except (IOError, OSError) as e:
    #     r['msg'] = 'Unable to change directory before execution: %s' % to_text(e)
    #     module.fail_json(**r) has no exception
    args = {
        "_raw_params": "",
        "_uses_shell": False,
        "argv": "",
        "chdir": "",
        "executable": "",
        "creates": "",
        "removes": "",
        "warn": False,
        "stdin": "",
        "stdin_add_newline": True,
        "strip_empty_ends": True,
    }

# Generated at 2022-06-13 04:58:19.997178
# Unit test for function main
def test_main():
    assert(os.path.exists('/usr/bin/jsx'))
    assert(os.path.exists('/usr/bin/cat'))
    assert(os.path.exists('/usr/bin/make'))


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:58:25.584244
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule({}, check_mode=True)
    # TODO : add tests for warning messages
    check_command(module, 'file test')
    check_command(module, 'curl test')
    check_command(module, 'service test')
    check_command(module, 'sudo service test')
    check_command(module, ['apt-get', 'test'])



# Generated at 2022-06-13 04:58:30.111991
# Unit test for function main
def test_main():
    test_input1 = {'_raw_params':"ls -l"}
    test_input2 = {'_raw_params':""}

# Generated at 2022-06-13 05:00:16.271012
# Unit test for function main
def test_main():
    with patch('ansible.modules.commands.command.subprocess.Popen', subprocess_popen_mock):
        p = subprocess_popen_mock.return_value
        p.returncode=0
        p.stdout.read.return_value="Test output"
        p.stderr.read.return_value="Test error"
        args = '/usr/bin/test args'
        module = MagicMock()
        module.params = {"argv": args}
        main()
        assert subprocess_popen_mock.call_count == 1
        assert subprocess_popen_mock.call_args == call(args, shell=False, cwd=None, executable=None, data=None, binary_data=True)
        assert p.communicate.call_count == 1
        assert p

# Generated at 2022-06-13 05:00:29.303411
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import is_iterable
    from ansible.module_utils.six import StringIO

    # Create a base AnsibleModule object
    module = basic._AnsibleModule('command', {
        '_raw_params': 'cat /etc/motd',
        '_uses_shell': False,
        'argv': None,
        'chdir': None,
        'executable': None,
        'creates': None,
        'removes': None,
        'warn': False,
        'stdin': None,
        'stdin_add_newline': True,
        'strip_empty_ends': True,
    }).load_params()


# Generated at 2022-06-13 05:00:30.123770
# Unit test for function check_command
def test_check_command():
    assert True



# Generated at 2022-06-13 05:00:44.234289
# Unit test for function main
def test_main():
    import ansible.module_utils.common.collections
    import ansible.module_utils._text
    import ansible.module_utils.basic

# Generated at 2022-06-13 05:00:49.210319
# Unit test for function main
def test_main():
    desc_dict = dict(
        _raw_params = dict(),
        _uses_shell = dict(type = 'bool', default = False),
        argv = dict(type = 'list', elements = 'str'),
        chdir = dict(type = 'path'),
        executable = dict(),
        creates = dict(type = 'path'),
        removes = dict(type = 'path'),
        warn = dict(type = 'bool', default = False, removed_in_version = '2.14', removed_from_collection = 'ansible.builtin'),
        stdin = dict(required = False),
        stdin_add_newline = dict(type = 'bool', default = True),
        strip_empty_ends = dict(type = 'bool', default = True),
    )


# Generated at 2022-06-13 05:00:50.278238
# Unit test for function main
def test_main():
    main()

# Generated at 2022-06-13 05:00:56.110045
# Unit test for function main
def test_main():
    test_args = [
        "192.168.1.1",
        "192.168.1.0",
        "192.168.1.2",
        "192.168.1.3"
    ]
    test_cmd = [
        "ls",
        "-l",
        "/tmp"
    ]
    # Test 1 check module.run_command with proper arguments
    local_run_command = module.run_command
    def fake_run_command(args, executable=None, use_unsafe_shell=False, data=None, binary_data=False, path_prefix=None, cwd=None,
                         raise_err=True, encoding=None):
        assert args == test_cmd
        assert use_unsafe_shell == False
        assert executable == None
        assert data == None
        assert binary_data

# Generated at 2022-06-13 05:00:59.300980
# Unit test for function main
def test_main():
    module = AnsibleModule({},{})
    main(module)


# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 05:01:10.818615
# Unit test for function main

# Generated at 2022-06-13 05:01:20.227697
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='/bin/ls',
        _uses_shell=False,
        executable='/bin/ls',
        creates='/test_command',
        removes='/test_command',
        warn=True,
        stdin='blah',
        stdin_add_newline=False,
        strip_empty_ends=False,
        check_mode=False
    )