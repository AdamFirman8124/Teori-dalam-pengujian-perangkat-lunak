

# Generated at 2022-06-13 06:21:05.891245
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:17.948250
# Unit test for function main
def test_main():

    '''
    at least one item must be required
    '''
    with pytest.raises(AnsibleFailJson) as exec_info:
        main()
    assert 'The `name` option is required' in str(exec_info.value)

    '''
    check exception thrown when a non-existent service is called with enabled state
    '''
    with pytest.raises(AnsibleFailJson) as exec_info:
        main(dict(
            name="foobar",
            enabled=True,
        ))
    assert "Service foobar does not exist" in str(exec_info.value)

    '''
    check exception thrown when a non-existent service is called with start state
    '''

# Generated at 2022-06-13 06:21:27.120599
# Unit test for function main
def test_main():
    from unittest import TestCase

    class TestMain(TestCase):
        def setUp(self):
            self.mock_system = ['systemd-213']
            self.mock_unit_name = 'sshd'
            self.mock_changed = False
            self.mock_running = False
            self.mock_loaded = False
            self.mock_enabled = False
            self.mock_masked = False

# Generated at 2022-06-13 06:21:33.421167
# Unit test for function main

# Generated at 2022-06-13 06:21:45.269985
# Unit test for function main
def test_main():
    mod = AnsibleModule(
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
    ),
    )

    test

# Generated at 2022-06-13 06:21:54.837069
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    multiline_value = '''{
    path=/usr/sbin/sshd ; argv[]=/usr/sbin/sshd -D $OPTIONS ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0
}'''
    singleline_value = '''{
    path=/usr/sbin/sshd ; argv[]=/usr/sbin/sshd -D $OPTIONS ; ignore_errors=no ; start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0}'''

    multi_out = parse_systemctl_show(['ExecStart=%s' % multiline_value])

# Generated at 2022-06-13 06:21:56.033822
# Unit test for function main
def test_main():
    assert callable(main)



# Generated at 2022-06-13 06:21:57.615748
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('Request was ignored')
    assert request_was_ignored('ignoring request')
    assert request_was_ignored('ignoring command')
    assert not request_was_ignored('=')



# Generated at 2022-06-13 06:22:06.642761
# Unit test for function main

# Generated at 2022-06-13 06:22:18.305138
# Unit test for function main
def test_main():
    # Test empty params
    params = dict()
    module = AnsibleModule(params)
    result = main()
    assert result['rc'] == 1


    # Test single service, non valid
    params = dict(name='test.service')
    module = AnsibleModule(params)
    result = main()
    assert result['rc'] == 1

    # Test single service, valid
    module = AnsibleModule(params)
    result = main()
    assert result['rc'] == 1

    # Test daemon_reload
    module = AnsibleModule(params)
    result = main()
    assert result['rc'] == 1

    # Test daemon_reexec
    module = AnsibleModule(params)
    result = main()
    assert result['rc'] == 1


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:41.479398
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    one_line = ['Id=foo']
    retval = parse_systemctl_show(one_line)
    expected_value = 'foo'
    assert retval['Id'] == expected_value, 'The function did not return the expected result.'

    multiline = ['ExecStart=\n', '      { path=/usr/bin/python2 ; argv[]=/usr/bin/python2 /usr/bin/sshd -D ; ignore_errors=no ;\n', '        start_time=[Mon 2017-10-16 16:32:57 EDT] ; stop_time=[n/a] ;\n', '        pid=0 ; code=(null) ; status=0/0 }\n']
    retval = parse_systemctl_show(multiline)

# Generated at 2022-06-13 06:22:45.732467
# Unit test for function main
def test_main():
    args = dict(
        name='sshd',
        enabled=False,
        scope='system'
    )
    # Load the module
    module = AnsibleModule(**args)
    # set params
    module._debug = False
    # call main
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:55.573952
# Unit test for function main

# Generated at 2022-06-13 06:23:07.085556
# Unit test for function main
def test_main():
    if not os.path.exists('/bin/systemctl'):
        # the os shouldn't have systemd, so we won't test it
        return


# Generated at 2022-06-13 06:23:15.037500
# Unit test for function main

# Generated at 2022-06-13 06:23:25.840620
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Check that we can handle single-line values
    lines1 = ['Description=some text here']
    expected_output1 = {'Description': 'some text here'}
    assert parse_systemctl_show(lines1) == expected_output1

    # Check that we can handle single-line values that start with {
    lines2 = ['Description={some text here']
    expected_output2 = {'Description': '{some text here'}
    assert parse_systemctl_show(lines2) == expected_output2

    # Check that we can handle multi-line values
    lines3 = ['ExecStart={', '  Path=/bin/a', '  Argument=1', '}']
    expected_output3 = {'ExecStart': '{\n  Path=/bin/a\n  Argument=1\n}'}
    assert parse_system

# Generated at 2022-06-13 06:23:33.990471
# Unit test for function main
def test_main():
    import json

    # mock ansible module

