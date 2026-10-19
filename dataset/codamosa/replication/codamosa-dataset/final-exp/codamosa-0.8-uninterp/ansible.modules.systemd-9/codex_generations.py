

# Generated at 2022-06-13 06:21:24.345281
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={})
    try:
        main()
    except SystemExit as e:
        e = str(e)
        if e == "0":
            return True
        else:
            raise

# import module snippets
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:31.507899
# Unit test for function main
def test_main():
    """
    This is the main test, only imported if ansible_module_runtime is set to nose
    """
    # These imports are only available on the system running the test, not the remote host
    import mock

    unit = 'sshd'
    state = 'started'
    enabled = None
    masked = None
    daemon_reload = False
    systemctl = '/usr/bin/systemctl'
    is_initd = False
    is_systemd = True
    # Set up our mock_module and some needed variables
    mock_module = mock.MagicMock()
    mock_module.params = {'name': unit, 'state': state, 'enabled': enabled, 'masked': masked,
                          'daemon_reload': daemon_reload, 'systemctl': systemctl}
    mock_module.check_mode = False

# Generated at 2022-06-13 06:21:43.567337
# Unit test for function main

# Generated at 2022-06-13 06:21:51.717507
# Unit test for function main
def test_main():
    '''
    Unit test for function main
    '''

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.systemd import sysv_exists


# Generated at 2022-06-13 06:22:05.034951
# Unit test for function main
def test_main():
    unit = "foobar"
    systemctl = ["/bin/systemctl"]
    state =  'started'

# Generated at 2022-06-13 06:22:06.487391
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('ignoring command (start/stop not enabled)')
    assert request_was_ignored('ignoring request (already started)')
    assert not request_was_ignored('static')



# Generated at 2022-06-13 06:22:18.123818
# Unit test for function main

# Generated at 2022-06-13 06:22:30.176466
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:22:41.479564
# Unit test for function main
def test_main():
    unit_name = 'sshd.service'
    state = 'started'
    result = dict(
        changed = False,
        status = {},
    )
    is_systemd = True
    is_initd = False
    enabled = True
    is_running = True
    action = 'start'
    module = DummyModule(unit = unit_name, state = state, enabled = enabled)
    module.warn = lambda x: None

    if is_initd and not is_systemd:
        module.warn('The service (%s) is actually an init script but the system is managed by systemd' % unit_name)

    if action:
        result['changed'] = True
        result['state'] = 'started'

# Generated at 2022-06-13 06:22:51.811388
# Unit test for function main

# Generated at 2022-06-13 06:23:24.283111
# Unit test for function main

# Generated at 2022-06-13 06:23:33.061689
# Unit test for function main
def test_main():
    import os
    import tempfile

    # Dummy AnsibleModule
    class DummyAnsibleModule(object):
        def __init__(self):
            self.params = {
                'state': None,
                'enabled': None,
                'masked': None,
                'name': 'autotest',
                'force': False,
                'daemon_reload': False,
                'daemon_reexec': False,
                'scope': 'system',
                'no_block': False,
            }
            self.check_mode = False

        def run_command(self, cmd, check_rc=False):
            return 0, '', ''

        def fail_json(self, **kwargs):
            raise Exception(kwargs)

        def exit_json(self, **kwargs):
            pass

       

# Generated at 2022-06-13 06:23:41.946650
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:23:52.514711
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    assert parse_systemctl_show(['Id=mysvc.service']) == {'Id': 'mysvc.service'}
    assert parse_systemctl_show(['Id=mysvc.service']) == {'Id': 'mysvc.service'}
    assert parse_systemctl_show(['Id=mysvc.service', 'Description=my desc']) == {
        'Id': 'mysvc.service',
        'Description': 'my desc'
    }
    assert parse_systemctl_show(['Id=mysvc.service', 'ExecStart=my command']) == {
        'Id': 'mysvc.service',
        'ExecStart': 'my command'
    }

# Generated at 2022-06-13 06:23:59.467105
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    sample_input = '''\
ActiveEnterTimestampMonotonic=8135942
ActiveExitTimestampMonotonic=0
ActiveState=active
After=auditd.service systemd-user-sessions.service time-sync.target
After=systemd-journald.socket basic.target system.slice
'''.split('\n')

    expected = {
        'ActiveEnterTimestampMonotonic': '8135942',
        'ActiveExitTimestampMonotonic': '0',
        'ActiveState': 'active',
        'After': 'auditd.service systemd-user-sessions.service time-sync.target systemd-journald.socket basic.target system.slice',
    }

    assert expected == parse_systemctl_show(sample_input)
test_parse_systemctl_show()



