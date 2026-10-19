

# Generated at 2022-06-13 06:20:54.368018
# Unit test for function main
def test_main():
    # Hack to run unit tests in centos
    argv = sys.argv
    sys.argv = ['systemd', 'enabled=True', 'name=test_service']

    with mock.patch.object(AnsibleModule, 'run_command', return_value=(0, 'enabled', '')):
        with pytest.raises(SystemExit) as cm:
            main()
        assert cm.value.code == 0

    sys.argv = argv
# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:03.462668
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:09.165054
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    assert parse_systemctl_show(["Id=sshd.service", "Description=OpenSSH server daemon", "ConditionPathExists=/etc/ssh/sshd_not_to_be_run"]) \
        == {'Id': 'sshd.service', 'Description': 'OpenSSH server daemon', 'ConditionPathExists': '/etc/ssh/sshd_not_to_be_run'}

# Generated at 2022-06-13 06:21:19.646565
# Unit test for function main
def test_main():
    from ansible.module_utils._text import to_bytes
    from ansible_collections.notstdlib.moveitallout.plugins.module_utils.common.fetch import fetch_url
    fetch_url.FetchUrl = FetchUrlMock
    mock_fetch_url = FetchUrlMock
    unit = 'docker.service'
    state = 'stopped'
    enabled = True
    masked = True
    force = True
    no_block = True

# Generated at 2022-06-13 06:21:28.125621
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('whatever') == False
    assert request_was_ignored('another thing=f') == False
    assert request_was_ignored('ignoring request (user-defined command)') == True
    assert request_was_ignored('ignoring command (user-defined command)') == True
    assert request_was_ignored('ignoring request (user-defined command) to reload') == True
    assert request_was_ignored('ignoring command (user-defined command) to reload') == True
    assert request_was_ignored('ignoring request (unit doest not exist)') == True
    assert request_was_ignored('ignoring command (unit doest not exist)') == True



# Generated at 2022-06-13 06:21:33.521222
# Unit test for function main
def test_main():
    for params, expected_result in [
        [
            {'daemon_reload': False, 'enabled': None, 'masked': None, 'name': None, 'no_block': False, 'scope': 'system', 'state': None, 'force': False, 'daemon_reexec': False},
            {'daemon_reload': False, 'enabled': None, 'masked': None, 'name': None, 'no_block': False, 'scope': 'system', 'state': None, 'force': False, 'daemon_reexec': False}
        ],
    ]:
        result = main(params)
        assert result == expected_result

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:45.353161
# Unit test for function main
def test_main():
    ''' Unit test for Ansible module: system_service '''

    '''
    Mock values to be used by the function main
    '''

    fake_args = dict(
        name='fake_service_name',
        state='fake_state',
        enabled='fake_enabled',
        masked='fake_masked',
        daemon_reload=True,
        daemon_reexec=True,
        scope='system',
        no_block=False,
    )
    fake_args = dict(name='fake_service_name')
    # fake_args = dict(daemon_reload=True)
    # fake_args = dict(daemon_reexec=True)
    # fake_args = dict(masked=True)
    # fake_args = dict(state='started')
    # fake_args = dict

# Generated at 2022-06-13 06:21:54.885191
# Unit test for function main
def test_main():
    from ansible.modules.system.systemd import main
    from ansible.module_utils.basic import AnsibleModule
    import tempfile
    import shutil
    import os
    import json
    import errno
    import subprocess

    params = dict(
        name="mock_service",
    )

    # Test if a service that is not installed on the system, but is a valid
    # systemd unit, is reported as missing
    def test_systemd_unit_not_installed():
        tmp_dir = tempfile.mkdtemp(prefix='ansible_test')

# Generated at 2022-06-13 06:22:07.106463
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:22:18.848936
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:22:45.475852
# Unit test for function main
def test_main():
    # mock module
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', aliases=['service', 'unit']),
            enabled=dict(type='bool'),
            masked=dict(type='bool'),
            daemon_reload=dict(type='bool', default=False, aliases=['daemon-reload']),
        ))
    # get function under test
    main = sys.modules[__name__].main

    # set return values
    # module.run_command = MagicMock(return_value=(0, '', ''))
    # module.exit_json = MagicMock()
    # module.warn = MagicMock()
    # module.fail_json = MagicMock()

    # run function under test
    # main()

    # root cause of mock_open failure
   

# Generated at 2022-06-13 06:22:55.303512
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Test case 1: A single-line value.
    inp = ['Id=foobar.service']
    assert parse_systemctl_show(inp) == {
        'Id': 'foobar.service',
    }
    # Test case 2: A multi-line value.
    inp = [
        'ExecReload=',
        '  { path=/bin/kill ; argv[]=/bin/kill -HUP $MAINPID ; ignore_errors=no ; ',
        '    start_time=[n/a] ; stop_time=[n/a] ; pid=0 ; code=(null) ; status=0/0 }',
    ]

