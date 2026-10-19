

# Generated at 2022-06-13 04:52:10.412705
# Unit test for function main
def test_main():
    assert callable(main)


# Generated at 2022-06-13 04:52:22.056535
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec=dict())
    check_command(module, '/usr/bin/chown')
    check_command(module, ['/usr/bin/chown'])
    check_command(module, '/usr/bin/rmdir')
    check_command(module, ['/usr/bin/rmdir'])
    check_command(module, '/usr/bin/tar')
    check_command(module, ['/usr/bin/tar'])
    check_command(module, '/usr/bin/curl')
    check_command(module, ['/usr/bin/curl'])
    check_command(module, '/usr/bin/pbrun')
    check_command(module, ['/usr/bin/pbrun'])



# Generated at 2022-06-13 04:52:31.102660
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='ls -l /tmp/test_command',
        _uses_shell=False,
        command='ls',
        executable='/bin/sh',
        creates=None,
    )
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
            _uses_shell=dict(type='bool', default=False),
            executable=dict(),
            creates=dict(type='path'),
        ),
        supports_check_mode=True,
    )
    mainresult = main(module, args)
    #print mainresult

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:52:40.665635
# Unit test for function check_command
def test_check_command():
    m = AnsibleModule(
            argument_spec=dict(
                command=dict(required=True),
                warn=dict(required=False, default=True, type='bool'),
            ),
        )
    check_command(m, "echo")
    assert m.warnings == ["Consider using the echo module rather than running 'echo'.  If you need to use 'echo' because the echo module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."]

# ===========================================
# Main control flow



# Generated at 2022-06-13 04:52:53.596035
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.common.collections import Mapping
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 04:53:01.634615
# Unit test for function main
def test_main():
    a = AnsibleModule(argument_spec={}, supports_check_mode=False)
    res_args = dict(
        changed=True,
        rc=0,
        start='',
        end='',
        delta='',
        msg='',
    )
    a.run_command = MagicMock(return_value=(res_args['rc'], res_args['stdout'], res_args['stderr']))
    main()


