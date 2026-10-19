

# Generated at 2022-06-13 06:21:09.594704
# Unit test for function main
def test_main():
    '''
    unit test for ansible-systemd/systemd.py function main
    '''

    import pytest

# Generated at 2022-06-13 06:21:12.762973
# Unit test for function main
def test_main():
    main()

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.urls import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:18.925369
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored("ignoring request to reload foo.service")
    assert not request_was_ignored("= foo.service loaded active running Foo Module")
    assert request_was_ignored("foo.service: Job type reload is not applicable for unit foo.service.")
    assert not request_was_ignored("foo.service: Reload failed: Invalid argument")
    assert request_was_ignored("foo.service: ignoring command.\n")
    assert not request_was_ignored("foo.service: bar")



# Generated at 2022-06-13 06:21:27.736947
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # This is a real value obtained from 'systemctl show crond.service'
    input = '''
ActiveEnterTimestamp=Sun 2016-05-15 18:28:49 EDT
ActiveEnterTimestampMonotonic=8135942
UnitFileState=enabled
'''.split('\n')
    assert parse_systemctl_show(input) == {
        'ActiveEnterTimestamp': 'Sun 2016-05-15 18:28:49 EDT',
        'ActiveEnterTimestampMonotonic': '8135942',
        'UnitFileState': 'enabled'
    }

    # This is a test to verify that values can span multiple lines

# Generated at 2022-06-13 06:21:33.837585
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:38.554444
# Unit test for function request_was_ignored
def test_request_was_ignored():
    failures = []
    if request_was_ignored('foo=bar'):
        failures.append('request_was_ignored failed to return False')
    if request_was_ignored(''):
        failures.append('request_was_ignored failed to return False')
    if not request_was_ignored('ignoring request'):
        failures.append('request_was_ignored failed to return True')
    if not request_was_ignored('foo ignoring command bar'):
        failures.append('request_was_ignored failed to return True')
    if len(failures):
        raise Exception('Unit tests failed:\n%s' % '\n'.join(failures))



# Generated at 2022-06-13 06:21:47.671521
# Unit test for function main

# Generated at 2022-06-13 06:21:59.425648
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=False)
    unit = '/test/test@test'
    systemctl = module.get_bin_path('systemctl', True)
    result = dict(
        name=unit,
        changed=False,
        status=dict(),
    )
    action = 'enable'
    rc = 1
    with mock.patch.dict(os.environ, {'XDG_RUNTIME_DIR': '/run/user/%s' % os.geteuid()}):
        with mock.patch.object(AnsibleModule, 'run_command') as run_command:
            run_command.return_value = rc, '', ''
            with pytest.raises(SystemExit) as excinfo:
                main()
            assert excinfo.value.args

# Generated at 2022-06-13 06:22:10.071330
# Unit test for function main

# Generated at 2022-06-13 06:22:21.524424
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('● x.service - user-defined service\n   Loaded: loaded (/user/lib/systemd/user/x.service; enabled)\n   Active: active (running) since Sat 2019-02-02 01:03:03 EST; 15min ago\n Main PID: 19682 (x.sh)') is False
    assert request_was_ignored('● x.service - user-defined service\n   Loaded: loaded (/user/lib/systemd/user/x.service; enabled)\n   Active: active (running) since Sat 2019-02-02 01:03:03 EST; 15min ago\n Main PID: 19682 (x.sh)\n\x1b[1A\x1b[1A\x1b[1A\x1b[K\n') is True
    assert request_was_ign

# Generated at 2022-06-13 06:22:57.855812
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Test for issue found in https://github.com/ansible/ansible/issues/30720
    # where non-multiline values can be parsed as multiline values.
    input = ["Description={  A very long description", "This description spans multiple lines  }"]
    output = parse_systemctl_show(input)
    assert output == {'Description': '{  A very long description\nThis description spans multiple lines  }'}



# Generated at 2022-06-13 06:23:08.483574
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    lines = ['Id=httpd.service', 'Description=The Apache HTTP Server', 'LoadState=loaded', 'ActiveState=active', 'SubState=running', 'UnitFileState=enabled', 'ExecMainPID=546', 'ExecMainStartTimestampMonotonic=0', 'ExecMainExitTimestampMonotonic=0', 'ExecMainCode=0', 'ExecMainStatus=0', 'Result=success', 'StatusErrno=0', 'Status=\\\\n\\\\t   Loaded: loaded (\\\\x20->/usr/sbin/httpd ; enabled; vendor preset: disabled)\\\\n\\\\t   Active: active (running) since Sun 2017-04-02 01:17:10 UTC; 6min ago', 'Triggers=\\\\nTransient=no']

