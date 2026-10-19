

# Generated at 2022-06-13 06:20:39.940439
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:20:44.883976
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.pycompat24 import get_exception
    from ansible.module_utils.pycompat24 import mock
    import collections

    # Replace function get_bin_path with a mock. This mock simply returns the string 'systemctl'
    # regardless of the arguments.
    module = collections.namedtuple('AnsibleModule', ['get_bin_path'])(
        get_bin_path=mock.Mock(return_value='systemctl')
    )
    module.run_command = mock.Mock(return_value=(0, '', ''))

    module.get_bin_path.assert_not_called()
    module.run_command.assert_not_called()

# Generated at 2022-06-13 06:20:51.611755
# Unit test for function main
def test_main():
    # Simply call main()
    main()


if __name__ == '__main__':
    # Set to False if you don't want to run unit tests
    test = True

    if test:
        import doctest
        # Running tests
        # Run tests in docstrings
        doctest.testmod()
        # Run tests on unit_service.py
        # Python 3.x need to convert to str
        doctest.run_docstring_examples(unit_service, globals(), verbose=False)
    # Calling main()
    main()

# Generated at 2022-06-13 06:20:53.655503
# Unit test for function main
def test_main():
    from ansible.module_utils.common.removed import removed_module
    removed_module(removed_in="2.11")

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:03.376502
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Input description is similar to one below
    # Description={ path=/usr/lib/systemd/systemd-journald ; argv[]=/usr/lib/systemd/systemd-journald ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }
    lines = [
        "Description={ path=/usr/lib/systemd/systemd-journald ; argv[]=/usr/lib/systemd/systemd-journald ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }\n"
    ]
    parsed = parse_systemctl_show(lines)
    assert('Description' in parsed)


# Generated at 2022-06-13 06:21:15.008571
# Unit test for function main

# Generated at 2022-06-13 06:21:26.711065
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    test = parse_systemctl_show

# Generated at 2022-06-13 06:21:28.410610
# Unit test for function main
def test_main():
    assert True
# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:34.293717
# Unit test for function main
def test_main():
    # mock_module - initialize
    def fail_json(*args, **kwargs):
        this.exit_args = args
        this.exit_kwargs = kwargs
        this.fail_json_called = True
        return False

    _mock_module = MagicMock(exit_args=None, exit_kwargs=None, fail_json_called=False)
    _mock_module.fail_json = MagicMock(side_effect=fail_json)

    def get_bin_path(*args, **kwargs):
        return 'systemctl'

    _mock_module.get_bin_path = MagicMock(side_effect=get_bin_path)
    _mock_module.run_command = MagicMock(return_value=(0, 'output', 'error'))

    # run main()


# Generated at 2022-06-13 06:21:46.008055
# Unit test for function main
def test_main():
    """ Unit test using mock for service file to print to stdout """
    # Set up mock environment

# Generated at 2022-06-13 06:22:10.145923
# Unit test for function main

# Generated at 2022-06-13 06:22:21.555413
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    """
    Test function parse_systemctl_show
    """

# Generated at 2022-06-13 06:22:32.209168
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # AC-8981: test case for Description= key whose value starts with { but does not end with }
    lines = ['ActiveState=active',
             'Description={',
             '  This is a test',
             '  ExecStart={',
             '    This is an ExecStart value but it does not end with }',
             '  ExecStartPost={',
             '    This is an ExecStartPost value',
             '  }',
             '}',
             'ExecMainStatus=0',
             'ExecMainStartTimestampMonotonic=99',
             'ExecMainPID=111',
             'ExecMainExitTimestampMonotonic=0',
             'ExecMainCode=0']

# Generated at 2022-06-13 06:22:44.455594
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Test with multiline value
    lines = ["UnitFileState=enabled",
             "ExecReload={ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }"]
    assert parse_systemctl_show(lines) == {'UnitFileState': 'enabled', 'ExecReload': '{ path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }'}
    # Test with single line value

# Generated at 2022-06-13 06:22:54.012448
# Unit test for function main
def test_main():
    '''
    Make sure all of the expected functions and parameters are available.
        Also test function return values.

    Each test is a function named 'test_[item_under_test]'.
        - The 'item_under_test' is the function to test.
        - 'assert' statements compare expected results with the actual results.
        - 'assert' statements are caught by the test harness and considered failures.
        - 'assert' statements can be used in any test.
    '''
    print('Test main')
    # Initialization