# Generated at 2022-06-13 04:53:12.770718
# Unit test for function main
def test_main():
    args = dict(
    _raw_params="find /tmp/ -type f -name '*.mp3'",
    _uses_shell=True,
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
    main(args)
test_main()

# Generated at 2022-06-13 04:53:24.844537
# Unit test for function check_command
def test_check_command():
    """Test function for `check_command` function"""
    import tempfile
    test_file = tempfile.NamedTemporaryFile()
    module = AnsibleModule(argument_spec={})
    module.params = {'warn': True}
    commandline = ['chmod', '-R', '777', test_file.name]
    check_command(module, commandline)
    assert module.warnings == ['Consider using the file module with mode rather than running \'chmod\'.  '
                               'If you need to use \'chmod\' because the file module is insufficient you can add '
                               "'warn: false' to this command task or set 'command_warnings=False' in "
                               'the defaults section of ansible.cfg to get rid of this message.']
    # Reset the warnings list
    del module.warnings[:]

# Generated at 2022-06-13 04:53:37.625491
# Unit test for function main
def test_main():
    params = {
        "chdir": "/root/test_dir",
        "args": "/usr/bin/cat /tmp/test.txt",
        "executable": "/usr/bin/bash",
        "removes": "/tmp/test.txt",
        "creates": "/tmp/foo.txt",
        "warn": True
    }

    result = {"start": "2017-11-17 19:27:34.267370", "rc": 0,
         "stdout": "hello\n", "end": "2017-11-17 19:27:34.272800",
         "changed": True, "stderr": "", "delta": "0:00:00.00543",
         "cmd": ["/usr/bin/cat", "/tmp/test.txt"]}

# Generated at 2022-06-13 04:53:48.206799
# Unit test for function main
def test_main():
    from ansible.modules.system import command
    from ansible.module_utils.system import command as module_command
    import tempfile
    import os
    import shutil
    from ansible.module_utils._text import to_bytes, to_text

    tmpdir = tempfile.mkdtemp()
    shutil.copy('test/ansible_command.ps1', tmpdir)
    shutil.copy('test/ansible_command.py', tmpdir)

    os.chdir(tmpdir)
    fd, tmpfile = tempfile.mkstemp()
    with os.fdopen(fd, 'wb') as f:
        f.write(to_bytes('hello'))

    # Without _raw_params.

# Generated at 2022-06-13 04:54:04.877661
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils import common
    from ansible.module_utils import connection
    from ansible.module_utils import dirlist
    from ansible.module_utils import facts
    from ansible.module_utils import text
    from ansible.module_utils import url
    from ansible.module_utils import vars
    from ansible.module_utils.connection import Connection
    from ansible.module_utils.facts import Facts
    from ansible.module_utils.facts import timeout
    from ansible.module_utils.facts.system.bsd import BSD
    from ansible.module_utils.facts.system.distribution import Distribution
    from ansible.module_utils.facts.system.generic import Generic

# Generated at 2022-06-13 04:54:17.854678
# Unit test for function main
def test_main():
    args = dict(
        _raw_params="cat /etc/motd",
        _uses_shell=False,
        argv=None,
        chdir=None,
        executable=None,
        creates=None,
        removes=None,
        warn=False,
        stdin=None,
        stdin_add_newline=True,
        strip_empty_ends=True,
    )
    result = main(None, "command", args)
    #print(result['stdout'])

# Generated at 2022-06-13 04:54:28.426152
# Unit test for function main
def test_main():
    global module
    global shell
    global chdir
    global executable
    global args
    global argv
    global creates
    global removes
    global warn
    global stdin
    global stdin_add_newline
    global strip
    global r
    global shoulda

# Generated at 2022-06-13 04:54:41.601756
# Unit test for function main
def test_main():
    # Need to stub out stdin for this
    import cStringIO
    import sys
    sys.stdin = cStringIO.StringIO('hello')
    # Need to stub out the module class to get both the internal code path and
    # the code path from the action plugin.
    from ansible.module_utils.basic import AnsibleModule
    from ansible.playbook.play_context import PlayContext
    from ansible.executor.task_queue_manager import TaskQueueManager
    from ansible.utils.display import Display
    display = Display()
    play_context = PlayContext()
    module_args = dict(
        _raw_params='echo hello',
        _uses_shell=False,
        chdir='',
        executable='',
        creates='',
        removes='',
        warn=True,
    )
    #

# Generated at 2022-06-13 04:54:55.461973
# Unit test for function main

# Generated at 2022-06-13 04:54:56.302721
# Unit test for function check_command
def test_check_command():
    assert True



# Generated at 2022-06-13 04:55:06.786245
# Unit test for function main
def test_main():
    stdin = 'stdin'
    stdin_add_newline = True
    strip_empty_ends = True
    chdir = 'test chdir'
    executable = 'test executable'
    creates = 'test creates'
    removes = 'test removes'
    args = 'test args'
    argv = ['test', 'argv']
    shell = True
    rc = 0
    stdout = 'test out put'
    stderr = 'test error output'
    r = {'changed': False, 'stdout': '', 'stderr': '', 'rc': None, 'cmd': None, 'start': None, 'end': None, 'delta': None, 'msg': ''}
    module = MagicMock(name='module')
    module.check_mode = False
    module.run_command.return_value

# Generated at 2022-06-13 04:55:14.315423
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    check_command(module, "ansible.builtin.file")
    check_command(module, "echo hello")
    check_command(module, '/bin/chgrp')
    check_command(module, 'curl http://www.ansible.com')
    check_command(module, 'wget http://www.ansible.com')
    check_command(module, 'svn co')
    check_command(module, 'dnf install')
    check_command(module, 'zypper install')
    check_command(module, 'yum install')
    check_command(module, 'tar xf')
    check_command(module, 'unzip')
    check_command(module, 'sed')
    check_command(module, 'rpm -q something')


# Generated at 2022-06-13 04:55:18.569755
# Unit test for function check_command
def test_check_command():
    failed = 0
    module = AnsibleModule(argument_spec=dict())
    expected_warnings = ["Consider using the service module rather than running 'service'.",
                         "Consider using the yum module rather than running 'yum'.",
                         "Consider using the uri module rather than running 'curl'."]
    for command in ['service nginx start', 'yum -y install nginx', 'curl http://example.com']:
        check_command(module, command)
        for warning in expected_warnings:
            if warning not in module.warnings:
                failed = 1
    assert failed == 0



# Generated at 2022-06-13 04:55:28.787543
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils.basic import AnsibleModule
    mod = AnsibleModule(argument_spec={'command': dict(type='path'),  'executable': dict(type='path')})
    check_command(mod, 'ln -s')
    check_command(mod, 'rpm -q')
    check_command(mod, ['wget', 'http://www.example.org/'])
    check_command(mod, 'touch')
    check_command(mod, 'yum install')
    check_command(mod, 'apt-get install')
    check_command(mod, 'dnf install')
    check_command(mod, 'zypper install')
    check_command(mod, 'sudo apt-get install')
    check_command(mod, 'su - root -c "dnf install"')
    check_

# Generated at 2022-06-13 04:56:00.086056
# Unit test for function main
def test_main():
    test = dict(
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

# Generated at 2022-06-13 04:56:13.751077
# Unit test for function main
def test_main():
    from ansible.modules.command.command import main
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 04:56:26.035024
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    assert check_command(module, ['chown'])
    assert check_command(module, ['chmod'])
    assert check_command(module, ['chgrp'])
    assert check_command(module, ['ln'])
    assert check_command(module, ['mkdir'])
    assert check_command(module, ['rmdir'])
    assert check_command(module, ['rm'])
    assert check_command(module, ['touch'])
    assert check_command(module, ['curl'])
    assert check_command(module, ['wget'])
    assert check_command(module, ['svn'])
    assert check_command(module, ['service'])
    assert check_command(module, ['mount'])

# Generated at 2022-06-13 04:56:36.485492
# Unit test for function check_command
def test_check_command():
    class FakeModule:
        def warn(self, msg):
            print(msg)

    command = ['yum', 'install', '-y', 'httpd']
    check_command(FakeModule(), command)
    command = ['mount', '-t', 'ext4', '/dev/mapper/centos-root', '/mnt/']
    check_command(FakeModule(), command)
    command = ['rpm', '-q', 'package-19.2.3']
    check_command(FakeModule(), command)
    command = ['touch', '-almo', '-t', '190012312359', '/etc/test']
    check_command(FakeModule(), command)
    command = ['curl', '10.10.10.10']
    check_command(FakeModule(), command)

# Generated at 2022-06-13 04:56:45.028825
# Unit test for function check_command
def test_check_command():

    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    for cmd in ['chown', 'chmod', 'chgrp', 'ln', 'mkdir', 'rmdir', 'rm', 'touch', 'curl', 'wget',
                'svn', 'service', 'mount', 'rpm', 'yum', 'apt-get', 'tar', 'unzip', 'sed', 'dnf', 'zypper']:
        m = basic.AnsibleModule(
            argument_spec = dict(),
        )
        m._ansible_warnings = []
        check_command(m, [cmd])
        assert len(m._ansible_warnings) == 1


# Generated at 2022-06-13 04:56:56.335691
# Unit test for function main

# Generated at 2022-06-13 04:57:03.865761
# Unit test for function main
def test_main():
    command_args = ['/usr/bin/echo', 'hello']
    params = dict(
        _raw_params='echo hello',
        _uses_shell=False,
        argv='[echo, hello]',
        executable=None,
        chdir=None,
        creates='',
        removes='',
        warn=False,
        stdin='',
        stdin_add_newline=True,
        strip_empty_ends=True,
    )
    res = dict(
        changed=True,
        cmd=command_args,
        delta=None,
        end=None,
        failed=False,
        start=None,
        stderr='',
        stdout='hello',
        warn=False,
        rc=0,
        msg='',
    )

# Generated at 2022-06-13 04:57:13.273079
# Unit test for function check_command
def test_check_command():
    import ansible.modules.commands.command
    module = type('Module', (object,), {})

# Generated at 2022-06-13 04:57:18.463176
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(
        argument_spec=dict(),
    )
    command = "cat"
    check_command(module, command)
    assert not module.warnings

    command = ["foo"]
    check_command(module, command)
    assert not module.warnings


# ===========================================
# Main control flow


# Generated at 2022-06-13 04:57:32.129568
# Unit test for function main
def test_main():
    r = dict(changed=False, cmd=None, rc=None, stdout='', start='', end='', delta='', stderr='', msg='')
    test_command_default = ['echo', 'hello']

    with patch.object(AnsibleModule, 'run_command') as mock_run_command:
        mock_run_command.return_value = 0, 'hello', ''
        main()
        assert r['rc'] == 0
        assert r['cmd'] == test_command_default

    with patch.object(AnsibleModule, 'run_command') as mock_run_command:
        mock_run_command.return_value = 1, '', 'error'
        main()
        assert r['rc'] == 1
        assert r['cmd'] == test_command_default
        assert r['stderr']

# Generated at 2022-06-13 04:58:17.517589
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec = dict())
    check_command(module, "sudo ls -ltr")
    check_command(module, ["sudo", "ls", "-ltr"])
    check_command(module, "curl http://www.ansible.com")
    check_command(module, "svn --version")
    check_command(module, "service --status-all")


# Generated at 2022-06-13 04:58:19.394975
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:58:28.299372
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils import basic
    from ansible.modules.extras.cloud.cloudforms.cfme.command import check_command
    mod = basic.AnsibleModule(argument_spec={})
    mod.warn = lambda *args, **kwargs: None
    # Ensure command warning is generated
    check_command(mod, 'curl')
    assert not hasattr(mod, 'warn')
    # Ensure warning is not generated for remote module
    check_command(mod, 'ansible.builtin.get_url')
    assert not hasattr(mod, 'warn')
    # Ensure warning is not generated for local module
    check_command(mod, 'ansible-doc')
    assert not hasattr(mod, 'warn')
    # Ensure command warning is generated for broken path

# Generated at 2022-06-13 04:58:38.881010
# Unit test for function main
def test_main():
    args = dict(
        _raw_params='echo "hello"',
        _uses_shell=True,
        chdir='',
        executable='',
        creates='',
        removes='',
        warn=False,
        stdin='',
        stdin_add_newline=True,
        strip_empty_ends=True,
    )
    r = dict(
        changed=False,
        stdout="",
        stderr="",
        rc=None,
        cmd=None,
        start=None,
        end=None,
        delta=None,
        msg='',
    )

    with pytest.raises(SystemExit):
        main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:58:42.436243
# Unit test for function main
def test_main():

    assert True


# ansible-playbook --diff --verbose --syntax-check -i ../hosts ./test.yaml --extra-vars='@vault-password.yaml'
if __name__ == "__main__":
    main()

# Generated at 2022-06-13 04:58:46.316755
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# import module snippets
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.basic import get_exception

if __name__ == "__main__":
    main()

# Generated at 2022-06-13 04:58:54.487034
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(type='str', default='ls -la'),
            _uses_shell=dict(type='bool', default=False),
            # The default for this really comes from the action plugin
            warn=dict(type='bool', default=False, removed_in_version='2.14', removed_from_collection='ansible.builtin'),
        ),
        supports_check_mode=True,
    )

    r = {'changed': False, 'stdout': '', 'stderr': '', 'rc': None, 'msg': ''}

    main()
    r = {'changed': True, 'stdout': '', 'stderr': '', 'rc': None, 'msg': ''}

    module.exit_json(**r)