# Generated at 2022-06-13 06:23:16.102130
# Unit test for function main
def test_main():
    import json
    # Unit test was written with the assumption that the module is run with --execute,
    # which sets the MODULE_COMPLEX_ARGS environment variable.
    args = json.loads(os.environ['MODULE_COMPLEX_ARGS'])

    unit = args['name']
    systemctl = args.get('bin')

    # Run daemon-reload first, if requested
    if args['daemon_reload'] and not args['CHECKMODE']:
        (rc, out, err) = module.run_command("%s daemon-reload" % (systemctl))
        if rc != 0:
            module.fail_json(msg='failure %d during daemon-reload: %s' % (rc, err))

    # Run daemon-reexec

# Generated at 2022-06-13 06:23:18.114781
# Unit test for function main
def test_main():

    # Unit test for function main
    # Execute function main with different parameters
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:28.819059
# Unit test for function main
def test_main():
    unit = 'sshd'
    systemctl = 'systemctl'
    rc = 0

# Generated at 2022-06-13 06:23:31.850372
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:41.012878
# Unit test for function main
def test_main():
    if os.getenv('SYSTEMD_OFFLINE') == '1' or os.path.exists('/etc/systemd/system/offline.target'):
        print("Systemd is offline, skipping tests")
        sys.exit(0)

    import shutil
    import sys
    import tempfile
    import traceback
    import yaml

    tempdir = tempfile.mkdtemp()
    tmp_file = tempfile.NamedTemporaryFile(mode='w+t', dir=tempdir)
    tmp_file.write('#!/bin/bash\necho "test"')
    tmp_file.flush()
    b_tmp_file = tempfile.NamedTemporaryFile(mode='w+t', dir=tempdir)

# Generated at 2022-06-13 06:23:52.218693
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes

    out='{"name":"mac\n","changed":false,"status":{"Id":"mac.service","Names":"mac.service","LoadState":"loaded","ActiveState":"active","SubState":"running","FragmentPath":"/usr/lib/systemd/system/mac.service"}}'

# Generated at 2022-06-13 06:23:59.264367
# Unit test for function main
def test_main():

    test_called = [False]

    # Test the requested state is the same as the states service is
    # Test the requested enabled state is the same as the services enabled state
    def run_command(self, args, check_rc=False):
        self.assertEqual(cmd, args)

        test_called[0] = True

        (rc, out, err) = (0, '', '')
        if args.strip() == "systemctl status test.service":
            rc = 0

# Generated at 2022-06-13 06:24:11.328979
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    assert parse_systemctl_show(['Description=Multi-User System', 'After=basic.target']) == {'Description': 'Multi-User System', 'After': 'basic.target'}
    assert parse_systemctl_show(['Description=Hello', 'Description=world', 'After=basic.target']) == {'Description': 'Hello\nworld', 'After': 'basic.target'}
    assert parse_systemctl_show(['ExecStart=hello', 'ExecStart=world', 'After=basic.target']) == {'ExecStart': 'hello\nworld', 'After': 'basic.target'}

# Generated at 2022-06-13 06:24:36.559685
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:24:47.838900
# Unit test for function main

# Generated at 2022-06-13 06:24:49.341182
# Unit test for function main
def test_main():
    """Test main functionality of module"""

    assert True


# Generated at 2022-06-13 06:24:59.949322
# Unit test for function main

# Generated at 2022-06-13 06:25:10.239411
# Unit test for function main

# Generated at 2022-06-13 06:25:21.548945
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:25:26.335762
# Unit test for function main
def test_main():

    module = AnsibleModule({
        'name': 'dummy_service',
        'enabled': True,
        'force': False,
        'masked': False,
    })

    import sys

    if sys.version_info.major == 2:
        exec('def to_native(x): return x')

    def run_command(module, cmd):
        return (0, "yes", "")

    setattr(module, 'run_command', run_command)

    # There is no support for testing main() in unit tests
    # main()

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:31.838435
# Unit test for function main
def test_main():
    with open('tests/unit/systemd/test_systemd.py') as f:
        module_args = dict()
        set_module_args(module_args)

        print(module_args)
        with pytest.raises(AnsibleExitJson) as exec_info:
            main()
        
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:40.354662
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:25:46.995670
# Unit test for function main
def test_main():
    module = None
    result = {"name": "wordpress"}


# Generated at 2022-06-13 06:26:16.981641
# Unit test for function main
def test_main():
    test_unit = [{
        "unit": {
            "key1": "value1",
            "key2": "value2"
        }
    }]
    test_unit.insert(0, dict(changed=False, name="foo", ansible_facts={'i_am_a_key': 'and_i_am_a_value'}))
    test_unit.insert(0, dict(ANSIBLE_MODULE_ARGS={'name': 'foo', 'state':'started'}))

