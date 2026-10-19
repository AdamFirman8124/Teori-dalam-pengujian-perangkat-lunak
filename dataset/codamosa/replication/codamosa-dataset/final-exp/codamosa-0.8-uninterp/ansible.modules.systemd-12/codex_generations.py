

# Generated at 2022-06-13 06:21:18.903301
# Unit test for function main
def test_main():
    # Define a mock object that has get_bin_path() method
    class MockModule(object):
        def __init__(self):
            pass

        def get_bin_path(self, *args, **kwargs):
            return 'path/to/systemctl'

    # Define a function that set variables(module, found, unit) in main() with defined values
    def set_var(module, found, unit):
        module.params['name'] = unit
        module.params['state'] = 'running'
        module.params['enabled'] = True
        module.params['daemon_reload'] = False
        module.params['daemon_reexec'] = False
        module.params['force'] = False
        module.params['masked'] = False
        module.params['scope'] = 'system'

# Generated at 2022-06-13 06:21:27.697112
# Unit test for function main

# Generated at 2022-06-13 06:21:34.995406
# Unit test for function main
def test_main():
    unit = 'sshd'
    state = 'started'
    enabled = False
    masked = False
    daemon_reload = False
    daemon_reexec = False
    scope = 'system'
    no_block = False
    main(unit, state, enabled, masked, daemon_reload, daemon_reexec, scope, no_block)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:36.692566
# Unit test for function main
def test_main():
    request_sentence = 'main'
    assert request_sentence == 'main'


# Generated at 2022-06-13 06:21:45.745174
# Unit test for function main

# Generated at 2022-06-13 06:21:56.641715
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Test for single line values
    assert parse_systemctl_show([
        'ActiveState=active',
        'After=auditd.service systemd-user-sessions.service time-sync.target systemd-journald.socket basic.target system.slice',
        'AllowIsolate=no',
    ]) == {
        'ActiveState': 'active',
        'After': 'auditd.service systemd-user-sessions.service time-sync.target systemd-journald.socket basic.target system.slice',
        'AllowIsolate': 'no',
    }
    # Test for multi-line values

# Generated at 2022-06-13 06:22:04.075529
# Unit test for function main

# Generated at 2022-06-13 06:22:12.955614
# Unit test for function main
def test_main():
    from ansible.module_utils.systemd import AnsibleModule
    import json


# Generated at 2022-06-13 06:22:22.623251
# Unit test for function main
def test_main():
    fake_module = FauxModule()
    fake_module.params = {
      'name': [
        None,
        "datadog-agent"
      ],
      'state': [
        None,
        "reloaded"
      ],
      'enabled': [
        None,
        False
      ],
      'force': [
        None,
        False
      ],
      'masked': [
        None,
        False
      ],
      'daemon_reload': [
        None,
        False
      ],
      'daemon_reexec': [
        None,
        False
      ],
      'scope': [
        None,
        "system"
      ],
      'no_block': [
        None,
        False
      ]
    }
    fake_module.run_command = run

# Generated at 2022-06-13 06:22:32.994893
# Unit test for function main
def test_main():

    print(".test has been called")

    # Set up arguments
    module_args = dict()
    module_args['no_block'] = False
    module_args['scope'] = 'system'
    module_args['enabled'] = False
    module_args['daemon_reexec'] = False
    module_args['name'] = 'sshd.service'
    module_args['force'] = False
    module_args['state'] = 'started'
    module_args['masked'] = False
    module_args['daemon_reload'] = False

    # Set up data
    test_data = {
        'rc': 0,
        'stdout': '',
        'stderr': '',
    }

    # Set up test object

# Generated at 2022-06-13 06:22:55.645647
# Unit test for function main

# Generated at 2022-06-13 06:23:07.128150
# Unit test for function main
def test_main():
  from ansible.module_utils.basic import AnsibleModule, to_bytes
  from ansible.module_utils._text import to_native
  module = AnsibleModule(argument_spec={}, supports_check_mode=True)
  module.params = {
    "masked": False,
    "enabled": True,
    "name": "cron.service",
    "state": "stopped",
    "force": True
  }
  systemctl = module.get_bin_path('systemctl', True)
  rc, out, err = module.run_command("%s show '%s'" % (systemctl, module.params['name']))

# Generated at 2022-06-13 06:23:15.076740
# Unit test for function main

# Generated at 2022-06-13 06:23:18.537938
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('ignoring request')
    assert request_was_ignored('ignoring command')
    assert not request_was_ignored('blah=bar')
    assert not request_was_ignored('active (blah blah blah)')



# Generated at 2022-06-13 06:23:22.351019
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('ignoring request')
    assert request_was_ignored('ignoring command')
    assert request_was_ignored('= sign missing')
    assert not request_was_ignored('did something')



# Generated at 2022-06-13 06:23:25.297825
# Unit test for function main
def test_main():
    # If a unit name is specified, the module must enable or disable the unit
    assert main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:33.628311
