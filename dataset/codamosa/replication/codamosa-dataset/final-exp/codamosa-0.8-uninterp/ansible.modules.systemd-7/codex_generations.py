

# Generated at 2022-06-13 06:21:30.693083
# Unit test for function main
def test_main():
    import ansible.module_utils.systemd.running as running_mock
    running_mock.is_running_service = lambda x: True
    running_mock.is_deactivating_service = lambda x: False
    running_mock.is_chroot = lambda x: False
    result = dict(
        name="test.service",
        changed=True,
        status=dict(
            ActiveState="active",
            SubState="running",
            UnitFileState="enabled"
        ),
        state="started",
        enabled=True
    )
    assert main(dict(name="test.service", state="started", enabled="yes", daemon_reload="no", no_block="no", daemon_reexec="no")) == result

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:36.037112
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert(request_was_ignored(u'') is False)
    assert(request_was_ignored(u'=') is False)
    assert(request_was_ignored(u'=foo') is False)
    assert(request_was_ignored(u'foo=') is False)
    assert(request_was_ignored(u'foo=bar') is False)
    assert(request_was_ignored(u'ignoring request') is True)
    assert(request_was_ignored(u'ignoring command') is True)
    assert(request_was_ignored(u'foo ignoring request') is True)
    assert(request_was_ignored(u'foo ignoring command') is True)
    assert(request_was_ignored(u'ignoring request bar') is True)

# Generated at 2022-06-13 06:21:39.842234
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    multiline_value = '''{
        path=/usr/bin/bluetoothd ;
        argv[]=/usr/bin/bluetoothd -C ;
        ignore_errors=no ;
        start_time=[n/a] ;
        stop_time=[n/a] ;
        pid=0 ;
        code=(null) ;
        status=0/0
    }'''
    assert parse_systemctl_show(['ExecStart=' + multiline_value]) == {'ExecStart': multiline_value}



# Generated at 2022-06-13 06:21:50.605970
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:22:04.042207
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:22:09.191322
# Unit test for function main
def test_main():
    from ansible.modules.system.systemd import main
    sys.modules['ansible.modules.system.systemd'].__package__ = 'ansible.modules.system'

    with pytest.raises(SystemExit):
        main('/usr/lib/systemd/system/sshd.service', state='stopped')


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:14.163465
# Unit test for function main
def test_main():
    import platform

    class MockSystemctl(object):
        def __init__(self):
            self.version = 'systemd 219\n +PAM +AUDIT +SELINUX +IMA -APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ -LZ4 -SECCOMP +BLKID -ELFUTILS +KMOD +IDN'

# Generated at 2022-06-13 06:22:24.143722
# Unit test for function main

# Generated at 2022-06-13 06:22:34.239875
# Unit test for function main
def test_main():
    if not os.path.exists("systemd_service/main.py"):
        raise SkipTest("test/unit/systemd_service/main.py not found.")
    if not os.path.exists("test/unit/systemd_service/main.json"):
        raise SkipTest("test/unit/systemd_service/main.json not found.")
    script_args = [
        "systemd_service/main.py",
        "--tb=no",
        "--args",
        "script",
        "systemd_service/main.py",
        "test/unit/systemd_service/main.json"
    ]
    code, stdout, stderr = module_utils.basic_module_exec(script_args)
    assert code == 0,"non-zero return code"
    assert st

# Generated at 2022-06-13 06:22:45.901376
# Unit test for function main
def test_main():
    import os
    import json
    import pytest

    unit = 'sshd'

# Generated at 2022-06-13 06:23:12.866387
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:23:20.398970
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    """Test parse_systemctl_show."""
    # pylint: disable=unused-argument
    def run_test(input_, expected):
        """Run a test case."""
        res = parse_systemctl_show(input_)
        assert res == expected
    run_test([], {})
    run_test(['Foo=Bar'], {'Foo': 'Bar'})
    run_test(['Foo={Bar'], {'Foo': '{Bar'})
    run_test(['Foo={Bar\nBaz\n}'], {'Foo': '{Bar\nBaz\n}'})
    run_test(['Foo={Bar\nBaz'], {'Foo': '{Bar\nBaz'})

# Generated at 2022-06-13 06:23:29.865743
# Unit test for function main

