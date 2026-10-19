

# Generated at 2022-06-13 06:20:57.238689
# Unit test for function main
def test_main():
    assert True

# Generated at 2022-06-13 06:21:04.265729
# Unit test for function main
def test_main():
    unit = 'test_service'
    systemctl = 'test_path'
    rc = 0
    out = err = ''
    result = dict(name = unit,
                  changed = False,
                  status = dict()
                 )

    def run_command(cmd, check_rc=False):
        assert cmd == "%s show '%s'" % (systemctl, unit)
        return (rc, out, err)

    def exit_json(**kwargs):
        assert kwargs == dict(name = unit,
                              changed = False,
                              status = dict()
                             )

    def fail_json(msg, **kwargs):
        print(msg)
        assert kwargs == dict()

    def get_bin_path(name, required):
        assert name == 'systemctl'
        assert required


# Generated at 2022-06-13 06:21:15.645754
# Unit test for function main

# Generated at 2022-06-13 06:21:27.370698
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:39.141202
# Unit test for function main
def test_main():
    the_argument_spec = dict(
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

# Generated at 2022-06-13 06:21:50.538054
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:57.298810
# Unit test for function main
def test_main():
    print('==========running test_main==========')

    class Argv:
        def __init__(self, argv):
            self.argv = argv
            self.called = 0

        def __call__(self, *args, **kwargs):
            ret = self.argv[self.called]
            self.called += 1
            return ret

    # begin test
    argv = ['ansible-test', 'test', '--force']
    argv_orig = sys.argv
    sys.argv = Argv(argv)
    cmd = AnsibleModule(argument_spec={}, supports_check_mode=True)
    module = cmd
    unit = 'apache2'
    systemctl = module.get_bin_path('systemctl', True)


# Generated at 2022-06-13 06:22:09.276885
# Unit test for function main
def test_main():
    test_args = {
        'name': 'myunit',
        'enabled': True,
        'state': 'started',
        'scope': 'system',
        'masked': True,
        'no_block': True,
    }
    test_rc = None
    test_stdout = None
    test_stderr = None

# Generated at 2022-06-13 06:22:21.001466
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.modules.system.systemd import main



# Generated at 2022-06-13 06:22:24.421664
# Unit test for function main
def test_main():
    with pytest.raises(AnsibleExitJson) as excinfo:
        main()
    assert excinfo.value.args[0]['changed']
test_main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:40.632635
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('ignoring request')
    assert not request_was_ignored('=')
    assert not request_was_ignored('foo')



# Generated at 2022-06-13 06:22:46.559534
# Unit test for function main
def test_main():
    out = mock.MagicMock(return_value='foo')
    rc = mock.MagicMock()
    err = mock.MagicMock()
    module = mock.MagicMock()
    module.get_bin_path = mock.MagicMock(return_value='1')
    module.run_command = mock.MagicMock(return_value=(rc, out, err))
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:55.676977
# Unit test for function main

# Generated at 2022-06-13 06:23:07.208981
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule # noqa: F401

# Generated at 2022-06-13 06:23:10.001102
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('Ignoring command.')
    assert not request_was_ignored('= stdout =')
    assert not request_was_ignored('[ OK ]')



# Generated at 2022-06-13 06:23:18.589368
# Unit test for function main

# Generated at 2022-06-13 06:23:29.000359
# Unit test for function main
def test_main():
    spec = dict(
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


# Generated at 2022-06-13 06:23:40.084156
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    assert parse_systemctl_show(['Id=crond.service', 'LoadState=loaded', 'ActiveState=active']) == {
        'Id': 'crond.service',
        'LoadState': 'loaded',
        'ActiveState': 'active'
    }

    assert parse_systemctl_show([
        'ExecStart={',
        '  path=/usr/sbin/crond',
        '  argv[]=/usr/sbin/crond -n $CRONDARGS',
        '  ignore_errors=no',
        '  start_time=[n/a]',
        '  stop_time=[n/a]',
        '  pid=0',
        '  code=(null)',
        '  status=0/0',
        '}',
        'Id=crond.service'
    ])

# Generated at 2022-06-13 06:23:43.017688
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:48.880086
# Unit test for function main
def test_main():
    from ansible.modules.system.systemd import main
    from ansible.module_utils.basic import AnsibleModule

    # basic
    module = AnsibleModule(argument_spec={'name': {'type': 'str'}, 'state': {'type': 'str'}})
    module.params = {'name': 'test', 'state': 'started'}
    result = main()
    assert result == "ok"

# Generated at 2022-06-13 06:24:13.304182
# Unit test for function main
def test_main():
    test_argv = ['']
    test_args = dict(
        state='started',
        name='httpd',
        force=True,
        daemon_reexec=True,
        daemon_reload=True,
        masked=False,
        enabled=True,
        scope='user'
    )
    unit = test_args['name']
    test_unit = '"%s"' % unit
    main()
    print('%s: %s' % (unit, test_args['state']))
    systemctl = module.get_bin_path('systemctl', True)
    (rc, out, err) = module.run_command("%s is-active '%s'" % (systemctl, unit))
    if out.strip() == 'active':
        result['state'] = 'started'

# Generated at 2022-06-13 06:24:22.744591
# Unit test for function main
def test_main():
    from .mock import patch, Mock
    from .mock import call

    module = Mock()

# Generated at 2022-06-13 06:24:34.750798
# Unit test for function main

# Generated at 2022-06-13 06:24:43.247360
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # parse_systemctl_show should return a dictionary
    assert isinstance(parse_systemctl_show([]), dict)

    # parse_systemctl_show should raise an exception on malformed input
    # (the input to the function is a list of lines returned by systemctl show)
    # (the exception will be caught and will be exposed as a fatal)
    assert_raises(AssertionError, lambda x: parse_systemctl_show(x), ['k1=v1', 'k2'])
    assert_raises(AssertionError, lambda x: parse_systemctl_show(x), ['k1'])
    assert_raises(AssertionError, lambda x: parse_systemctl_show(x), ['k1=multiline', 'v1', 'continues'])

    # parse_systemctl_show should

# Generated at 2022-06-13 06:24:55.587305
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.systemd import state_exists, is_chroot, is_running_service, request_was_ignored

    os.environ['XDG_RUNTIME_DIR'] = 'XDG_RUNTIME_DIR'

# Generated at 2022-06-13 06:25:06.983439
# Unit test for function main

# Generated at 2022-06-13 06:25:14.334645
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes


# Generated at 2022-06-13 06:25:23.674084
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModuleMock

    main_mock = Mock(return_value=dict(changed=False, status=dict(), name='unit'))
    service_info_mock = Mock(return_value=dict(
        name='unit',
        status=dict(),
        enabled=True,
        state='stopped',
    ))
    os_mock = Mock()
    os_mock.path.exists.return_value = False
    os_mock.path.islink.return_value = False
    os_mock.path.isdir.return_value = False


# Generated at 2022-06-13 06:25:33.683685
# Unit test for function main
def test_main():
    module = ansible_module_get()
    module.params = {
        'daemon_reload': False,
        'daemon_reexec': False,
        'enabled': False,
        'force': False,
        'masked': None,
        'name': 'openssh-server',
        'no_block': False,
        'scope': 'system',
        'state': None,
    }
    assert module.get_bin_path('systemctl', required=True) is not None
    systemctl = module.get_bin_path('systemctl', required=True)
    (rc, out, err) = module.run_command("%s show '%s'" % (systemctl, module.params['name']))
    assert rc == 0
    assert systemctl in out

# Generated at 2022-06-13 06:25:38.191894
# Unit test for function main
def test_main():
    # If the target is a chroot or systemd is offline, this can lead to false positives or prevent the init system tools from working.
    with mock.patch('ansible_collections.misc.not_a_real_collection.plugins.module_utils.basic.AnsibleModule.run_command', side_effect=Exception):
        module = get_module(dict(name="mocked", state='stopped', daemon_reload=False, daemon_reexec=False, enabled=True, masked=None, scope="system"))
        module.run_command = MagicMock()
        main()
        module.warn.assert_called_once_with('Target is a chroot or systemd is offline. This can lead to false positives or prevent the init system tools from working.')

    # When correct parameters are set

# Generated at 2022-06-13 06:26:30.598526
# Unit test for function main
def test_main():
    # Create a mock object of the module so that we have the necessary variables
    # to test the main function.
    args = dict()
    args['name'] = 'zabbix-agent'
    args['state'] = 'stopped'
    args['enabled'] = True
    args['masked'] = False
    args['daemon_reload'] = False
    args['daemon_reexec'] = False
    args['scope'] = 'system'
    args['no_block'] = False
    module = AnsibleModule(argument_spec=args)
    
    # Set test directory 
    test_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'unit-tests')

    # proper setup is required to run the unit tests
    # init scripts must be copied to init

# Generated at 2022-06-13 06:26:42.359751
# Unit test for function main

# Generated at 2022-06-13 06:26:44.925234
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:26:54.584064
# Unit test for function main
def test_main():
    unit = "sshd"
    rc = 1
    out = " "
    err = "test"
    found = None
    masked = None

    # define arguments

# Generated at 2022-06-13 06:27:05.614412
# Unit test for function main
def test_main():
  args = dict(
    name=None,
    state=None,
    enabled=None,
    force=False,
    masked=False,
    daemon_reload=False,
    daemon_reexec=False,
    scope='system',
    no_block=False,
  )

# Generated at 2022-06-13 06:27:15.607735
# Unit test for function main
def test_main():
    # Prepare the mock environment
    test_params = {
        'name': 'test_name',
        'state': 'test_state',
        'enabled': True,
        'force': True,
        'masked': True,
        'daemon_reload': True,
        'daemon_reexec': True,
        'scope': 'system',
        'no_block': False,
    }
    test_bin_path = '/usr/bin'
    test_output = {
        'name': 'test_name',
        'changed': False,
        'status': dict(),
    }

# Generated at 2022-06-13 06:27:22.483364
# Unit test for function main

# Generated at 2022-06-13 06:27:28.480495
# Unit test for function main
def test_main():
    '''systemd_service main'''

# Generated at 2022-06-13 06:27:29.843006
# Unit test for function main
def test_main():
    import ansible.module_utils.basic
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:37.825994
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils._text import to_text
    # The argument spec will be used to configure the mock.  We want all
    # the parameters here

# Generated at 2022-06-13 06:28:40.516383
# Unit test for function main

# Generated at 2022-06-13 06:28:51.413378
# Unit test for function main
def test_main():
    def run_main(mock_module, unit, state, enabled=None, force=False, masked=None, daemon_reload=False, daemon_reexec=False, scope="system", no_block=False):
        # The old version of this code used monkeypatch to mock multiple functions at the same time,
        # but it was replaced with the mocks below to make the testing code clearer. For more details
        # about why the old version was replaced, see
        # https://docs.pytest.org/en/latest/deprecations.html#monkeypatch-setattr-to-mock-functions
        m = mock.Mock()

# Generated at 2022-06-13 06:28:52.649651
# Unit test for function main
def test_main():
    assert isinstance(main(), dict), "It should return a dict"



# Generated at 2022-06-13 06:29:01.200754
# Unit test for function main

# Generated at 2022-06-13 06:29:08.089547
# Unit test for function main
def test_main():
    # import and define module arguments
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', aliases=['service', 'unit'], default='sshd'),
            state=dict(type='str', choices=['reloaded', 'restarted', 'started', 'stopped']),
            enabled=dict(type='bool'),
            force=dict(type='bool'),
            masked=dict(type='bool'),
            daemon_reload=dict(type='bool', default=False, aliases=['daemon-reload']),
            no_block=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled', 'masked', 'daemon_reload']],
    )


# Generated at 2022-06-13 06:29:18.703450
# Unit test for function main
def test_main():
    args = dict(
        name='memcached',
        state='started',
    )


# Generated at 2022-06-13 06:29:23.095078
# Unit test for function main
def test_main():
    #
    # Unit tests for main
    #
    try:
        response = main()
    except Exception as e:
        raise

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:29:32.350605
# Unit test for function main
def test_main():
    args = dict(
        name='foo',
        state='stopped',
        daemon_reload=False,
        daemon_reexec=False,
        scope='system',
        no_block=False,
    )


# Generated at 2022-06-13 06:29:33.954767
# Unit test for function main
def test_main():
    pass

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:29:40.152895
# Unit test for function main
def test_main():
    import os
    import sys
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.pycompat24 import get_exception
    import sys
    sys.path.append("../library/")
    sys.stdout = open("/tmp/ansible_systemd_test", "w")
    sys.stderr = open("/tmp/ansible_systemd_error", "w")

    my_env = os.environ.copy()

    my_env['MOLECULE_INVENTORY_FILE']='/tmp/ansible_systemd_error'