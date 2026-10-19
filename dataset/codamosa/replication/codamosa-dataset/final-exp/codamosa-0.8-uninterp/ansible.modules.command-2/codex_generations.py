

# Generated at 2022-06-13 04:52:11.990500
# Unit test for function main
def test_main():
    import ansible.module_utils.common.removed
    with pytest.raises(ansible.module_utils.common.removed.RemovedInAnsible26Warning):
        assert main()


# Generated at 2022-06-13 04:52:24.110418
# Unit test for function check_command
def test_check_command():
    class args:
        def __init__(self):
            self.no_log = False
    class module:
        def __init__(self):
            self.no_log = False
            self.args = args()
            self.check_mode = False
            self.debug = False
    mod = module()
    check_command(mod, "/bin/touch")
    check_command(mod, ["/bin/echo", "hello"])
    check_command(mod, "pip install ansible")
    check_command(mod, "sudo apt-get install")
    check_command(mod, ["/bin/yum", "install", "ansible"])
    check_command(mod, ["/bin/dnf", "install", "ansible"])

# Generated at 2022-06-13 04:52:32.950264
# Unit test for function main
def test_main():
    # Mock the module class
    class AnsibleModule:
        def __init__(self):
            self.params = {}
            self.check_mode = True
        def fail_json(self, **kwargs):
            raise Exception('Ansible Module Failure')
        def warn(self, msg):
            raise Exception('Ansible Module Warn')
        def run_command(self, args, executable=None, use_unsafe_shell=None, encoding=None, data=None, binary_data=None):
            return 0, "stdout", "stderr"

    # Mock the datetime class
    class date:
        def now(self):
            return "now"

    # Mock the glob class
    class glob:
        def glob(self, path):
            if path == "exists":
                return True

# Generated at 2022-06-13 04:52:39.677274
# Unit test for function main
def test_main():
  test_module=AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(),
            _uses_shell=dict(type='bool', default=False)
        ),
        supports_check_mode=True,
  )
  test_module.params = {"_raw_params":"mkdir -p /home/quora/build/protobuf", "_uses_shell":False}
  test_run_command(test_module, ["mkdir", "-p", "/home/quora/build/protobuf"])
  return True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:52:51.975347
# Unit test for function check_command
def test_check_command():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import mock

    my_mock = mock.Mock()

    def mock_warn(msg):
        my_mock(msg)

    test_module = AnsibleModule(argument_spec={})
    test_module.check_mode = False
    test_module.warn = mock_warn

    check_command(test_module, 'yum -y install foo')
    assert my_mock.called is True

# Generated at 2022-06-13 04:53:04.838518
# Unit test for function main
def test_main():
    # Utility to allow us to capture stdout and stderr
    class Capture(object):
        def __init__(self, *a):
            self._a = a
        def __enter__(self):
            self._stdout = sys.stdout
            self._stderr = sys.stderr
            sys.stdout = self._stringio_stdout = six.StringIO()
            sys.stderr = self._stringio_stderr = six.StringIO()
            return self
        def __exit__(self, exc_type, exc_value, traceback):
            self.extend(self._stringio_stdout.getvalue(), self._stringio_stderr.getvalue())
            sys.stdout = self._stdout
            sys.stderr = self._stderr

# Generated at 2022-06-13 04:53:16.240914
# Unit test for function main
def test_main():
    def test_ansible_module(args):
        for key, value in args.items():
            setattr(module.params, key, value)


# Generated at 2022-06-13 04:53:21.709794
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.common.collections import is_iterable
    module = basic.AnsibleModule({}, {})
    #test when _raw_params is given as string
    result = main(module)
    assert result == None
    #test when _raw_params is given as list
    result = main(module)
    assert result == None
    #test when _raw_params is blank
    result = main(module)
    assert result == None
    #test when _raw_params and argv are given
    result = main(module)
    assert result == None

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:53:33.516724
# Unit test for function main
def test_main():
    data = {
            '_raw_params': 'echo hello world',
            '_uses_shell': True,
            'chdir': '/',
            'executable': None,
            'creates':None,
            'removes':None,
            'warn': True,
            'stdin':None,
            'stdin_add_newline': True,
            'strip_empty_ends': True
            }

# Generated at 2022-06-13 04:53:42.296951
# Unit test for function main
def test_main():
    r = {'changed': False, 'stdout': '', 'stderr': '', 'rc': None, 'cmd': None, 'start': None, 'end': None, 'delta': None, 'msg': ''}
    module = AnsibleModule(argument_spec={})
    module.run_command = lambda args, executable=None, use_unsafe_shell=False, encoding=None, data=None, binary_data=False: (0, "", "")
    try:
        main()
    except SystemExit as e:
        try:
            assert(e.code == 0)
        except:
            print("Expected exit code 0, got %d" % e.code)
            raise