# Generated at 2022-06-13 04:59:07.094644
# Unit test for function main
def test_main():
    argv = [
        '/usr/bin/ansible-test',
        'command',
        'echo hello',
    ]
    import site
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import builtins
    builtins.__dict__['_'] = lambda x: x
    os = MockOS()
    os.getpid = Mock(return_value=1000)
    os.environ = dict(LANG='en_US.UTF-8')
    site.PREFIXES = ['/usr']
    site.USER_BASE = '/usr/local'
    site.USER_SITE = '/usr/local/lib/python3.6/site-packages'
    main(dict(args=argv[2]))

# import module snippets

# Generated at 2022-06-13 04:59:14.633804
# Unit test for function check_command
def test_check_command():
    path = '/bin'
    test_command = os.path.join(path, 'curl')
    module = AnsibleModule(
        argument_spec=dict(modified_date=dict(type='str')),
        supports_check_mode=True
    )
    commandline = [test_command, 'http://google.com']
    check_command(module, commandline)
    assert module.warnings



# Generated at 2022-06-13 04:59:25.301195
# Unit test for function check_command
def test_check_command():
    # Test if a list is correctly converted to a string for check_command
    class TestModule():
        def warn(self, msg):
            assert msg == "Consider using 'become', 'become_method', and 'become_user' rather than running list_test"
    TestModule.warn = warn
    commandline = ['list_test']
    module = TestModule()
    check_command(module, commandline)

    # Test if a string is correctly converted to a list for check_command
    class TestModule():
        def warn(self, msg):
            assert msg == "Consider using 'become', 'become_method', and 'become_user' rather than running string_test"
    TestModule.warn = warn
    commandline = "string_test"
    module = TestModule()
    check_command(module, commandline)