# Generated at 2022-06-13 06:23:40.160965
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 06:23:52.176648
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:23:59.237720
# Unit test for function main
def test_main():
    # mock unit test : return_value = ([returncode, out, err])
    import platform
    import types
    unit = "123"
    mock_module = types.ModuleType('ansible.module_utils.basic')
    mock_module.run_command = lambda x: [0, '', '']
    mock_module.get_bin_path = lambda x, y: "systemctl"
    mock_module.HAS_PYTHON26 = False
    mock_module.AnsibleModule = types.ClassType('ansible.module_utils.basic.AnsibleModule')
    mock_module.AnsibleModule.exit_json = lambda x, **kwargs: 0
    mock_module.AnsibleModule.fail_json = lambda x, **kwargs: 0
    mock_module.AnsibleModule.run_

# Generated at 2022-06-13 06:24:11.236371
# Unit test for function main
def test_main():
    sys.modules['ansible.module_utils.ansible_release'] = MagicMock(return_value=(2, 8, 0))
    sys.modules['ansible.module_utils.distro'] = MagicMock(return_value='redhat')
    sys.modules['ansible.module_utils.six.moves.shutil'] = shutil
    sys.modules['ansible.module_utils.six.moves.tempfile'] = tempfile
    sys.modules['ansible.module_utils.six'] = MagicMock(**{'binary_type.return_value': type(b'')})
    sys.modules['ansible.module_utils.basic.AnsibleModule'] = MagicMock(return_value='"changed": false')
    sys.modules['ansible.module_utils.basic'] = MagicMock()

# Generated at 2022-06-13 06:24:13.925544
# Unit test for function main
def test_main():
    main()

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:22.843731
# Unit test for function main
def test_main():
    ''' test_main
    This function tests the main branch of the program
    '''

    # Testing with exit_json
    m = ansible_module_mock()
    m.params = dict(
                name=None,
                state=None,
                daemon_reload=False,
                daemon_reexec=False,
        )
    with pytest.raises(SystemExit):
        main()

    # Testing with fail_json
    m = ansible_module_mock()
    m.params = dict(
                name='myservice',
                state=None,
                daemon_reload=False,
                daemon_reexec=False,
        )
    with pytest.raises(SystemExit):
        main()

    # Testing with exit_json
    m = ansible_module_mock()

# Generated at 2022-06-13 06:24:34.839217
# Unit test for function main
def test_main():
    args = dict(
        daemon_reload=False,
        daemon_reexec=False,
        force=False,
        masked=False,
        name=None,
        no_block=False,
        scope="system",
        state="running",
        enabled=False
    )
    module = AnsibleModule(argument_spec=args)
    unit = module.params['name']
    systemctl = module.get_bin_path('systemctl', True)

    rc = 0
    out = err = ''

    # Run daemon-reload first, if requested
    if module.params['daemon_reload'] and not module.check_mode:
        (rc, out, err) = module.run_command("%s daemon-reload" % (systemctl))
        if rc != 0:
            module.fail_json

# Generated at 2022-06-13 06:25:43.775827
# Unit test for function main
def test_main():
    unit = dict()
    unit['name'] = 'systemd-sysctl'
    unit['masked'] = 'False'
    unit['enabled'] = 'True'
    unit['state'] = ''
    unit['force'] = 'False'
    unit['daemon_reload'] = 'False'
    unit['daemon_reexec'] = 'False'
    unit['scope'] = 'system'
    unit['no_block'] = 'False'
    module = dict()
    module['state'] = 'True'
    module['name'] = 'systemd-sysctl'

    main()
# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:54.216800
# Unit test for function main

# Generated at 2022-06-13 06:26:02.308518
# Unit test for function main

# Generated at 2022-06-13 06:26:07.968442
# Unit test for function main
def test_main():
    """If using ssh connection, ansible-playbook returns an unhandled error message when
    return rc != 0 and stderr is not empty because ssh connection would fail.
    This causes the unit test to fail.
    """

# Generated at 2022-06-13 06:26:16.955945
# Unit test for function main

# Generated at 2022-06-13 06:26:22.788818
# Unit test for function main
def test_main():
    test_args = [
        "name=httpd",
        "state=reloaded"
    ]

    test_options = prepare_options(test_args)
    result = main(test_args, test_options) 
    if not result:
        print("Unit test for function main() failed.")

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:26:26.216930
# Unit test for function main
def test_main():
    module = AnsibleModule({'name': 'sshd', 'state': 'stopped'},
                           check_invalid_arguments=False)
    assert module.params['name'] == 'sshd'
    assert module.params['state'] == 'stopped'


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:26:35.773116
# Unit test for function main
def test_main():
    args = dict(
      name='sshd'
    )