# Generated at 2022-06-13 06:22:59.925322
# Unit test for function main

# Generated at 2022-06-13 06:23:05.250154
# Unit test for function main
def test_main():
    # Test as root user
    os.seteuid(0)
    assert os.geteuid() == 0
    # Test as non-root user
    # os.seteuid(1000)
    # assert os.geteuid() == 1000

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:09.147523
# Unit test for function main
def test_main():
    print("Testing function: main")

    # simple test to check is_initd
    assert is_initd("testservice") == True

    # Test get_systemctl_binary
    assert get_systemctl_binary("systemctl") == "systemctl"
    assert get_systemctl_binary("systemd") == "systemctl"


# Generated at 2022-06-13 06:23:10.253066
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:19.819172
# Unit test for function main
def test_main():
    import json

    # Ansible exit_json and fail_json transforms work with python2 and python3
    class AnsibleExitJson(Exception):
        pass

    class AnsibleFailJson(Exception):
        pass

    def exit_json(*args, **kwargs):
        raise AnsibleExitJson(kwargs)

    def fail_json(*args, **kwargs):
        raise AnsibleFailJson(kwargs)

    def fail_if_missing(module, found, unit, msg='service'):
        pass

    def is_running_service(status):
        return False

    def is_deactivating_service(status):
        return False

    def sysv_exists(unit):
        return False

    def sysv_is_enabled(unit):
        return False

    def to_native(vl):
        return

# Generated at 2022-06-13 06:23:48.148852
# Unit test for function main
def test_main():

    from test.unit.modules.utils import set_module_args
    from ansible.modules.system.systemd import main
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 06:23:50.886253
# Unit test for function request_was_ignored
def test_request_was_ignored():
    out = "ignoring command"
    assert request_was_ignored(out)
    out = "= some other string"
    assert not request_was_ignored(out)



# Generated at 2022-06-13 06:23:58.352840
# Unit test for function main
def test_main():
    if os.environ.get('ANSIBLE_SYS_VINIT') == 'True':
        # Set environment for Ansible testing
        os.environ['XDG_RUNTIME_DIR'] = '/run/user/%s' % os.geteuid()

        import tempfile
        from ansible.module_utils.systemd import sysv_exists, sysv_is_enabled, sysv_update_rc

        # Test sysv_exists
        fd, script_path = tempfile.mkstemp()
        with os.fdopen(fd, 'w') as script:
            script.write('#!/bin/sh\necho hello world\n')

# Generated at 2022-06-13 06:24:08.677014
# Unit test for function main
def test_main():
    test_sysv_exists_file = open('test_sysv_exists_file.py', 'w+')
    try:
        import os
        import sys
        test_sysv_exists_file.write('#!/usr/bin/python\ntest_sysv_exists_file')
        os.chmod('test_sysv_exists_file.py', 0o755)
        sys.path.append(os.getcwd())
        from test_sysv_exists_file import main
        main()
    finally:
        os.remove('test_sysv_exists_file.py')


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:18.707181
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    test_output = '''
ActiveEnterTimestamp=Sun 2016-05-15 18:28:49 EDT
ActiveEnterTimestampMonotonic=8135942
'''
    result = parse_systemctl_show(test_output.split('\n'))
    assert result['ActiveEnterTimestamp'] == 'Sun 2016-05-15 18:28:49 EDT'

    test_output = '''
ActiveEnterTimestamp=Sun 2016-05-15 18:28:49 EDT
ActiveEnterTimestampMonotonic=8135942
Description=Description
'''
    result = parse_systemctl_show(test_output.split('\n'))
    assert result['Description'] == 'Description'


# Generated at 2022-06-13 06:24:26.237898
# Unit test for function main

# Generated at 2022-06-13 06:24:37.760603
# Unit test for function main
def test_main():
    monkeypatch.setattr(ansible.plugins.module_utils.systemd.AnsibleModule, 'run_command', mock_run_command)
    monkeypatch.setattr(ansible.plugins.module_utils.systemd.AnsibleModule, 'get_bin_path', mock_get_bin_path)
    result = dict(
        ansible_facts={},
        changed=False,
        status={},
    )

# Generated at 2022-06-13 06:24:50.004880
# Unit test for function main