# Generated at 2022-06-13 05:01:07.060080
# Unit test for function main
def test_main():

    def run_module():
        # Each test takes a dict arg that sets up the module state just prior to execution
        # Each test returns a dict of the module.exit_json return values, to validate expected results
        argv_command = dict(
            _raw_params='/bin/true',
            _uses_shell=False,
            argv=[],
            chdir=None,
            executable=None,
            creates=None,
            removes=None,
            warn=True,
            stdin=None,
            stdin_add_newline=True,
            strip_empty_ends=True,
        )
        module = AnsibleModule(**argv_command)

# Generated at 2022-06-13 05:01:14.319203
# Unit test for function main
def test_main():

     # test function main
     # load arguments into ansible params
     arg_spec = dict(
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
     )

# Generated at 2022-06-13 05:01:22.109799
# Unit test for function main
def test_main():
    import sys
    import os
    import glob
    import shutil
    import tempfile
    import copy

    test_dir = tempfile.mkdtemp()
    test_file = tempfile.mkstemp(dir=test_dir)
    test_file_name = os.path.basename(test_file[1])
    test_file_dir = os.path.dirname(test_file[1])
    test_file_content = 'hello world'
    test_file_copy = os.path.join(test_dir, 'copied')
    test_file2_name = 'hello.world'
    test_file2 = os.path.join(test_dir, test_file2_name)
    test_file3 = os.path.join(test_dir, 'world.hello')
    test_dir2

