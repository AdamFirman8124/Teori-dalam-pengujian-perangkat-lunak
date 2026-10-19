

# Generated at 2022-06-13 06:21:06.691811
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('ignoring request')
    assert request_was_ignored('ignoring command')
    assert not request_was_ignored('=')
    assert not request_was_ignored('/bin/systemctl status')



# Generated at 2022-06-13 06:21:14.201692
# Unit test for function main
def test_main():
    test_class = type('', (), {})
    module = test_class()
    module.run_command = Mock()
    module.get_bin_path = Mock(return_value='/bin/systemctl')
    module.check_mode = Mock()
    module.fail_json = Mock()
    module.warn = Mock()
    module.exit_json = Mock()
    main()
    assert module.exit_json.called


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:24.309716
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:31.479012
# Unit test for function main
def test_main():
    """
    Perform unit tests for main routine
    """

# Generated at 2022-06-13 06:21:34.039278
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('ignoring request')
    assert request_was_ignored('ignoring command')
    assert request_was_ignored('ignoring request and ignoring command')
    assert not request_was_ignored('ignoring request=')
    assert not request_was_ignored('ignoring command=')



# Generated at 2022-06-13 06:21:39.630840
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    lines = '''
Description=Crond
Documentation=man:crond(8) man:crontab(5)
'''.split('\n')
    assert len(parse_systemctl_show(lines)) == 1
    assert parse_systemctl_show(lines)['Description'] == 'Crond'

    lines = '''
Description=Unit Name
Documentation=man:hello(1)
refuse=manual
ExecStart={ path=/usr/bin/python ; argv[]=/usr/bin/python -s /usr/sbin/hello ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }
'''.split('\n')
    assert len(parse_systemctl_show(lines)) == 3
    assert parse_

# Generated at 2022-06-13 06:21:50.605576
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:53.415378
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('ignoring request') is True
    assert request_was_ignored('ignoring request: unit not loaded') is True
    assert request_was_ignored('ignoring command: unit not loaded') is True
    assert request_was_ignored('ignoring command') is True
    assert request_was_ignored('This is a long text which contains both ignoring command and the string "="') is False



# Generated at 2022-06-13 06:22:06.045956
# Unit test for function main

# Generated at 2022-06-13 06:22:17.984147
# Unit test for function main
def test_main():
    """
    Test systemd module
    """

    unit_name = "vsftpd.service"
    test_main_unit = {
        'name': unit_name,
        'state': None,
        'enabled': None,
        'masked': None,
        'force': False,
        'daemon_reload': False,
        'daemon_reexec': False,
        'scope': 'system',
    }

    module = AnsibleModule(
        argument_spec=test_main_unit.copy(),
        supports_check_mode=True,
    )

    systemctl = module.get_bin_path('systemctl', True)


# Generated at 2022-06-13 06:22:44.273299
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    test_multiline = """\
EnvironmentFile=/etc/sysconfig/rhn/satellite-sysid (ignore_errors=yes)
ExecStartPre=/bin/rm -f /var/run/rhn/satellite-sysid.file /var/run/rhn/osad-server.pid /var/spool/mqueue/o2s.*
ExecStart=/usr/sbin/rhn-satellite $DAEMON_OPTS
ExecStartPost=/bin/rm -f /var/lib/rhn/rhn_systemid.info
Restart=always
RestartSec=10
"""
    test_singleline = """\
Description=Command Scheduler
Documentation=man:crond(8) man:crontab(5)
"""

# Generated at 2022-06-13 06:22:53.901368
# Unit test for function main
def test_main():
    unit = 'sshd'
    state = 'started'
    enabled = None
    masked = None
    daemon_reload = None
    daemon_reexec = None
    scope = None
    no_block = None


# Generated at 2022-06-13 06:23:05.341945
# Unit test for function main

# Generated at 2022-06-13 06:23:13.516760
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:23:20.781792
# Unit test for function main
def test_main():
    import sys
    import __main__ as main
    main.systemctl = '/bin/systemctl'


# Generated at 2022-06-13 06:23:30.200820
# Unit test for function main
def test_main():
    # This is not a general test, it is only for testing the above interface integration.
    # There is no way to mock out systemctl in a deterministic manner.
    import os
    import shutil
    import tempfile
    from ansible.module_utils.common.systemd import sysv_exists, sysv_is_enabled, sysv_set_enabled
    from ansible.module_utils.basic import AnsibleModule
    class MockModule(AnsibleModule):
        def __init__(self, *args, **kwargs):
            super(MockModule, self).__init__(*args, **kwargs)
            self._sysv_init_dir = tempfile.mkdtemp()
            self.fail_json.__globals__['_ansible_tmpdir'] = tempfile.mkdtemp()
            self.exit

# Generated at 2022-06-13 06:23:40.194529
# Unit test for function main
def test_main():
    unit = {
        'name': 'foo',
        'state': 'started',
        'enabled': True,
        'masked': False,
        'daemon_reload': False,
        'daemon_reexec': True,
        'scope': 'system',
        'no_block': False
    }