# Unit test for function main
def test_main():
    # Test for success run
    sys.modules['ansible.module_utils.basic'] = MagicMock()
    sys.modules['ansible.module_utils.basic'].AnsibleModule.run_command = MagicMock(return_value=(0, '', ''))
    sys.modules['ansible.module_utils.systemd'] = MagicMock()
    sys.modules['ansible.module_utils.systemd'].is_chroot = MagicMock(return_value=False)
    sys.modules['ansible.module_utils.systemd'].is_initd = MagicMock(return_value=False)
    sys.modules['ansible.module_utils.systemd'].is_running_service = MagicMock(return_value=False)

# Generated at 2022-06-13 06:23:42.356992
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    assert parse_systemctl_show([]) == {}

# Generated at 2022-06-13 06:23:52.814800
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:23:59.133411
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:24:18.319832
# Unit test for function main
def test_main():
    '''
    Ansible unit test for function main
    '''
    # set args and set params
    args = dict(name="sshd", state="started")

    # set the module args
    set_module_args(args)
    # execute the module
    main()


# Generated at 2022-06-13 06:24:27.670514
# Unit test for function main
def test_main():
    test_result = dict(
        name='httpd',
        changed=False,
        status=dict(
            LoadState='loaded'
        ),
    )

    # Get a non-mocked list of units the real systemctl can access
    systemctl = module.get_bin_path('systemctl', True)
    (rc, out, err) = module.run_command("%s list-unit-files '*'" % systemctl)
    assert rc == 0
    unit_list = out.splitlines()

    # All of the following tests should not do any real systemctl calls, so we patch
    # run_command (which gets called through module.run_command) to make sure the
    # real systemctl command is not executed.

# Generated at 2022-06-13 06:24:39.036614
# Unit test for function main

# Generated at 2022-06-13 06:24:45.848225
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_systemd as systemd
    ans_module = AnsibleModule(argument_spec=systemd.ARGUMENT_SPEC,
                               supports_check_mode=True)
    ans_module.params['enabled'] = True
    systemd.main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:57.469565
# Unit test for function main
def test_main():
    test_systemctl = 'fake_systemctl'
    test_rc = 0
    test_out = 'State=running'
    test_err = ''
    # This creates a unit test configuration known as a moke that
    # is used as a test double when running the unit tests
    class TestModule(object):
        def __init__(self):
            self.params = {
                'name': 'foo',
                'enabled': False,
                'state': 'stopped',
                'masked': False,
                'force': False
            }
            self.check_mode = False
            self.exit_json = lambda result: result
            self.fail_json = lambda msg: msg
        def run_command(self, command, check_rc=False):
            return (test_rc, test_out, test_err)
       

# Generated at 2022-06-13 06:25:08.943900
# Unit test for function main
def test_main():
  import os
  import shutil
  from tempfile import mkdtemp
  from ansible.utils.path import makedirs_safe
  from ansible.utils.path import unfrackpath
  from ansible.utils.display import Display
  display = Display()

  def setUp():
    global fixture_path 
    global fixture_data
    global fixture_unit
    global fixture_path_systemd
    global fixture_path_initd
    global fixture_path_rcd
    global fixture_path_d
    global fixture_unit_multiple_prefix

    fixture_path = mkdtemp()
    fixture_path_systemd = "%s/systemd" % fixture_path
    fixture_path_initd = "%s/init.d" % fixture_path

# Generated at 2022-06-13 06:25:20.500790
# Unit test for function main

# Generated at 2022-06-13 06:25:30.796302
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:25:36.646741
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Test monoline value
    expected = dict(foo='bar', baz='quux')
    actual = parse_systemctl_show('foo=bar\nbaz=quux'.splitlines())
    assert (actual == expected)
    # Test multi-line value
    expected = dict(foo='{ bar\n  baz\n}')
    actual = parse_systemctl_show('foo={ bar\n  baz\n}'.splitlines())
    assert (actual == expected)



# Generated at 2022-06-13 06:25:44.194897
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:26:35.124300
# Unit test for function main
def test_main():
    from ansible.module_utils.systemd import sysv_exists
    from ansible.module_utils.systemd import sysv_is_enabled


# Generated at 2022-06-13 06:26:47.861511
# Unit test for function main
def test_main():
    """
    Unit test for main function
    """
    import sys
    import __builtin__
    if sys.version_info[0] >= 3:
        import builtins
        __builtin__ = builtins
    else:
        __builtin__ = __builtin__

    current_args = __builtin__.__dict__.get('ARGS', None)
    if current_args is None:
        __builtin__.ARGS = {}
    else:
        __builtin__.ARGS = {}
        for k, v in current_args.iteritems():
            __builtin__.ARGS[k] = v

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import load_platform_subclass
    from ansible.module_utils.basic import get_platform