# Generated at 2022-06-13 06:23:42.548045
# Unit test for function main
def test_main():

    import os

    tmp_dir = os.path.realpath(tempfile.mkdtemp())
    sysvinit_path = os.path.join(tmp_dir, 'sysvinit')
    sysvinit_file_path = os.path.join(sysvinit_path, 'httpd')

    os.makedirs(sysvinit_path)
    os.mkdir(sysvinit_file_path)

    systemd_path = os.path.join(tmp_dir, 'systemd')
    systemd_file_path = os.path.join(tmp_dir, 'systemd', 'httpd.service')

    os.makedirs(systemd_path)

    with open(systemd_file_path, 'w') as f:
        f.write('[Unit]\n')

# Generated at 2022-06-13 06:23:52.984944
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:23:59.295465
# Unit test for function main
def test_main():
    # mock functions
    class MockAnsibleModule:
        def __init__(self):
            self.params = {}
            self.params['name'] = None
            self.params['state'] = None
            self.params['enabled'] = None
            self.params['force'] = None
            self.params['masked'] = None
            self.params['daemon_reload'] = None
            self.params['daemon_reexec'] = None
            self.params['scope'] = None
            self.params['no_block'] = None
            self.fail_json = None

        def get_bin_path(self, *args, **kwargs):
            return "/usr/bin/systemctl"

        def run_command(self, *args, **kwargs):
            return 0, "", ""


# Generated at 2022-06-13 06:24:49.581561
# Unit test for function main
def test_main():
    result = main()
    assert result is not None, 'Should not be None'

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils._text import to_bytes

main()

# Generated at 2022-06-13 06:24:56.909747
# Unit test for function main
def test_main():
    import doctest
    import sys
    results = doctest.testmod(sys.modules[__name__], optionflags=doctest.NORMALIZE_WHITESPACE)
    if results.failed != 0:
        sys.exit(1)

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.basic import AnsibleModule

if __name__ == '__main__':
    test_main()
    main()

# Generated at 2022-06-13 06:25:08.311142
# Unit test for function main

# Generated at 2022-06-13 06:25:09.765004
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:21.419237
# Unit test for function main
def test_main():
    # prep the environment
    import tempfile
    tmp_dir = tempfile.mkdtemp()
    tmp_rc_d = tempfile.mkdtemp(suffix="rc.d", dir=tmp_dir)
    tmp_systemd_system = tempfile.mkdtemp(suffix="system", dir=tmp_dir)
    rc_d_ansible = tempfile.mkdtemp(suffix="rc.d.ansible", dir=tmp_rc_d)
    service_file_path = os.path.join(tmp_systemd_system, 'foo.service')

    # create mock service
    os.makedirs(os.path.join(tmp_dir, 'usr', 'lib', 'systemd', 'system'))
    service_file = open(service_file_path, "w", encoding='utf-8')

# Generated at 2022-06-13 06:25:22.688765
# Unit test for function main
def test_main():
    pass


# import module snippets
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:26.075549
# Unit test for function main
def test_main():
    result = {
        "name": "foo",
        "changed": False,
        "status": {}
    }
    module = AnsibleModule({
        "name": "foo",
        "state": None,
        "enabled": None,
        "masked": None,
        "scope": "system",
        "no_block": False,
    })

    main()
    assert result == module.exit_json


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:36.139661
# Unit test for function main
def test_main():
    # Define mock objects
    class MockModule():
        def __init__(self):
            self.params = {}
            self.return_value = None

        def fail_json(self, msg, **kwargs):
            self.return_value = msg

        def exit_json(self, **kwargs):
            self.return_value = kwargs

        def warn(self, msg):
            pass

        def get_bin_path(self, command, required):
            if command in (
                    'systemctl',
                    'systemctl-daemon-reload',
            ):
                return command
            else:
                return None


# Generated at 2022-06-13 06:25:38.707210
# Unit test for function main
def test_main():
    # TODO: Implement unit test
    pass


# import module snippets
#from ansible.module_utils.basic import *
#from ansible.module_utils.basic import AnsibleModule
# run module function
#main()


# Generated at 2022-06-13 06:25:43.413159
# Unit test for function main
def test_main():
    test_cases = [
        {
            'name': 'test_1',
            'params': {
                'scope': 'system',
                'state': 'stopped',
                'enable': False,
                'masked': False,
                'daemon-reload': False,
                'daemon-reexec': False,
            }
        }
    ]
    for test_case in test_cases:
        unit = test_case['name']
        params = test_case['params']
        state = params['state']
        enabled = params['enable']
        masked = params['masked']
        daemon_reload = params['daemon-reload']
        daemon_reexec = params['daemon-reexec']
        scope = params['scope']

# Generated at 2022-06-13 06:26:55.050684
# Unit test for function main

# Generated at 2022-06-13 06:26:56.520978
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:07.200816
# Unit test for function main

# Generated at 2022-06-13 06:27:09.397385
# Unit test for function main
def test_main():

    with pytest.raises(SystemExit):
        main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:18.829608