# Generated at 2022-06-13 06:23:41.205936
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:52.261159
# Unit test for function main
def test_main():
    print("Test main() with unit=None", end=' ')
    unit_name = None

# Generated at 2022-06-13 06:23:59.291056
# Unit test for function main
def test_main():
    test_args = [
        'name',
        'state',
        'enabled',
        'force',
        'masked',
        'daemon_reload',
        'daemon_reexec',
        'scope',
        'no_block',
    ]
    test_vals = [
        'ansible',
        'running',
        True,
        True,
        True,
        True,
        True,
        'system',
        True
    ]

# Generated at 2022-06-13 06:24:24.920003
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:24:36.703854
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:24:48.103731
# Unit test for function main

# Generated at 2022-06-13 06:24:59.092812
# Unit test for function main

# Generated at 2022-06-13 06:25:09.671742
# Unit test for function main

# Generated at 2022-06-13 06:25:21.321952
# Unit test for function main
def test_main():
    with mock.patch('ansible_collections.ansible.community.plugins.module_utils.basic.AnsibleModule') as mock_amodule:
        import ansible_collections.ansible.community.plugins.modules.systemd.systemd as systemd
        mock_module = mock_amodule.return_value

# Generated at 2022-06-13 06:25:22.834781
# Unit test for function main
def test_main():
    with pytest.raises(Exception) as exc:
        main()
    assert 'AnsibleModule object' in str(exc.value)

# Generated at 2022-06-13 06:25:33.477353
# Unit test for function main

# Generated at 2022-06-13 06:25:34.731906
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:42.508231
# Unit test for function main

# Generated at 2022-06-13 06:26:16.255744
# Unit test for function main
def test_main():
    # Mock unit parameter
    unit = "os-collect-config"
    # Mock systemctl
    systemctl = "/usr/bin/systemctl"
    # Mock path
    path = "/path/to"
    # Mock module

# Generated at 2022-06-13 06:26:26.150964
# Unit test for function main
def test_main():
    unit_tests = [
        {
            'name': 'systemd',
            'params': {
                'name': 'foo',
                'state': None,
                'enabled': None
            },
            'output': {
                'state': None,
                'enabled': None,
                'changed': False,
                'status': {},
                'name': 'foo'
            }
        }
    ]
    for test in unit_tests:
        result = main(test['params'])
        if result != test['output']:
            print("Input: %s" % test['params'])
            print("Expected output: %s" % test['output'])
            print("Actual output: %s" % result)
            return False
    return True


# Generated at 2022-06-13 06:26:33.207130
# Unit test for function main
def test_main():
    unit = 'bluetooth.service'
    params = {}
    params['name'] = unit
    params['state'] = None
    params['enabled'] = None
    params['masked'] = None
    params['daemon_reload'] = False
    params['daemon_reexec'] = False
    params['scope'] = 'system'
    params['no_block'] = False
    params['force'] = False

# Generated at 2022-06-13 06:26:46.195067
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:26:56.350720
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:26:58.592165
# Unit test for function main
def test_main():
    with open('utils_systemd_test.json', 'r') as data_file:
        data = json.load(data_file)
    p = Mock(**data)
    main()
    p.fail_json.assert_not_called()


# Generated at 2022-06-13 06:27:08.544120
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:27:18.720088
# Unit test for function main

# Generated at 2022-06-13 06:27:26.081599
# Unit test for function main
def test_main():
    """ Unit test for function main """

# Generated at 2022-06-13 06:27:35.555095
# Unit test for function main

# Generated at 2022-06-13 06:28:12.887893
# Unit test for function main
def test_main():
  result = {"result":{}}
  result['msg'] = "test"
  assert result['msg'] == "test"

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.six import iteritems

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:22.558725
# Unit test for function main
def test_main():
    request = {
        "name":"cron",
        "state":"started",
        "enabled":"yes",
        "masked":None,
        "daemon_reload":False,
        "daemon_reexec":False,
        "force":False,
        "check_mode":False,
        "scope":"system",
        "no_block":False
    }
    result = main(request)
    assert result["changed"] == True
    assert result["name"] == "cron"
    assert result["status"]["ActiveState"] == "active"
    assert result["state"] == "started"

main()

# Generated at 2022-06-13 06:28:31.877157
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    test_output = [
        r'Id=some-service.service',
        r'Description=some description',
        r'ExecStart={',
        r'  PathExistsGlob=/foo/*.pid',
        r'  ExecStart=/bin/rm -f /foo/*.pid',
        r'}',
        r'Description=another description',
    ]
    parsed = parse_systemctl_show(test_output)
    expected = {
        'Id': 'some-service.service',
        'Description': 'another description',
        'ExecStart': '\n'.join(test_output[2:6]) + '\n',
    }
    assert parsed == expected