# Generated at 2022-06-13 06:25:00.467211
# Unit test for function main
def test_main():
    """
    Function to do some unit testing for function main.
    """
    params = {
        'name': 'test',
        'state': 'reloaded',
        'enabled': True,
        'force': True,
        'masked': True,
        'daemon_reload': False,
        'daemon_reexec': False,
        'scope': 'system',
        'no_block': False
    }


# Generated at 2022-06-13 06:25:03.641458
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored(' = "test"') is False
    assert request_was_ignored(' ignoring request') is True
    assert request_was_ignored(' ignoring command') is True



# Generated at 2022-06-13 06:25:41.405848
# Unit test for function main
def test_main():
    import json
    import tempfile
    tmp_dir = tempfile.mkdtemp()
    os.environ["XDG_RUNTIME_DIR"] = tmp_dir
    os.makedirs(os.path.join(tmp_dir, 'dbus-1'))
    os.makedirs(os.path.join(tmp_dir, 'systemd'))
    os.system('touch {0}/dbus-1/system-bus-socket'.format(tmp_dir))
    os.system('touch {0}/systemd/private'.format(tmp_dir))
    os.system('touch {0}/systemd/sessions'.format(tmp_dir))


# Generated at 2022-06-13 06:25:43.075263
# Unit test for function main
def test_main():
    assert True

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:44.293667
# Unit test for function main
def test_main():
    assert True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:54.618091
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(type='str', required=True),
            state = dict(type='str', required=True),
        ),
        supports_check_mode=True,
        required_by=dict(
            name=('state', ),
        ),
    )
    unit = module.params['name']
    state = module.params['state']
    systemctl = module.get_bin_path('systemctl', True)

    if os.getenv('XDG_RUNTIME_DIR') is None:
        os.environ['XDG_RUNTIME_DIR'] = '/run/user/%s' % os.geteuid()

    rc = 0
    out = err = ''

# Generated at 2022-06-13 06:25:58.823041
# Unit test for function main
def test_main():
    # test with missing argument
    args = dict(
        daemon_reload=False,
    )
    result = dict(
        failed=True,
        msg='One of the following is required: name, state, enabled, masked, daemon_reload, daemon_reexec'
    )
    with pytest.raises(AnsibleExitJson):
        main(module_args=args)


# Generated at 2022-06-13 06:26:05.063045
# Unit test for function main
def test_main():
    test_data = (
        (True, 0, '', '', {
            "name": None,
            "changed": False,
            "status": '',
        }),
    )

# Generated at 2022-06-13 06:26:10.458051
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:26:11.359038
# Unit test for function main
def test_main():
    result = main()


# Generated at 2022-06-13 06:26:17.235735
# Unit test for function main
def test_main():
    from ansible.module_utils._text import to_bytes
    result = dict(
        name='sshd',
        changed=False,
        status=dict(),
    )

# Generated at 2022-06-13 06:26:22.349580
# Unit test for function main
def test_main():
    for version in ['v229', 'v239']:
        print("Test for systemd version %s" % version)
        unit_file_name = "test_systemd_1.service"
        unit_file_path = os.path.join(TEST_DIR, "systemd", version, "system", unit_file_name)
        print('    Creating file %s' % unit_file_path)
        with open(unit_file_path, 'w') as unit_file:
            unit_file.write("""[Unit]
Description=A test service

[Service]
Type=oneshot
ExecStart=/bin/true

[Install]
WantedBy=multi-user.target
""")


# Generated at 2022-06-13 06:27:10.100384
# Unit test for function main
def test_main():
    from ansible.modules.system.systemd import main
    from ansible.module_utils.basic import AnsibleModule
    import sys
    import os

    test_dir = os.path.dirname(os.path.realpath(__file__))
    sys.path.insert(0, os.path.dirname(test_dir))

    class Args():
        name = None
        state = None
        enabled = None
        masked = None
        daemon_reload = None
        daemon_reexec = None
        scope = None
        no_block = None

    args = Args()

    # test without any service param
    try:
        main()
    except SystemExit as e:
        assert e.code==1

    # test with service param
    args.name = "foo.service"
    # run with no

# Generated at 2022-06-13 06:27:19.874397
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import get_exception
    from ansible.module_utils.systemd import main

    # create the mocks
    mock_module = MagicMock()
    mock_module.params = {
        'enabled': True,
        'name': 'foobar',
        'masked': False,
        'scope': 'system',
    }

    # create a dummy main() function
    # NOTE: We cannot call 'main()' directly, since it's an AnsibleModule object which requires 'run_command' to
    #       be mocked.
    def dummy_main(module):
        # The linter complains about using 'global' inside a function, but we have no other option since we need to
        # reassign the value of systemctl here.
        global systemctl
        systemctl = module.get_bin_