# Generated at 2022-06-13 06:22:59.679068
# Unit test for function main

# Generated at 2022-06-13 06:23:09.925616
# Unit test for function main
def test_main():
    unit = 'foo'
    params = {}
    params['name'] = unit
    params['state'] = None
    params['enabled'] = None
    params['masked'] = None
    params['force'] = False
    params['daemon_reload'] = False
    params['daemon_reexec'] = False
    params['scope'] = 'system'
    params['no_block'] = False
    rc = 0
    out = err = ''
    result = {}


# Generated at 2022-06-13 06:23:18.069314
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 06:23:28.816515
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:23:40.043617
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from io import StringIO
    import sys


# Generated at 2022-06-13 06:23:52.133040
# Unit test for function main
def test_main():
    spec = dict(
        name=dict(type='str', aliases=['service', 'unit']),
        state=dict(type='str', choices=['reloaded', 'restarted', 'started', 'stopped']),
        enabled=dict(type='bool'),
        force=dict(type='bool'),
        masked=dict(type='bool'),
        daemon_reload=dict(type='bool', aliases=['daemon-reload']),
        daemon_reexec=dict(type='bool', aliases=['daemon-reexec']),
        scope=dict(type='str', choices=['system', 'user', 'global']),
        no_block=dict(type='bool')
    )

# Generated at 2022-06-13 06:23:58.395002
# Unit test for function main
def test_main():
    def mock_run_command(module, cmd):
        if cmd[:9] == 'systemctl ':
            return [0, '', '']
        return [1, '', '']

    def mock_fail_json(module, msg):
        assert module is sys.modules['__main__'].AnsibleModule
        assert msg == 'service is not installed'

    def mock_get_bin_path(self, executable, required=False, opt_dirs=[]):
        self.assertEqual('systemctl', executable)
        return executable

    def mock_run_command(module, cmd):
        if cmd[:9] == 'systemctl ':
            return [0, '', '']
        return [1, '', '']


# Generated at 2022-06-13 06:23:59.762971
# Unit test for function main
def test_main():
    with open('testfile.txt') as f:
        content = f.read()
        print(content)


# Generated at 2022-06-13 06:24:25.134447
# Unit test for function main
def test_main():

    # If you want to create a unit test file:
    import os
    import tempfile
    import time

    # This is a hack to prevent the module from exiting
    class SetExitJsonModule(object):
        def __init__(self, module):
            self.module = module
            self.exit_json = module.exit_json
            self.fail_json = module.fail_json
            self.params = module.params
            self.systemctl = module.get_bin_path('systemctl', True)

        def exit_json(self, *args, **kwargs):
            # print ("args:", args)
            # print ("kwargs:", kwargs)
            if 'changed' in kwargs:
                self.module.exit_json_data = {'changed': kwargs['changed']}

# Generated at 2022-06-13 06:24:36.842746
# Unit test for function main
def test_main():
    """ Test ansible-module-systemd's main function with a mock response """

    #
    # Function parameters
    #
    module = object()
    module.get_bin_path = Mock(return_value='/bin/systemctl')
    module.params = dict(
        name='sshd',
        state=None,
        enabled=None,
        force=False,
        masked=None,
        daemon_reload=True,
        daemon_reexec=False,
        scope='system',
        no_block=False,
    )
    module.run_command = Mock()

# Generated at 2022-06-13 06:24:48.417527
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(
        name=dict(type='str'),
        state=dict(type='str', choices=['reloaded', 'restarted', 'started', 'stopped']),
        enabled=dict(type='bool'),
        force=dict(type='bool'),
        masked=dict(type='bool'),
        scope=dict(type='str', default='system', choices=['system', 'user', 'global']),
        no_block=dict(type='bool', default=False),
    )
    )

    unit = module.params['name']
    systemctl = module.get_bin_path('systemctl', True)


# Generated at 2022-06-13 06:24:49.865685
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:00.361290
# Unit test for function main
def test_main():
    # Test with service name with params
    test_unit = '/usr/local/bin/unit'
    unit_base, sep, suffix = test_unit.partition('@')
    unit_search = unit_base + sep
    test_params = dict(name=test_unit, enabled=True, scope='system', no_block=False)

# Generated at 2022-06-13 06:25:10.277822
# Unit test for function main

# Generated at 2022-06-13 06:25:21.548688
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.systemd import is_running_service
    import os
    import sys

    if six.PY3 and getattr(sys, 'frozen', False):
        import importlib
        importlib.reload(sys)
        sys.setdefaultencoding('utf8')

    # AnsibleModule tests

# Generated at 2022-06-13 06:25:32.217886
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:25:38.679131
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Single line
    lines = ["Id=totally.service"]
    parsed = parse_systemctl_show(lines)
    assert(parsed == {'Id': 'totally.service'})

    # Multi line
    lines = ["Id=totally.service",
             "Description=This is a multi-line description",
             "   that makes a good unit test!"]
    parsed = parse_systemctl_show(lines)
    assert(parsed == {'Id': 'totally.service',
                      'Description': 'This is a multi-line description\n  that makes a good unit test!'})