# Generated at 2022-06-13 06:28:39.293088
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:28:48.093439
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Normal line
    assert parse_systemctl_show(['foo=bar']) == {'foo': 'bar'}
    # Multi-line "Exec" value starting and ending on the same line
    assert parse_systemctl_show(['ExecStart={ foo; bar; }']) == {'ExecStart': '{ foo; bar; }'}
    # Multi-line "Exec" value starting and ending on different lines
    assert parse_systemctl_show(['ExecStart={\n  foo;\n  bar;\n}']) == {'ExecStart': '{\n  foo;\n  bar;\n}'}

# Generated at 2022-06-13 06:28:49.217670
# Unit test for function main
def test_main():
    assert True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:57.599815
# Unit test for function main
def test_main():
    out='''Loaded: loaded (/lib/systemd/system/openvas-scanner.service; enabled; vendor preset: enabled)
  Active: active (running) since Mon 2018-06-11 14:28:51 EDT; 13min ago
'''
    d=parse_systemctl_show(out.split('\n'))
    assert d['Loaded'] == '/lib/systemd/system/openvas-scanner.service; enabled; vendor preset: enabled'
    assert d['Active'] == 'active (running) since Mon 2018-06-11 14:28:51 EDT; 13min ago'


# Generated at 2022-06-13 06:29:04.524871
# Unit test for function main

# Generated at 2022-06-13 06:29:06.998417
# Unit test for function main
def test_main():
    result = dict(
        changed=False,
        status=dict(),
    )
    result['status'] = {'LoadState': '', 'ActiveState': '', 'LoadError': ''}
    module.exit_json(**result)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:29:17.201013
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    result = parse_systemctl_show(['LoadState=loaded', 'ActiveState=active', 'Description=Some service', 'ExecStart={\n  ls\n}', 'ExecReload={\n  kill -HUP $MAINPID\n}'])
    assert result == {'LoadState': 'loaded', 'ActiveState': 'active', 'Description': 'Some service', 'ExecStart': '{\n  ls\n}', 'ExecReload': '{\n  kill -HUP $MAINPID\n}'}
    result = parse_systemctl_show(['LoadState=loaded', 'ActiveState=active', 'Description={\n  Some service\n}', 'ExecStart={\n  ls\n}'])

# Generated at 2022-06-13 06:30:05.852353
# Unit test for function main
def test_main():
    with patch('ansible_collections.misc.not_a_real_collection.plugins.module_utils.basic.AnsibleModule') as mock_ansiblemodule:
        mock_module = MagicMock()
        mock_module.params = dict()
        mock_module.params['name'] = None
        mock_module.params['state'] = None
        mock_module.params['enabled'] = None
        mock_module.params['force'] = False
        mock_module.params['masked'] = None
        mock_module.params['daemon_reload'] = False
        mock_module.params['daemon_reexec'] = False
        mock_module.params['scope'] = 'system'
        mock_module.params['no_block'] = False
        
        mock_ansiblemodule.return_value = mock_module

# Generated at 2022-06-13 06:30:11.273131
# Unit test for function main
def test_main():
    module = AnsibleModule({
        'state': 'started',
        'name': 'dummy',
    })
    rc, out, err = module.run_command('systemctl show dummy', check_rc=True)
    assert rc == 0
    # When systemd is >= 239, any service can be shown with systemctl. But with older
    # versions of systemd, only existing services can be shown.
    assert "UnitFileState=invalid" not in out and "LoadState=not-found" not in out
#
# Autogenerated from test_runner.py, in the future we should run this
# directly with Nose2 as a unit test for this file.
#
# This example test always passes.

# import os
# import sys
# import unittest
#
# class TestExample(unittest.TestCase):
#
#

# Generated at 2022-06-13 06:30:20.899911
# Unit test for function main
def test_main():
    # Unit tests do not run with the 'systemctl' binary.
    # We can mock the module's state, and check the output of ansible

    # mock AnsibleModule class
    class AnsibleModuleMock(AnsibleModule):
        def get_bin_path(self, cmd, required=False):
            if 'systemctl' in cmd:
                return '/bin/systemctl'
            elif 'systemd-nspawn' in cmd:
                return '/usr/bin/systemd-nspawn'
            else:
                return super(AnsibleModuleMock, self).get_bin_path(cmd, required=required)

        def run_command(self, cmd, check_rc=None):
            if 'is-system-running' in cmd:
                return 0, 'running', ''

# Generated at 2022-06-13 06:30:27.113762
# Unit test for function main
def test_main():
  test_module = AnsibleModule(argument_spec={
      'name': {'type': 'str', 'required': 'True'},
      'state': {'type': 'str', 'required': 'True'},
      'enabled': {'type': 'bool'},
      'masked': {'type': 'bool'},
      'daemon_reload': {'type': 'bool'},
      'daemon_reexec': {'type': 'bool'},
      'scope': {'type': 'str'},
      'no_block': {'type': 'bool'},
  })

  test_main_function = main()
  test_is_enabled_function = is_enabled()
  test_is_masked_function = is_masked()
  test_is_system_running_function = is_system