# Generated at 2022-06-13 06:26:45.969233
# Unit test for function main
def test_main():
    argv = [
        'systemctl.py',
        'name=cloudera-scm-server',
        'state=restarted',
        'enabled=True',
        'masked=False',
        'daemon_reload=False',
        'daemon_reexec=False',
        'scope=system',
        'no_block=False'
    ]
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0



# Generated at 2022-06-13 06:26:55.258403
# Unit test for function main
def test_main():
    ''' ansible-test cases '''

# Generated at 2022-06-13 06:28:07.824389
# Unit test for function main
def test_main():
    def test_module(module):
        pass
    main(module=test_module)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:19.484532
# Unit test for function main
def test_main():
    # preparing the test
    test_unit_path = os.path.join(os.path.dirname(__file__), 'test_units')
    local_test_units = [fname for fname in os.listdir(test_unit_path) if os.path.isfile(os.path.join(test_unit_path, fname)) and fname.endswith('.service')]
    for unit in local_test_units:
        unit = os.path.join(test_unit_path, unit)
        shutil.copy2(unit, './')

    # prepare the mock

# Generated at 2022-06-13 06:28:22.940056
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(argument_spec={})
    module.exit_json = lambda **kwargs: None
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:33.496301
# Unit test for function main

# Generated at 2022-06-13 06:28:40.436561
# Unit test for function main
def test_main():
    # Mock
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.systemd import (
        sysv_is_enabled,
        sysv_exists,
        is_running_service,
        is_deactivating_service,
        request_was_ignored,
        parse_systemctl_show,
        to_native,
        is_chroot
    )

    class MockAnsibleModule:
        def __init__(self, params, check_mode=True, run_command=None, fail_json=None, exit_json=None, warn=None):
            self.params = params
            self.check_mode = check_mode
            self.run_command = run_command
            self.fail_json = fail_json or self.fail_json_default
            self

# Generated at 2022-06-13 06:28:51.345450
# Unit test for function main
def test_main():
    # test as a systemd unit
    test_args = dict(
        state='started',
        name='unbound.service',
    )
    ansible_module_main(test_args)

    # test as a sysv service
    test_args = dict(
        state='started',
        name='unbound',
    )
    ansible_module_main(test_args)

    # test as a invalid service
    test_args = dict(
        state='started',
        name='invalid.service',
    )
    ansible_module_main(test_args)

    # test as a invalid sysv service
    test_args = dict(
        state='started',
        name='invalid',
    )
    ansible_module_main(test_args)

    # test as a service unit with param
    test

# Generated at 2022-06-13 06:29:00.669726
# Unit test for function main
def test_main():
    '''Ansible systemctl module unit test template'''
    # Test variables
    systemctl = '/usr/bin/systemctl'
    # Mock for systemctl command
    mock_args = [
        '/usr/bin/systemctl',
        "--scope=system",
        "stop",
        "rsyslog",
    ]
    mock_rc = 0
    mock_stdout = "Active: active (running)"
    mock_stderr = "Unit rsyslog.service could not be found."
    m_systemctl = mock.Mock(return_value=(mock_rc, mock_stdout, mock_stderr))

    # Module arguments

# Generated at 2022-06-13 06:29:07.813833
# Unit test for function main

# Generated at 2022-06-13 06:29:18.358703
# Unit test for function main
def test_main():
    ''' Unit test for main() '''

    # Test for bad scope
    scope = "system"
    systemctl = "systemctl"
    if scope != "system":
        systemctl += " --%s" % scope
    
    systemctl += " daemon-reload"
    systemctl += " --no-block"
    systemctl += " --force"
    systemctl += " daemon-reexec"

    rc = 0
    out = ""
    err = ""
    unit = ""

    found = False
    is_initd = True
    is_systemd = False

    ''' Test for list-unit-files'''
    rc = 0
    out = "test.service"
    err = ""
    unit = "test.service"
    is_systemd = out == unit


# Generated at 2022-06-13 06:29:29.974143
# Unit test for function main