# Generated at 2022-06-13 06:26:56.685744
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    assert parse_systemctl_show([
        'Description=Command Scheduler',
        'Documentation=man:crond(8) man:crontab(5)',
        'LoadState=loaded',
        'ActiveState=active',
        'SubState=running',
        'UnitFileState=enabled',
    ]) == {
        'Description': 'Command Scheduler',
        'Documentation': 'man:crond(8) man:crontab(5)',
        'LoadState': 'loaded',
        'ActiveState': 'active',
        'SubState': 'running',
        'UnitFileState': 'enabled',
    }

# Generated at 2022-06-13 06:27:01.467092
# Unit test for function main
def test_main():
    argv = sys.argv
    sys.argv = [sys.argv[0], "name=test.service", "state=started", "no_block=True", "daemon_reload=True"]
    main()
    sys.argv = argv


# Generated at 2022-06-13 06:27:11.644239
# Unit test for function main

# Generated at 2022-06-13 06:27:19.926578
# Unit test for function main
def test_main():

    # mocks the actual ansible module with a dummy object
    class AnsibleModule:
        def __init__(self, arg_spec, required_one_of, required_by, supports_check_mode, check_invalid_arguments=False, mutually_exclusive=None, required_together=None, required_if=None, bypass_checks=False, no_log=False, deprecated_args=None, add_file_common_args=True, supports_diff=False, supports_flush=False, required_together_if_one_or_more_present=None, argument_spec_ext=None, min_supported_json=None, local_tmp=None, fail_json_on_init_errors=True,):
            self.params = dict()
            self.check_mode = False
            self.exit_json = lambda **kwargs: None

# Generated at 2022-06-13 06:27:32.561124
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    raw = """
Key1=Val1
Key2=Val2
K3=Val 3
Key4 = Val 4
Key5 = {
Val5
Val6
Val7
}
ExecStart = {
command1
command2
command3
}
Key6=Val6
ExecStartPost = {
postcommand1
postcommand2
}
Key7 = {
Val7
}
ExecStartPost = {
postcommand3
}
"""

# Generated at 2022-06-13 06:27:41.516737
# Unit test for function main
def test_main():
    """
      Run unit test for function main
    """
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 06:27:55.161948
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    simple_service = '''
ActiveState=inactive
After=systemd-networkd.service network-online.target
Alias=systemd-networkd.service
Before=runlevel3.target shutdown.target
ConditionPathExists=/etc/systemd/network
Description=Network Service
##
'''.split('\n')
    parsed_simple_service = parse_systemctl_show(simple_service)
    assert parsed_simple_service == {'ActiveState': 'inactive',
                                     'After': 'systemd-networkd.service network-online.target',
                                     'Alias': 'systemd-networkd.service',
                                     'Before': 'runlevel3.target shutdown.target',
                                     'ConditionPathExists': '/etc/systemd/network',
                                     'Description': 'Network Service'}

    multi_line_service

# Generated at 2022-06-13 06:28:08.364116
# Unit test for function main

# Generated at 2022-06-13 06:28:59.366096
# Unit test for function main
def test_main():
    # run with no required args and expect to be told what is missing
    args = dict(
        state=None,
        enabled=None,
        masked=None,
        daemon_reload=False,
        daemon_reexec=False
    )

# Generated at 2022-06-13 06:29:06.093693
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    lines = ['Description=Something that spans \n',
             '  multiple \n',
             '    lines']
    expected = {'Description': 'Something that spans multiple lines'}
    result = parse_systemctl_show(lines)
    assert result == expected
    lines = ['ExecStart=forking { path=/sbin/service ; argv[]=/sbin/service httpd start ; ignore_errors=no ; start_time=[Thu 2018-03-15 12:45:14 EST] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }']

# Generated at 2022-06-13 06:29:15.861366
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    lines = parse_systemctl_show([
        'Id=crond.service',
        'Description=Command Scheduler',
        'ExecStart={ path=/usr/sbin/crond ; argv[]=/usr/sbin/crond -n $CRONDARGS ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }',
    ])
    assert lines['Id'] == 'crond.service'
    assert lines['Description'] == 'Command Scheduler'

# Generated at 2022-06-13 06:29:23.361752
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:29:32.447104
# Unit test for function main

# Generated at 2022-06-13 06:29:33.579666
# Unit test for function main
def test_main():
    exit_code = main()
    assert exit_code == 0


# Generated at 2022-06-13 06:29:39.875868
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:29:48.978987
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:29:55.502542
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:30:03.460743
# Unit test for function main
def test_main():
    # Test loading of show results
    assert parse_systemctl_show(['LoadState=loaded']) == {'LoadState': 'loaded'}
    assert parse_systemctl_show(['LoadState=not-found']) == {'LoadState': 'not-found'}
    assert parse_systemctl_show(['Description={'] + ['  This is a test'] + ['}']) == {'Description': 'This is a test'}
    assert parse_systemctl_show(['Description={'] + ['  This is a test'] + ['}', 'LoadState=loaded']) == {'Description': 'This is a test', 'LoadState': 'loaded'}