# Generated at 2022-06-13 06:26:26.772851
# Unit test for function main
def test_main():
    test_opts = {
        'name': 'crond.service'
    }

    test_mod = MagicMock()
    test_mod.params = test_opts
    test_mod.run_command = MagicMock(return_value=(0, 'Active: active (running)', ''))
    test_mod.is_failed = MagicMock(return_value=False)
    test_mod.fail_json = MagicMock()
    test_mod.exit_json = MagicMock()

    # Test with a valid command
    main()
    assert test_mod.exit_json.called

    # Test with an invalid command
    test_mod.run_command = MagicMock(return_value=(1, '', 'Could not find service crond.service'))
    main()
    assert test_mod.fail_

# Generated at 2022-06-13 06:26:33.552223
# Unit test for function main
def test_main():
    with patch.object(AnsibleModule, "run_command") as run_command:
        with patch.object(AnsibleModule, "get_bin_path") as get_bin_path:
            with patch.object(os, "geteuid") as geteuid:
                geteuid.return_value = 0
                get_bin_path.return_value = '/bin/systemctl'


# Generated at 2022-06-13 06:26:46.234881
# Unit test for function main
def test_main():
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'library'))
    from ansible.module_utils import systemd
    from ansible.module_utils.systemd import systemd_unit_get, systemd_unit_exists
    from ansible.module_utils.six import PY3
    from ansible.module_utils import basic
    import json


# Generated at 2022-06-13 06:26:56.352426
# Unit test for function main

# Generated at 2022-06-13 06:27:03.666791
# Unit test for function main
def test_main():
    unit = 'sshd'
    params = dict(
       name=unit,
       daemon_reload=True
    )
    args = json.dumps(params)
    rc, out, err = module_run_command(systemctl, rc, stdout, stderr)
    for line in err.splitlines():
        if 'error' in line:
            raise KeyError
    return out

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:09.896228
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    test_data = '''
    foo=bar
    baz=boo
    ExecStart={/one/two;\
-three/four}
    ExecStart={/one/two;\
-three/four}
    '''
    assert parse_systemctl_show(test_data.split('\n')) == {'foo': 'bar', 'baz': 'boo', 'ExecStart': '/one/two;-three/four'}



# Generated at 2022-06-13 06:27:19.158577
# Unit test for function main
def test_main():
    import os
    import sys
    import shutil
    import json
    import tempfile
    import copy

    try:
        from ansible.module_utils import basic
    except ImportError:
        print('failed=True msg="ansible.module_utils.basic could not be imported"')
        sys.exit(1)

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six import PY3

    # Make a temporary directory to act as a chroot
    chroot_tempdir = tempfile.mkdtemp()
    os.chmod(chroot_tempdir, 0o755)
    # Create a temporary directory for the test
    tempdir = tempfile.mkdtemp()
    os.chmod(tempdir, 0o755)
    # Create a file in the working directory which

# Generated at 2022-06-13 06:27:26.437942
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    _test_parse_systemctl_show_get_lines = lambda s: s.strip().split('\n')

# Generated at 2022-06-13 06:27:35.827793
# Unit test for function main
def test_main():
    ''' Test function main
    :return:
    '''
    with patch.object(AnsibleModule, 'run_command') as mock_run_command:
        with patch.object(AnsibleModule, 'get_bin_path') as mock_get_bin_path:
            with patch.object(AnsibleModule, 'fail_json') as mock_fail_json:
                mock_get_bin_path.return_value = 'foo/bin/systemctl'
                mock_run_command.return_value = (1, '', '')

# Generated at 2022-06-13 06:27:59.448524
# Unit test for function main
def test_main():
    class Args(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)


# Generated at 2022-06-13 06:28:12.181788
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    input = '''Description=My service
After=network.target
ExecStart=/bin/bash -c 'echo starting'
ExecStop=/bin/bash -c 'echo stopping'
ExecReload=/bin/bash -c 'echo reloading'
ExecStartPre=/bin/bash -c 'echo starting pre'
ExecStartPost=/bin/bash -c 'echo starting post'
ExecRestart=/bin/bash -c 'echo restarting'
ExecStopPost=/bin/bash -c 'echo stopping post'
        '''

# Generated at 2022-06-13 06:28:23.363905
# Unit test for function main
def test_main():
    args = dict(
        name='foo',
        state='started',
        enabled=False,
        masked=False,
        daemon_reload=True,
        daemon_reexec=False,
        force=False,
        scope='system',
        no_block=False,
    )
    mock_module = MagicMock(spec=AnsibleModule)
    mock_module.run_command = MagicMock(return_value=(0, b'bar', ''))
    mock_module.get_bin_path = MagicMock(return_value='/bin/systemctl')
    mock_module.check_mode = False
    mock_module.params = args
    with monkeypatch.context() as m:
        m.setenv('XDG_RUNTIME_DIR', None)