# Generated at 2022-06-13 04:54:04.304641
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule, get_exception

    args = dict(
        chdir='/',
        executable='/bin/bash',
        args='ls',
        creates='/var/tmp/foo',
        removes='/var/tmp/foo',
        warn=True
    )


# Generated at 2022-06-13 04:54:17.308269
# Unit test for function main
def test_main():
    args = {
        '_raw_params': '/usr/bin/echo hello',
        'chdir': None,
        'creates': '',
        'removes': '',
        'warn': False,
        'stdin': '',
        'stdin_add_newline': True,
        'strip_empty_ends': True,
        '_uses_shell': False,
        'argv': '',
        'executable': ''
    }

# Generated at 2022-06-13 04:54:25.787255
# Unit test for function main
def test_main():
    args = dict(
        _raw_params="echo hello world",
        _uses_shell=True,
        chdir="~/Downloads",
        executable="/bin/sh",
        args=["echo","hello","world"],
        creates="/tmp/foo",
        removes="/tmp/bar",
        warn=True,
        stdin=None,
        stdin_add_newline=False,
        strip_empty_ends=False
    )

    module = AnsibleModule(argument_spec=args)

    r = {"changed": False,
         "stdout": '',
         "stderr": '',
         "rc": None,
         "cmd": None,
         "start": None,
         "end": None,
         "delta": None,
         "msg": ''}


    shell = True
    ch

# Generated at 2022-06-13 04:54:28.186127
# Unit test for function check_command
def test_check_command():
    m = AnsibleModule(argument_spec=dict())
    # catch exception thrown if command is not found
    check_command(m, 'not_a_real_command')
    check_command(m, 'ls')



# Generated at 2022-06-13 04:54:41.406591
# Unit test for function main
def test_main():
    p = {'_raw_params': 'ls -l', '_uses_shell': False, 'argv': [], 'chdir': '', 'executable': '', 'creates': None, 'removes': None, 'warn': False,
         'stdin': '', 'stdin_add_newline': True, 'strip_empty_ends': True}

# Generated at 2022-06-13 04:54:55.408472
# Unit test for function main

# Generated at 2022-06-13 04:55:01.907608
# Unit test for function main
def test_main():
    args = dict(
        chdir='/usr/share/',
        executable='/bin/bash',
        argv=['ls', '-l'],
        args='ls -l',
        warn=False
    )
    main(args)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:55:11.590903
# Unit test for function main
def test_main():
    # Check if program exits gracefully
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest_wrapped_e.type == SystemExit
#
    # Check if program exits with the desired exit code
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest_wrapped_e.type == SystemExit
#
    # Check if program correctly prints to stdout
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest_wrapped_e.type == SystemExit
#
    # Check if program correctly prints to stderr
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest

# Generated at 2022-06-13 04:55:16.284584
# Unit test for function check_command
def test_check_command():
    """ basic test to ensure it works """
    module = FakeModule()
    commandline = 'curl "http://www.ansible.com"'
    check_command(module, commandline)
    assert module.warnings == [
        "Consider using the get_url or uri module rather than running 'curl'.  If you need to use 'curl' because the get_url or uri module is insufficient you can add 'warn: false' to this command task or set 'command_warnings=False' in the defaults section of ansible.cfg to get rid of this message."
    ]
    assert not module.deprecations



# Generated at 2022-06-13 04:55:18.691717
# Unit test for function main
def test_main():
    #import ansible.modules.command
    #print("Hello")
    #print(ansible.modules.command.main())
    print("Test main function in command module")


# Generated at 2022-06-13 04:55:37.686434
# Unit test for function main
def test_main():
    assert True


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:55:40.907823
# Unit test for function check_command
def test_check_command():
    module = AnsibleModule(argument_spec={})
    module.warn = lambda *args: None
    commandline = "/path/to/some/command"
    check_command(module, commandline)



# Generated at 2022-06-13 04:55:42.332770
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:55:51.123084
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec=dict(
            _raw_params=dict(default=''),
            _uses_shell=dict(default=False),
            argv=dict(elements='str', type='list'),
            chdir=dict(default='/tmp'),
            executable=dict(),
            creates=dict(),
            removes=dict()
        )
    )
    def mock_run_command(args, **kwargs):
        return (0, 'OK', '')
    test_module.run_command = mock_run_command
    result = main()
    assert isinstance(result, dict)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:56:03.120289
# Unit test for function main
def test_main():
    cmd = ["echo"]

# Generated at 2022-06-13 04:56:16.007432
# Unit test for function main