# Generated at 2022-06-13 06:24:11.598946
# Unit test for function main

# Generated at 2022-06-13 06:24:13.976453
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleExitJson) as exec_info:
        main()
    assert exec_info.value.args[0]['changed'] == False


# Generated at 2022-06-13 06:24:22.916986
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:24:35.064574
# Unit test for function main
def test_main():
    from ansible.module_utils.systemd import main
    from ansible.module_utils.systemd import sysv_exists
    from ansible.module_utils.systemd import sysv_is_enabled
    from ansible.module_utils.systemd import is_running_service
    from ansible.module_utils.systemd import is_deactivating_service
    from ansible.module_utils.systemd import request_was_ignored
    from ansible.module_utils.systemd import is_chroot
    from ansible.module_utils.systemd import fail_if_missing
    from ansible.module_utils.systemd import parse_systemctl_show
    from ansible.module_utils.basic import AnsibleModule
    import os

    module = AnsibleModule(argument_spec={})

    module.run_

# Generated at 2022-06-13 06:24:43.507088
# Unit test for function main
def test_main():
    #function load_systemctl_status
    assert load_systemctl_status('ActiveState=running\n') == {'ActiveState': 'running'}
    assert load_systemctl_status('ActiveState=inactive') == {'ActiveState': 'inactive'}
    assert load_systemctl_status('ActiveState=active\n') == {'ActiveState': 'active'}
    assert load_systemctl_status('ActiveState=failed\n') == {'ActiveState': 'failed'}
    assert load_systemctl_status('ActiveState=activating\n') == {'ActiveState': 'activating'}
    assert load_systemctl_status('ActiveState=deactivating\n') == {'ActiveState': 'deactivating'}

    #function is_running_service

# Generated at 2022-06-13 06:25:08.712847
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    lines = [
        'Description=Command Scheduler',
        'ExecStart={ path=/usr/sbin/crond ; argv[]=/usr/sbin/crond -n $CRONDARGS ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }',
        'ExecReload={ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }',
    ]
    parsed = parse_systemctl_show(lines)
    assert parsed['Description'] == 'Command Scheduler'

# Generated at 2022-06-13 06:25:20.352602
# Unit test for function main
def test_main():
    # mock function for function main
    def mock_run_command(*args, **kwargs):
        class Object(object):
            pass
        retn = Object()
        retn.rc = 0
        retn.stdout = "mock_stdout"
        retn.stderr = "mock_stderr"
        return retn
    # mock function for function to_native
    def mock_to_native(*args, **kwargs):
        return "mock_to_native"
    # mock function for function parse_systemctl_show
    def mock_parse_systemctl_show(*args, **kwargs):
        return "mock_parse_systemctl_show"
    # mock function for function sysv_exists

# Generated at 2022-06-13 06:25:26.292824
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    output = [
        'ActiveEnterTimestamp=Sun 2016-05-15 18:28:49 EDT',
        'ActiveEnterTimestampMonotonic=8135942',
        'ActiveExitTimestampMonotonic=0',
        'ActiveState=active',
        'Transient=no',
        'UnitFileState=enabled',
        'Description=Command Scheduler',
        'ExecStart={ path=/usr/sbin/crond ; argv[]=/usr/sbin/crond -n $CRONDARGS ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }',
        'ExecReload=/bin/kill -HUP $MAINPID',
        'MainPID=595',
    ]

# Generated at 2022-06-13 06:25:36.491539
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:25:44.036812
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    lines_1 = '''ExecMainStartTimestamp=Sun 2016-05-15 18:28:49 EDT
ExecMainStartTimestampMonotonic=8134990
ExecMainStatus=0'''.splitlines()
    lines_2 = '''ExecMainStartTimestamp=Sun 2016-05-15 18:28:49 EDT
ExecMainStartTimestampMonotonic=8134990
ExecMainStatus={ status_dict }'''.splitlines()
    lines_3 = '''ExecMainStartTimestamp=Sun 2016-05-15 18:28:49 EDT
ExecMainStartTimestampMonotonic=8134990
ExecMainStatus={ status_dict
    with more
    lines
    than
    one }'''.splitlines()


# Generated at 2022-06-13 06:25:54.372877
# Unit test for function main
def test_main():
    unit = 'sshd'

    rc = 0
    out = err = ''
    result = {
        'name': unit,
        'changed': False,
        'status': {},
    }

    # Check if we are supposed to return changed or not