# Generated at 2022-06-13 06:28:33.805125
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    assert parse_systemctl_show(['Description=This is a description']) == {'Description': 'This is a description'}
    assert parse_systemctl_show(['Description={', 'This is a description', '}']) == {'Description': 'This is a description'}
    assert parse_systemctl_show(['Description={', 'This is a description', 'that spans', 'multiple lines', '}']) == {'Description': 'This is a description\nthat spans\nmultiple lines'}

# Generated at 2022-06-13 06:28:40.663847
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    assert parse_systemctl_show([]) == {}
    assert parse_systemctl_show(['foo=']) == {'foo': ''}
    assert parse_systemctl_show(['foo=bar']) == {'foo': 'bar'}
    assert parse_systemctl_show(['foo=bar', 'baz=']) == {'foo': 'bar', 'baz': ''}
    assert parse_systemctl_show(['foo=b ar', 'baz=']) == {'foo': 'b ar', 'baz': ''}
    assert parse_systemctl_show(['foo=bar', 'baz=qux']) == {'foo': 'bar', 'baz': 'qux'}

# Generated at 2022-06-13 06:28:49.770952
# Unit test for function main
def test_main():
    '''
    Unit test function for function main
    '''
    module = _get_module_mock()
    action = "test action"
    rc = 1
    out = "test output"
    err = "test error"
    module.run_command = _get_run_command_mock(rc, out, err)
    module.exit_json = _get_exit_json_mock(module)
    unit = "test unit"
    module.params = _get_params_mock(unit)
    module.fail_json = _get_fail_json_mock(module)

    module.warn = _get_warn_mock(module)
    module.get_bin_path = _get_get_bin_path_mock(module)

# Generated at 2022-06-13 06:28:52.602189
# Unit test for function main
def test_main():
    pass


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:29:01.171005
# Unit test for function main
def test_main():
    import os
    import tempfile
    import shutil
    import sys
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule

    def generate_fake_systemctl():
        def fake_systemctl(args):
            pass
        return fake_systemctl


# Generated at 2022-06-13 06:29:08.088616
# Unit test for function main
def test_main():
    class TestAnsibleModuleMock(AnsibleModule):
        def __init__(self, *args, **kwargs):
            self.params = kwargs['argument_spec']
            self.exit_json = lambda **kwargs: None
            self.fail_json = lambda msg: None
            self.run_command = lambda command, check_rc=False, executable=None: (0, 'systemctl', '')
        def warn(self, msg):
            print(msg)


# Generated at 2022-06-13 06:29:10.955629
# Unit test for function main
def test_main():
    if __name__ == '__main__':
        main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:29:44.546546
# Unit test for function main
def test_main():
    import json
    import sys
    # print(sys.argv)
    # print(sys.stdin)
    if len(sys.argv) != 2:
        raise Exception("missing state parameter")

    state = sys.argv[1]
    if "active" in state:
        state_int = 1
    else:
        state_int = 0

    print(json.dumps({ "ansible_facts": { "service_state": state_int } }))

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()
    # test_main()

# Generated at 2022-06-13 06:29:48.366018
# Unit test for function main
def test_main():
    with patch('ansible.module_utils.basic.AnsibleModule.get_bin_path') as get_bin_path:
        get_bin_path.return_value='systemctl'
        main()
# Import module snippets
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:29:55.088104
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    result = parse_systemctl_show("""
Id=basic.target
Names=basic.target
Requires=system.slice
Wants=
BoundBy=
Conflicts=shutdown.target
Before=shutdown.target
After=system.slice sysinit.target
Documentation=man:systemd.special(7)
Description=Basic System
Documentation=man:systemd.special(7)
RequiresMountsFor=/
DefaultDependencies=no
Requires=system.slice
Wants=
""".split('\n'))

# Generated at 2022-06-13 06:30:03.103847
# Unit test for function main

# Generated at 2022-06-13 06:30:09.055997
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:30:19.166876
# Unit test for function main
def test_main():
    print('Testing for main function')

    # Create a mock module
    class MockModule:
        def __init__(self):
            self.params = {
                'name': 'fake_service',
                'masked': False,
                'daemon_reload': False,
            }
            self.check_mode = False
        def run_command(self, command):
            if command.startswith('/bin/systemctl list-unit-files fake_service'):
                if command.startswith('/bin/systemctl list-unit-files fake_service | grep -E "^fake_service"'):
                    print('Mock, command: %s' % command)
                    return 1, '', 'Unknown service: fake_service'
                else:
                    print('Mock, command: %s' % command)
                    return 0

# Generated at 2022-06-13 06:30:27.434934
# Unit test for function main
def test_main():
    module = AnsibleModule({
        'name': "autofs.service",
        'enabled': True,
        'state': "started"
    })
    module.warn = mock.MagicMock()
    module.fail_json = mock.MagicMock()
    module.run_command = mock.MagicMock()
    module.run_command.return_value = 0, "", ""
    main()