# Generated at 2022-06-13 04:56:27.072371
# Unit test for function main
def test_main():
    FieldStorage = mock.Mock()
    setattr(FieldStorage, 'filename', None)
    setattr(FieldStorage, 'file', None)


    fields = {
        '_salt_system_modes': ['full'],
        'fun': 'cmd.run',
        '_salt_return_pub_port': '10900',
        '__pub_user': 'michael',
        '__pub_arg': ['ls -al /'],
        '__pub_jid': '20161006115446779636',
        '__pub_fun': 'cmd.run',
        '__pub_pid': '47163',
        '__pub_tgt': 'salt-master'
    }

    module = AnsibleModule(argument_spec={})
    sys.modules['cmd'] = types.ModuleType

# Generated at 2022-06-13 04:56:36.603029
# Unit test for function check_command
def test_check_command():
    from collections import namedtuple
    import ansible.module_utils.basic
    MockModule = namedtuple('MockModule', ['warn'])
    check_command(MockModule(warn=lambda x: x), 'sudo')
    check_command(MockModule(warn=lambda x: x), 'su')
    check_command(MockModule(warn=lambda x: x), 'pbrun')
    check_command(MockModule(warn=lambda x: x), 'pfexec')
    check_command(MockModule(warn=lambda x: x), 'runas')
    check_command(MockModule(warn=lambda x: x), 'pmrun')
    check_command(MockModule(warn=lambda x: x), 'machinectl')

# Generated at 2022-06-13 04:56:46.012138
# Unit test for function main

# Generated at 2022-06-13 04:56:57.017014
# Unit test for function check_command
def test_check_command():
    class FakeModule(object):
        def __init__(self):
            self.warnings = []
        def warn(self, msg):
            self.warnings.append(msg)

    cmd = 'curl http://192.168.0.1/index.html'
    cmd_list = ['/usr/bin/curl', 'http://192.168.0.1/index.html']
    module = FakeModule()
    check_command(module, cmd)
    assert('Consider using the get_url or uri module rather than running' == module.warnings[0][:56])
    module.warnings = []
    check_command(module, cmd_list)
    assert('Consider using the get_url or uri module rather than running' == module.warnings[0][:56])



# Generated at 2022-06-13 04:58:38.075115
# Unit test for function main
def test_main():
    args = dict(
        _raw_params = "echo hello",
        executable = "",
        chdir = "",
        creates = "",
        removes = "",
        warn = False,
    )
    module = AnsibleModule(argument_spec=args.copy())
    assert module.params["_raw_params"] == "echo hello"

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:58:41.706127
# Unit test for function main
def test_main():
    args = dict (
        argv=['/usr/bin/make_database.sh'],
    )

    r = main(args)
    assert r['changed'] == True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:58:51.127186
# Unit test for function main
def test_main():
    mocked_module = mocker.MagicMock()
    mocked_module.params = {
        '_raw_params': ['echo', 'hello', 'world'],
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
    }

    # check_mode partial support, since it only really works in checking creates/removes
    mocked_module.check_mode = False

    mocked_shell = mocker.MagicMock()
    mocked_shell = False

    mocked_chdir = mocker.MagicMock()
    mocked

# Generated at 2022-06-13 04:58:57.667851
# Unit test for function main
def test_main():
    my_command = ["python3", "/home/travis/build/cu-unix-admins/ansible-modules-extras/lib/ansible/modules/system/command.py"]

# Generated at 2022-06-13 04:59:08.958636
# Unit test for function main

# Generated at 2022-06-13 04:59:11.829905
# Unit test for function main
def test_main():
    if not main() == None:
        raise Exception("Function main failed")
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 04:59:13.463786
# Unit test for function main
def test_main():
    print("Test function main")
    print(main())



# Generated at 2022-06-13 04:59:14.231237
# Unit test for function main
def test_main():
    assert 1 == 2

# Generated at 2022-06-13 04:59:24.393644
# Unit test for function main

# Generated at 2022-06-13 04:59:36.682619
# Unit test for function main
def test_main():
    import ansible.module_utils.basic as basic
    import ansible.module_utils.ansible_release as ansible_release
    
    module_name = "ansible.builtin.command"

# Generated at 2022-06-13 05:02:00.723011
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    test_data = {}
    test_data['argv'] = [b"echo", b"hello"]
    test_data['_raw_params'] = b"echo hello"
    test_data['chdir'] = None
    test_data['_uses_shell'] = False
    test_data['creates'] = None
    test_data['removes'] = None
    test_data['executable'] = None
    test_data['warn'] = False
    test_data['stdin'] = None
    test_data['stdin_add_newline'] = True
    test_data['strip_empty_ends'] = True
    test_data['_ansible_check_mode'] = True