# Generated at 2022-06-13 06:26:02.341899
# Unit test for function main
def test_main():
    unit = 'foo.service'
    action = 'start'
    systemctl = '/bin/systemctl'
    scope = 'system'

    # Test result for command: systemctl start foo.service
    systemctl_start = {
        'rc': 0,
        'stdout': '',
        'stderr': ''
    }

    # Test result for command: systemctl daemon-reload
    systemctl_daemon_reload = {
        'rc': 0,
        'stdout': '',
        'stderr': ''
    }

    class AnsibleModule:
        def __init__(self, argument_spec, supports_check_mode, required_one_of, required_by):
            self.check_mode = False

# Generated at 2022-06-13 06:26:04.605476
# Unit test for function main
def test_main():
    module = AnsibleModule({ }, { })
    module.exit_json = lambda x, **kw: print(x)
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:26:15.434123
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    out = '''Description=A multi-line value
that is surrounded by {}
{
    Another line
    Another line that ends with }
}

OtherOutput=single line value
OtherOutput2=single line value with {

ExecStart={
    This starts with {
    But continues onto multiple lines
    }
}'''

    parsed = parse_systemctl_show(out.splitlines())
    assert parsed['Description'] == 'A multi-line value\nthat is surrounded by {}\n{\n    Another line\n    Another line that ends with }\n}'
    assert parsed['OtherOutput'] == 'single line value'
    assert parsed['OtherOutput2'] == 'single line value with {'
    assert parsed['ExecStart'] == '''{\n    This starts with {\n    But continues onto multiple lines\n    }\n}'''

# Generated at 2022-06-13 06:26:20.766290
# Unit test for function main

# Generated at 2022-06-13 06:26:51.805306
# Unit test for function main
def test_main():
    argv = sys.argv
    sys.argv = argv[:1]
    sys.argv.extend(['-vvv', '-m', 'systemd', '-a', 'name=httpd', '-a', 'state=started', '-a', 'enabled=yes'])
    sys.argv.extend(['-vvv', '-m', 'systemd', '-a', 'name=httpd', '-a', 'state=stopped', '-a', 'enabled=no'])
    sys.argv.extend(['-vvv', '-m', 'systemd', '-a', 'name=httpd', '-a', 'enabled=yes'])

# Generated at 2022-06-13 06:27:04.584305
# Unit test for function main
def test_main():
    # Mock the module, state, and params
    mock_module = MagicMock()
    mock_module.params = {'name':'some.service', 'state':'stopped'}
    mock_module.check_mode = False

    # Mock the systemctl command
    mock_systemctl = MagicMock()
    mock_systemctl.return_value = ('Output', 'Error', 0)
    mock_module.get_bin_path.return_value = 'systemctl'

    # Mock the status
    mock_status = MagicMock()
    mock_status.return_value = 'active'

    # Mock the module.run_command
    mock_run_command = MagicMock()
    mock_run_command.return_value = ('Output', 'Error', 0)

    # Set up the mocked objects

# Generated at 2022-06-13 06:27:15.469135
# Unit test for function main
def test_main():
    unit_test = []
    # if scope is 'system' or None, we can ignore as there is no extra switch. The other choices match the corresponding switch
    unit_test.append({'params': dict(scope='system')})
    unit_test.append({'params': dict(scope='user')})
    unit_test.append({'params': dict(scope='global')})
    unit_test.append({'params': dict(no_block=True)})
    unit_test.append({'params': dict(force=True)})
    unit_test.append({'params': dict(masked=False)})
    # Run daemon-reload
    unit_test.append({'params': dict(daemon_reload=True)})
    unit_test.append({'params': dict(daemon_reexec=True)})

# Generated at 2022-06-13 06:27:17.728342
# Unit test for function main
def test_main():
    # NOTE: even though the following lines are hard-coded strings,
    # it's ok because this is meant to be unit-tested
    assert main() is None

# Generated at 2022-06-13 06:27:25.196374
# Unit test for function main

# Generated at 2022-06-13 06:27:29.426377
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Produce output that looks like the output of `systemctl show` for a unit that has
    # both a single-line value and a multi-line value.
    f = StringIO()
    print('Description=single-line value', file=f)
    print('ExecStart=', file=f)
    print(' {', file=f)
    print('  Command1', file=f)
    print('  Command2', file=f)
    print(' }', file=f)
    # Note: The original version of this code would incorrectly consume all remaining lines as
    # part of the multi-line value, so we don't need lines that follow this point.
    f.seek(0)

# Generated at 2022-06-13 06:27:37.434192
# Unit test for function main
def test_main():
    # Test for scope=system
    module = ansible_module_create()
    ansible_module_set_arguments(module, daemon_reload=True, name="cron", state="stopped", enabled=False, mask=False, daemon_reexec=True, no_block=True)
    rc, out, err = ansible_module_run(module, False)
    assert rc == 0 and len(err) == 0 and "stopped" in out

    # Test for scope=user
    module = ansible_module_create()
    ansible_module_set_arguments(module, daemon_reload=True, name="cron", state="stopped", enabled=False, mask=False, daemon_reexec=True, no_block=True, scope="user")
    rc, out, err = ansible_module_