# Unit test for function main
def test_main():
    import os
    from ansible.module_utils import basic


# Generated at 2022-06-13 06:27:25.985863
# Unit test for function main
def test_main():
    # read in test data
    f = open("./unit/systemd/ansible_module_service_systemd_arguments.json", "r")
    data = json.load(f)

    # create mock module
    module = AnsibleModuleMock(data)

    # set module args
    for arg in data['arguments']:
        module.params[arg] = data['arguments'][arg]

    # run module
    main()

    # gather and set results
    results = dict(
        changed=data['changed'],
        state=dict(
            status=data['status'],
        ),
    )

    # exit module
    module.exit_json(**results)


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:35.564389
# Unit test for function main
def test_main():
    unit = 'foo'

    # Test that 'systemctl' exists
    module = AnsibleModule(argument_spec={})
    systemctl = module.get_bin_path('systemctl', True)

    # Test the return of the function
    module = AnsibleModule(argument_spec={})
    with patch('ansible.module_utils.basic.AnsibleModule.run_command', return_value=(0, '0', '')):
        with patch('ansible.module_utils.basic.AnsibleModule.get_bin_path', return_value='/bin/systemctl'):
            with patch('ansible.module_utils.systemd.sysv_is_enabled', return_value=True):
                with patch('ansible.module_utils.systemd.sysv_exists', return_value=True):
                    assert main

# Generated at 2022-06-13 06:27:38.266567
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:53.104362
# Unit test for function main
def test_main():
    # test catches import error if module could not be loaded
    from ansible.modules.system.systemd import main

    module = MagicMock()
    module.params = {'enabled': True}
    module.run_command = MagicMock()
    module.fail_json = MagicMock()
    module.exit_json = MagicMock()
    module.get_bin_path = MagicMock(return_value='/usr/bin/systemctl')
    module.check_mode = False

    module.run_command.side_effect = [
        (1, '', 'Failed to parse bus message'),
        (1, 'active', ''),
        (0, '', ''),
        (0, '', ''),
        (1, '', ''),
    ]

    main(module)

# Generated at 2022-06-13 06:28:01.104323
# Unit test for function main

# Generated at 2022-06-13 06:29:56.416564
# Unit test for function main
def test_main():
    import os
    import shutil
    import tempfile
    import json

    module_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'ansible_collections', 'ansible', 'community', 'plugins', 'modules', 'systemd')

    systemd_module = os.path.join(module_path, 'systemd.py')

    tmp = tempfile.mkdtemp()

    mock_systemd_file = os.path.join(tmp, 'test_service.service')
    mock_systemd_file_symlink = os.path.join(tmp, 'test_service_symlink.service')
    mock_systemd_file_mask = os.path.join(tmp, 'test_service_mask.service')
    mock_systemd_file

# Generated at 2022-06-13 06:30:04.271830
# Unit test for function main
def test_main():
    # Setup mocks
    [mock_run_command, mock_check_rc, mock_fail_json, mock_exit_json, mock_warn, mock_get_bin_path] = mock.Mock(), mock.Mock(), mock.Mock(), mock.Mock(), mock.Mock(), mock.Mock()
    mock_run_command.return_value = [0, "mock_stdout", "mock_stderr"]
    mock_get_bin_path.return_value = "test_system"

# Generated at 2022-06-13 06:30:07.016487
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    argv = ['systemd','foo','bar','baz','quux','corge','garply']   # last four args are ignored
    with pytest.raises(SystemExit):
        basic._ANSIBLE_ARGS = argv
        main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:30:07.911697
# Unit test for function main
def test_main():
    assert main() == None

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:30:08.788301
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:30:13.584164
# Unit test for function main
def test_main():
    # Module parameters
    module_params = {
        "name": "test-unit",
        "state": "started",
        "enabled": False,
        "masked": True,
        "daemon_reload": True,
        "daemon_reexec": True,
        "force": True,
        "scope": "global",
        "no_block": True
    }

    # State of the target
    target_state = {
        'state': 'stopped',
        'enabled': True,
        'masked': True,
        'status': {
            'ActiveState': 'inactive',
            'LoadState': 'loaded',
        }
    }

    # Merged current module parameters and target state
    result = merge_module_params(module_params, target_state)

    # Initialize module
   

# Generated at 2022-06-13 06:30:22.241473
# Unit test for function main
def test_main():
    # create a mock module
    mock_module = Mock(name='ansible.module_utils.basic.AnsibleModule')
    mock_module.params = {
        'name' : 'foo',
        'enabled': True,
        'force': False,
        'masked': False,
        'daemon_reload': False,
        'daemon_reexec': False,
        'scope': 'system',
        'no_block' : False,
        'state': None
    }
    # mock get_bin_path()
    mock_get_bin_path = Mock(name='ansible.module_utils.basic.AnsibleModule.get_bin_path')
    mock_get_bin_path.return_value = 'some_binary'
    mock_module.get_bin_path = mock_get_

# Generated at 2022-06-13 06:30:33.202421
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.systemd import request_was_ignored