# Generated at 2022-06-13 05:01:26.942813
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
            warn=dict(type='bool', default=False),
            stdin=dict(required=False),
            stdin_add_newline=dict(type='bool', default=True),
            strip_empty_ends=dict(type='bool', default=True),
        ),
        supports_check_mode=True,
    )
    shell = module.params['_uses_shell']


# Generated at 2022-06-13 05:01:31.180277
# Unit test for function main
def test_main():
    args = {}
    args['_raw_params'] = 'ls -lrt'
    args['_uses_shell'] = True
    args[''] = True
    args[''] = True
    args[''] = True
    args[''] = True
    args[''] = True
    args[''] = True

test_main()

# Generated at 2022-06-13 05:01:42.992320
# Unit test for function main
def test_main():
    # File does not exist
    exists = False
    shoulda = "Did"
    commandline = "grep -i hostname inventory"
    args = commandline.split()

# Generated at 2022-06-13 05:01:51.572877
# Unit test for function main
def test_main():
    from ansible.module_utils.common.collections import Mapping
    from ansible.module_utils.common.text.converters import to_bytes, to_text

    class AnsibleModule(object):

        def __init__(self, argument_spec, supports_check_mode=False, bypass_checks=False):
            self.argument_spec = argument_spec
            self.supports_check_mode = supports_check_mode
            self.check_mode = True
            self.fail_json = lambda r: None
            self.exit_json = lambda r: None

        def run_command(self, cmd, executable=None, use_unsafe_shell=True, encoding=None, data=None, binary_data=False):
            return 0, '', 'stdout', ''


# Generated at 2022-06-13 05:02:03.642565
# Unit test for function main
def test_main():
  """
  Test ansible.module_utils.command.py main() with different input arguments
  """