# Generated at 2022-06-13 06:25:45.908631
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:26:47.542691
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:26:56.539210
# Unit test for function main
def test_main():
    # Mock of module.
    class ModuleMock(object):
        def __init__(self):
            self.params = {}
            self.params['scope'] = None
            self.params['no_block'] = False
            self.params['force'] = False
            self.params['daemon_reload'] = False
            self.params['daemon_reexec'] = False
            self.params['masked'] = None
            self.params['enabled'] = None
            self.params['state'] = None
        def parameterType(self, param):
            return self.params[param]
        def get_bin_path(self, name, required):
            return 'systemctl'
        def run_command(self, name, check_rc=True):
            # Output of `systemctl show <unit>`
            unit_output

# Generated at 2022-06-13 06:27:07.236918
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    lines_test = '''
Description=Test unit
LoadState=loaded
ActiveState=active
SubState=running
UnitFileState=enabled
'''.split('\n')
    assert parse_systemctl_show(lines_test) == dict(Description='Test unit', LoadState='loaded', ActiveState='active', SubState='running', UnitFileState='enabled')
    lines_test = '''
Description=Multi-
 line
LoadState=loaded
ActiveState=active
SubState=running
UnitFileState=enabled
'''.split('\n')
    assert parse_systemctl_show(lines_test) == dict(Description='Multi-\n line', LoadState='loaded', ActiveState='active', SubState='running', UnitFileState='enabled')

# Generated at 2022-06-13 06:27:17.728937
# Unit test for function main

# Generated at 2022-06-13 06:27:24.342072
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:27:32.347857
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec=dict(
                                              state=dict(type='str', required=False, choices=['started', 'stopped']),
                                              enabled=dict(type='bool'),
                                              systemctl=dict(required=False),
                                              name=dict(type='str', aliases=['service', 'unit']),
                                             )
                         )

    try:
        main(module)
    except SystemExit:
        pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:41.441832
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:27:49.950398
# Unit test for function main
def test_main():
    testargs = { 'name': 'show',
                 'state': 'reloaded',
                 'enabled': False,
                 'force': False,
                 'masked': True,
                 'daemon_reload': True,
                 'daemon_reexec': True,
                 'scope': 'system',
                 'no_block': False }
    main(testargs)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:59.781760
# Unit test for function main
def test_main():
    #assert False

    import sys
    #sys.argv.append('--ingore-deps install')
    #sys.argv.append('--force --autoremove')
    #sys.argv.append('--state absent')
    #sys.argv.append('--extra-vars')
    #sys.argv.append('{"with_deps": true}')
    #sys.argv.append('emacs')

    sys.argv.append('install')
    sys.argv.append('--extra-vars')

# Generated at 2022-06-13 06:28:12.468101
# Unit test for function main
def test_main():
    my_module = AnsibleModule({
        'name': 'test',
        'enabled': True,
        'state': 'started',
        'systemctl_command': '/bin/systemctl',
    })
    my_module.run_command = MagicMock()
    my_module.run_command.return_value = (0, 'out', 'err')
    my_module.check_mode = False

    my_module.get_bin_path = MagicMock()
    my_module.get_bin_path.return_value = '/bin/systemctl'

    my_module.fail_json = MagicMock()
    my_module.fail_json.side_effect = SystemExit
    my_module.exit_json = MagicMock()

    with pytest.raises(SystemExit):
        main()
    my_

# Generated at 2022-06-13 06:29:52.917836
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:29:54.206335
# Unit test for function main
def test_main():
    print("***")
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:30:00.639371
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    parsed = parse_systemctl_show(
            ['Description=My Service',
             'ExecStart={',
             '  first line',
             '  second line}',
             'ExecReload={',
             '  key1=value1',
             '  key2=value2}'])
    assert parsed['Description'] == 'My Service'
    assert parsed['ExecStart'] == '{\n  first line\n  second line}'
    assert parsed['ExecReload'] == '{\n  key1=value1\n  key2=value2}'


# Generated at 2022-06-13 06:30:07.602081
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Test single-line, multi-line, Exec*, non-Exec*, etc.
    assert parse_systemctl_show(['SingleLineValue=foo', 'MultiLineValue={', '    moo', '}']) == {'SingleLineValue': 'foo', 'MultiLineValue': 'moo'}
    assert parse_systemctl_show(['ExecFoo={', '    foo', '}', 'ExecBar={', '    bar', '}', 'MultiLineValue={', '    moo', '}']) == {'ExecFoo': 'foo', 'ExecBar': 'bar', 'MultiLineValue': 'moo'}

# Generated at 2022-06-13 06:30:16.582164
# Unit test for function main

# Generated at 2022-06-13 06:30:31.429496
# Unit test for function main