# Generated at 2022-06-13 06:27:23.563942
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    from ansible.module_utils.basic import AnsibleModule
    main()

# Generated at 2022-06-13 06:27:34.663962
# Unit test for function main
def test_main():
    """
    Test function main
    """
    # Fixtures
    fixture_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures/')
    fixture_systemctl_show = read_file(fixture_path + 'systemctl_show.out')
    fixture_systemctl_show_2 = read_file(fixture_path + 'systemctl_show_2.out')
    fixture_systemctl_show_multi_line = read_file(fixture_path + 'systemctl_show_multi_line.out')

    # Initialize systemctl module

# Generated at 2022-06-13 06:27:42.652712
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 06:27:55.450413
# Unit test for function main
def test_main():
    import sys

    class AnsibleModuleMock(object):
        def __init__(self):
            self.params = dict()
            self.result = dict()

        def fail_json(self, **kwargs):
            raise Exception(kwargs['msg'])

        def exit_json(self, **kwargs):
            self.result = kwargs

        def get_bin_path(self, executable, required):
            return 'systemctl'

        def run_command(self, command, check_rc=False):
            return(0, '', '')

    class AnsibleModuleTest(AnsibleModuleMock):
        def __init__(self):
            # Avoid calling the real AnsibleModule constructor
            super(AnsibleModuleTest, self).__init__()

# Generated at 2022-06-13 06:27:57.498875
# Unit test for function main
def test_main():
    assert True


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:58.129508
# Unit test for function main
def test_main():
    pass


# Generated at 2022-06-13 06:28:11.004977
# Unit test for function main

# Generated at 2022-06-13 06:28:22.526581
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule


# Generated at 2022-06-13 06:29:43.335449
# Unit test for function main
def test_main():
    # Test parameters needed by AnsibleModule.
    module_args = {}


# Generated at 2022-06-13 06:29:53.094948
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:29:58.779051
# Unit test for function main
def test_main():
    # Importing module for side effects
    import ansible.modules.system.systemd
    # Populating params
    params = dict(
        name="Unit name",
        state=None,
        enabled=None,
        force=None,
        masked=None,
        daemon_reload=None,
        daemon_reexec=None,
        scope=None,
    )
    ansible.modules.system.systemd.main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:30:05.666716
# Unit test for function main
def test_main():
    test_cases = [{'name': 'dummy','params': {'name': 'dummy', 'state':'started'}},
                  {'name': 'dummy1','params': {'name': 'dummy1', 'state':'stopped'}}]
    for test_case in test_cases:
        unit_params = {'name': test_case['name'], 'state': test_case['state']}
        unit = AnsibleModule(unit_params)
        rc = 0
        out = err = ''
        result = dict(
            name=unit,
            changed=False,
            status=dict(),
        )

        # Run daemon-reload first, if requested

# Generated at 2022-06-13 06:30:11.112002
# Unit test for function main
def test_main():
    # init
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str'),
            enabled=dict(type='bool'),
            masked=dict(type='bool'),
            daemon_reload=dict(type='bool'),
        ),
    )
    module.run_command = MagicMock()
    module.fail_json = MagicMock()
    module.warn = MagicMock()
    global systemctl
    systemctl = MagicMock()
    global is_initd
    is_initd = True
    
    # check with missing input
    try:
        main()
    except SystemExit:
        pass
    # check with input name=True

# Generated at 2022-06-13 06:30:20.667057
# Unit test for function main
def test_main():
    from ansible.module_utils.systemd import ACTION_STATES
    from ansible.module_utils.systemd import parse_systemctl_show
    from ansible.module_utils.systemd import SERVICE_STATES


# Generated at 2022-06-13 06:30:26.950046
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={})
    service = {
        "name": "test_service",
        "state": "started",
        "enabled": True,
        "masked": False,
        "daemon_reload": True,
        "daemon_reexec": False,
        "scope": "system",
        "no_block": True,
        "force": True
    }
    systemctl = module.get_bin_path('systemctl', True)
    os.environ['XDG_RUNTIME_DIR'] = '/run/user/%s' % os.geteuid()

    if service['scope'] != 'system':
        systemctl += " --%s" % (service['scope'])

    if service['no_block']:
        systemctl += " --no-block"