# Generated at 2022-06-13 06:27:52.757273
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:27:58.916184
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={})
    exit_args = {}
    main()
    while True:
        exit_args['changed'] = True
        exit_args['name'] = 'test'
        exit_args['status'] = 'Status'
        exit_args['state'] = 'state_value'
        exit_args['enabled'] = False
        module.exit_json(**exit_args)

# Main function that starts the module execution
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:11.913148
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:28:47.529212
# Unit test for function main
def test_main():
    args = {
        'daemon_reload': False,
        'daemon_reexec': False,
        'enabled': False,
        'force': False,
        'masked': False,
        'name': 'tcpdump',
        'no_block': False,
        'scope': 'system',
        'state': None
    }
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)

    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:55.463391
# Unit test for function main
def test_main():
    # Find the unit test directory
    unit_test_dir = os.path.dirname(os.path.realpath(__file__))

    # Establish path to sysvinit script and ensure it exists
    init_script_path = os.path.join(unit_test_dir, 'test_init_d_script')
    assert os.path.isfile(init_script_path)

    # Establish path to systemd unit, and ensure it exists
    unit_file_path = os.path.join(unit_test_dir, 'test.service')
    assert os.path.isfile(unit_file_path)

    # Create the module object reference
    module = AnsibleModule(argument_spec=dict())

    # Set the module's options to values that would normally be provided
    # to ansible-playbook

# Generated at 2022-06-13 06:28:57.829535
# Unit test for function main
def test_main():
    with pytest.raises(Exception) as excinfo:
        main()
    assert 'either state or enabled is required' in str(excinfo.value)


# Generated at 2022-06-13 06:29:04.723344
# Unit test for function main
def test_main():
    test_unit = 'test_unit'
    test_unit_full = 'test_unit.service'
    test_unit_full_at = 'test_unit@.service'
    test_unit_full_after = 'test_unit.service.d/test.conf'
    test_user = 'test_user'

    # Test 1 - make sure state can be set to stopped for a non-existant unit file
    params = {
        'name': test_unit,
        'state': 'stopped',
        'enabled': False,
        'masked': False,
    }

# Generated at 2022-06-13 06:29:10.127709
# Unit test for function main

# Generated at 2022-06-13 06:29:19.145424
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    assert parse_systemctl_show([
        "Id=httpd.service",
        "Names=httpd.service",
        "Description=The Apache HTTP Server",
        "After=network.target remote-fs.target nss-lookup.target",
        "Wants=auth-rpcgss-module.service nfs-config.service"
    ]) == {
        'Id': 'httpd.service',
        'Description': 'The Apache HTTP Server',
        'After': 'network.target remote-fs.target nss-lookup.target',
        'Wants': 'auth-rpcgss-module.service nfs-config.service',
        'Names': 'httpd.service'
    }



# Generated at 2022-06-13 06:29:25.687803
# Unit test for function main
def test_main():
    from ansible.modules.system.systemd import main
    from ansible.module_utils.systemd import Systemd
    import pytest

    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:29:33.733530
# Unit test for function main
def test_main():
    new_module = basic.AnsibleModule({'scope': 'system', 'daemon_reexec': 'False', 'no_block': 'False', 'force': 'False', 'state': 'reloaded', 'enabled': 'False', 'masked': 'False', 'name': 'zabbix-agent', 'daemon_reload': 'False'}, check_invalid_arguments=False)
    new_module.warn = MagicMock()
    new_module.fail_json = MagicMock()
    new_module.fail_json.side_effect = Exception
    new_module.run_command = MagicMock(return_value=(0,'','',))
    new_module.get_bin_path = MagicMock(return_value='/bin/systemctl')

# Generated at 2022-06-13 06:29:43.441636
# Unit test for function main
def test_main():
    argument_spec = dict(
        name=dict(type='str', aliases=['service', 'unit']),
        state=dict(type='str', choices=['reloaded', 'restarted', 'started', 'stopped']),
        enabled=dict(type='bool'),
        force=dict(type='bool'),
        masked=dict(type='bool'),
        daemon_reload=dict(type='bool', default=False, aliases=['daemon-reload']),
        daemon_reexec=dict(type='bool', default=False, aliases=['daemon-reexec']),
        scope=dict(type='str', default='system', choices=['system', 'user', 'global']),
        no_block=dict(type='bool', default=False),
    )

# Generated at 2022-06-13 06:29:53.186571
# Unit test for function main