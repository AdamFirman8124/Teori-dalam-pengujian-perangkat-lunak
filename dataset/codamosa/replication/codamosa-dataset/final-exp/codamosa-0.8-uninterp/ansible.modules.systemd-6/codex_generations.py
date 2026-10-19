

# Generated at 2022-06-13 06:21:15.889168
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={})
# Simple unit test for function sysv_exists

# Generated at 2022-06-13 06:21:27.370985
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:21:39.224736
# Unit test for function main

# Generated at 2022-06-13 06:21:50.574039
# Unit test for function main
def test_main():
    unit_test = {}
    unit_test['unit'] = 'crond'
    unit_test['scope'] = 'system'
    unit_test['daemon_reload'] = False
    unit_test['daemon_reexec'] = False
    unit_test['masked'] = None
    unit_test['force'] = False
    unit_test['state'] = None
    unit_test['enabled'] = None

# Generated at 2022-06-13 06:22:03.996135
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:22:12.925294
# Unit test for function main
def test_main():
    module = Datacenter()
    suite = unittest.TestSuite()
    test_cases = []
    res = None

    module.params = {'name': None}
    test_cases.append(
        (
            (0, "", ""),
            {'name': None, 'state': None, 'enabled': None, 'force': None, 'masked': None, 'daemon_reload': False,
             'daemon_reexec': False, 'scope': 'system', 'no_block': False},
            {
                'changed': False,
                'name': None,
                'status': {}}
        )
    )


# Generated at 2022-06-13 06:22:22.620750
# Unit test for function main
def test_main():

    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.common.shell import Cli
    import shutil
    import os.path

    # Temp systemctl binary file
    tmp_systemctl = '/tmp/systemctl'

    # Select action based on case
    def fake_systemctl_action(cli):
        rc = 0
        out = ''
        err = ''
        if cli.invoked_command == 'list-unit-files':
            out = '''
UNIT FILE                                             STATE
anacron.service                                       enabled
atd.service                                           enabled
autovt@.service                                       masked
'''
        elif cli.invoked_command == 'is-enabled':
            out = 'enabled'

        return rc, out, err

    # Mock systemctl


# Generated at 2022-06-13 06:22:32.954937
# Unit test for function main
def test_main():
    """
    Unit test for main
    """
    global unit
    global systemctl
    global main_rc
    global main_out
    global main_err
    global rc
    global out
    global err
    global module

# Generated at 2022-06-13 06:22:45.390784
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Test with simple single-line values
    inp = []
    inp.append('Key1=Value1')
    inp.append('Key2=Value2')
    inp.append('Key3=Value3')
    result = parse_systemctl_show(inp)
    assert dict(result) == dict(Key1='Value1', Key2='Value2', Key3='Value3')

    # Test with a single multi-line value
    inp = []
    inp.append('Key1=Value1')
    inp.append('Key2=Value2')
    inp.append('ExecStart=')
    inp.append(' command1')
    inp.append(' command2')
    inp.append(' Key3=Value3')
    result = parse_systemctl_show(inp)
   

# Generated at 2022-06-13 06:22:55.232199
# Unit test for function main

# Generated at 2022-06-13 06:23:13.150243
# Unit test for function main
def test_main():
   assert main() == None

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:19.039992
# Unit test for function main
def test_main():
    with open('unit_test/unit_systemd.json') as f:
        module = AnsibleModule(argument_spec=ast.literal_eval(f.read()))
    systemctl = module.get_bin_path('systemctl', True)
    assert not is_chroot(module)
    # requires a system in the known_hosts of the testing machine
    module.params['scope'] = 'system'
    module.params['daemon_reload'] = True
    module.params['daemon_reexec'] = True
    main()
    
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:24.505704
# Unit test for function main
def test_main():
    args = dict(
        state='reloaded',
        name='auditd'
    )
    import platform

# Generated at 2022-06-13 06:23:26.326341
# Unit test for function main
def test_main():
    import ansible.module_utils.systemd
    assert 'systemd' == ansible.module_utils.systemd.__name__


# import module snippets
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:34.276125
# Unit test for function main
def test_main():
    # Requests
    class Request(object):
        def __init__(self, **kwargs):
            self.module = kwargs
            self.check_mode = kwargs['check_mode']
            self.params = kwargs['params']
            self.rc = 0
            self.stdout = ''
            self.stderr = ''

            if kwargs.get('rc'):
                self.rc = kwargs['rc']
            if kwargs.get('stdout'):
                self.stdout = kwargs['stdout']
            if kwargs.get('stderr'):
                self.stderr = kwargs['stderr']

# Generated at 2022-06-13 06:23:42.732397
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    test_unit = '/usr/lib/systemd/system/test_unit'
    test_unit_link = os.path.join(os.path.dirname(test_unit), 'test_unit.service')
    os.makedirs(os.path.dirname(test_unit), exist_ok=True)
    # The full output of systemctl show is several hundred lines long; just include a few representative lines in the unit test
    # These lines are taken from the output of 'systemctl show crond.service' on CentOS 7.3

# Generated at 2022-06-13 06:23:53.152840
# Unit test for function main
def test_main():
    # Loading mocked module
    from ansible.modules.system.systemd import importlib_mock
    from ansible.modules.system.systemd import subprocess_mock
    from ansible.modules.system.systemd import os_mock
    from ansible.modules.system.systemd import stat_mock
    from ansible.modules.system.systemd import systemctl_show_mock
    from ansible.modules.system.systemd import systemctl_list_unit_files_mock


# Generated at 2022-06-13 06:23:54.360524
# Unit test for function main
def test_main():
    print("running func main")
    main()

test_main()

# Generated at 2022-06-13 06:24:00.594556
# Unit test for function main

# Generated at 2022-06-13 06:24:12.379422
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.basic import env_fallback
    import sys
    import os
    reload(sys)
    sys.setdefaultencoding("utf-8")
    sys.path.append(os.path.abspath("/tmp"))

    def test_set_module_args(args):
        args = json.dumps({'ANSIBLE_MODULE_ARGS': args})
        basic._ANSIBLE_ARGS = to_bytes(args)


# Generated at 2022-06-13 06:24:40.430025
# Unit test for function main
def test_main():
    test_cases = [{
        'name': 'foobar',
        'state': 'started'
    }, {
        'name': 'foobar',
        'enabled': True
    }, {
        'name': 'foobar',
        'enabled': False
    }]

    for test_case in test_cases:
        module = AnsibleModule(**test_case)

        systemctl = module.get_bin_path('systemctl', True)

        if os.getenv('XDG_RUNTIME_DIR') is None:
            os.environ['XDG_RUNTIME_DIR'] = '/run/user/%s' % os.geteuid()

        ''' Set CLI options depending on params '''
        # if scope is 'system' or None, we can ignore as there is no extra switch.
        #

# Generated at 2022-06-13 06:24:52.269555
# Unit test for function main
def test_main():
    import json
    import tempfile
    import shutil
    import os

    class Args(object):
        name = 'foo'
        state = 'stopped'
        enabled = False
        masked = False
        daemon_reload = False
        daemon_reexec = True
        scope = 'system'
        no_block = False

    def create_test_files(test_dir, custom_systemd_dir):
        unit_dir = os.path.join(test_dir, 'etc', 'systemd', 'system')
        os.makedirs(unit_dir)

        os.makedirs(os.path.join(test_dir, 'etc', 'systemd', 'user'))
        os.makedirs(os.path.join(test_dir, 'etc', 'systemd', 'global'))

       

# Generated at 2022-06-13 06:24:53.409640
# Unit test for function main
def test_main():
    pass


# import module snippets
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:57.894035
# Unit test for function main
def test_main():
    import subprocess
    import shlex
    p = subprocess.Popen(shlex.split('python systemctl.py'), stdout=subprocess.PIPE)
    print(p.communicate()[0].decode())


if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 06:25:09.247335
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    # Test 1: single-line value
    lines = ['foo=bar']
    assert parse_systemctl_show(lines) == {'foo': 'bar'}
    # Test 2: multi-line value, with multiline as first line
    lines = ['foo={', 'bar', 'baz', '}']
    assert parse_systemctl_show(lines) == {'foo': '{\nbar\nbaz\n}'}
    # Test 3: multi-line value, with multiline as second line
    lines = ['foo=bar', 'baz={', 'blah', '}']
    assert parse_systemctl_show(lines) == {'foo': 'bar', 'baz': '{\nblah\n}'}
    # Test 4: multi-line value, with final value as first line

# Generated at 2022-06-13 06:25:20.028033
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_bytes
    import sys
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    old_run_command = module.run_command
    module.run_command = lambda *args, **kwargs: (0, to_bytes('', encoding=sys.getdefaultencoding()), to_bytes('', encoding=sys.getdefaultencoding()))
    module.exit_json = lambda **kwargs: None
    main()
    module.run_command = old_run_command


# import module snippets
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:29.882801
# Unit test for function main
def test_main():
    os.environ['SYSTEMD_OFFLINE'] = '1'

# Generated at 2022-06-13 06:25:38.814405
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:25:45.994660
# Unit test for function main
def test_main():
    import sys
    import subprocess
    sys.path.append("./library")
    import pytest
    import mock
    from AnsibleModule_systemctl import AnsibleModule
    from SystemCtl_Module import main
    with mock.patch.object(sys, 'argv', [__file__, 'test', '-s']):
        with pytest.raises(SystemExit):
            sys.exit(main())

    with mock.patch.object(sys, 'argv', [__file__, 'test']):
        with pytest.raises(SystemExit):
            sys.exit(main())

    with mock.patch.object(sys, 'argv', [__file__, 'test', '-vvvv']):
        with pytest.raises(SystemExit):
            sys.exit(main())


# Generated at 2022-06-13 06:25:55.061216
# Unit test for function main
def test_main():
    # pylint: disable=bare-except
    # pylint: disable=import-error
    # pylint: disable=attribute-defined-outside-init
    # pylint: disable=no-member
    # pylint: disable=no-self-use
    # pylint: disable=global-statement
    # pylint: disable=redefined-outer-name

    class FakeModule:
        '''
            Fake module for the systemctl module tests
        '''
        def __init__(self, params):
            self.params = params

        def check_mode(self):
            '''
                Fake Ansible check_mode method
            '''
            if self.params['check_mode']:
                sys.exit(0)


# Generated at 2022-06-13 06:26:48.779781
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('') is False
    assert request_was_ignored('=') is False
    assert request_was_ignored('ignoring request') is True
    assert request_was_ignored('test\nignoring request') is True



# Generated at 2022-06-13 06:26:55.018623
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
     sample_lines = ['Id=ansible.service',
                     'Description={',
                     ' This is the ansible service',
                     '}',
                     'ExecStart=/bin/true',
                     'Wants=network.target',
                     'After=network.target']
     expected_value = {
        'Id': 'ansible.service',
        'Description': 'This is the ansible service',
        'ExecStart': '/bin/true',
        'Wants': 'network.target',
        'After': 'network.target'
     }
     assert parse_systemctl_show(sample_lines) == expected_value


# Generated at 2022-06-13 06:27:06.082338
# Unit test for function main
def test_main():
    ''' Test the main entry point for the module '''


# Generated at 2022-06-13 06:27:08.564602
# Unit test for function main
def test_main():
  with pytest.raises(AnsibleFailJson) as excinfo:
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:13.001666
# Unit test for function request_was_ignored
def test_request_was_ignored():
    assert request_was_ignored('ignoring request')
    assert request_was_ignored('ignoring command')
    assert not request_was_ignored('inactive (dead)')
    assert not request_was_ignored('inactive (dead)')



# Generated at 2022-06-13 06:27:15.305759
# Unit test for function main
def test_main():
    result = {}
    with pytest.raises(SystemExit):
        main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:22.306646
# Unit test for function main

# Generated at 2022-06-13 06:27:28.557018
# Unit test for function main
def test_main():
    import sys
    import doctest
    old_args = sys.argv
    sys.argv = ['ansible-test', '--allow-unsupported-check', 'systemd']
    doctest.testmod()
    sys.argv = old_args


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:36.755221
# Unit test for function main
def test_main():
    from ansible.module_utils.systemd import UnitFlags
    from collections import namedtuple

    test = namedtuple('module', 'params,check_mode,get_bin_path,run_command')(
        params={'name': 'test_service', 'enabled': True, 'masked': False, 'scope': None},
        check_mode=False,
        get_bin_path=lambda x, y: 'test_bin_path',
        run_command=lambda x: (0, 'ok', ''))

    # Create mock commands
    def mock_cmd(cmd, *args, **kwargs):
        if 'is-enabled' in cmd:
            return UnitFlags.Masked, '', ''
        if 'enable' in cmd:
            return 0, 'ok', ''
    test.run_command = mock_cmd

   

# Generated at 2022-06-13 06:27:52.604884
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:28:26.190654
# Unit test for function main
def test_main():
    for unit in ['student', 'no-such-unit']:
        os.environ['SYSTEMD_OFFLINE'] = '0'
        if unit == 'no-such-unit':
            os.environ['SYSTEMD_OFFLINE'] = '1'

# Generated at 2022-06-13 06:28:41.642356
# Unit test for function main

# Generated at 2022-06-13 06:28:52.018768
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', aliases=['service', 'unit']),
            state=dict(type='str', choices=['reloaded', 'restarted', 'started', 'stopped']),
            enabled=dict(type='bool'),
            force=dict(type='bool'),
            masked=dict(type='bool'),
        ),
        required_one_of=[['state', 'enabled', 'masked']],
        required_by=dict(
            state=('name', ),
            enabled=('name', ),
            masked=('name', ),
        ),
        supports_check_mode=True,
    )
    rc = 0
    out = err = ''

# Generated at 2022-06-13 06:29:00.566095
# Unit test for function main

# Generated at 2022-06-13 06:29:06.919120
# Unit test for function parse_systemctl_show

# Generated at 2022-06-13 06:29:17.113940
# Unit test for function parse_systemctl_show
def test_parse_systemctl_show():
    test_cases = dict()
    test_cases['input'] = []
    test_cases['output'] = dict()

    test_cases['input'].append('Description=some value')
    test_cases['output'] = dict(Description='some value')

    test_cases['input'].append('Description=some other value')
    test_cases['output']['Description'] += '\n' + 'some other value'

    test_cases['input'].append('Description=yet another value')
    test_cases['output']['Description'] += '\n' + 'yet another value'

    test_cases['input'].append('ExecStart={')
    test_cases['input'].append('  PathExistsGlob=')
    test_cases['input'].append('}')


# Generated at 2022-06-13 06:29:23.930058
# Unit test for function main

# Generated at 2022-06-13 06:29:32.871238
# Unit test for function main
def test_main():
    fake_module = FakeModule({
        'name': 'dummy',
        'state': 'reloaded',
        'enabled': False,
        'masked': True,
        'daemon_reload': True,
        'daemon_reexec': True,
        'scope': 'global'
    })
    with mock.patch('ansible_collections.ansible.community.plugins.modules.systemd.ModuleArgs.get_bin_path', return_value='/usr/bin/systemctl'):
        with mock.patch('ansible_collections.ansible.community.plugins.modules.systemd.run_command', return_value=(0, '', '')):
            main()

# import module snippets
from ansible.module_utils.basic import *

if __name__ == '__main__':
    main

# Generated at 2022-06-13 06:29:42.425665
# Unit test for function main
def test_main():
    unit = 'httpd'
    systemctl = 'systemctl'

    ''' Set CLI options depending on params '''
    # if scope is 'system' or None, we can ignore as there is no extra switch.
    # The other choices match the corresponding switch
    # if module.params['scope'] != 'system':
    #    systemctl += " --%s" % module.params['scope']

    if True:
        systemctl += " --no-block"
    if True:
        systemctl += " --force"
    if False:
        print(systemctl)
    rc = 0
    out = err = ''
    result = dict(
        name=unit,
        changed=False,
        status=dict(),
    )

    # Run daemon-reload first, if requested

# Generated at 2022-06-13 06:29:50.787948
# Unit test for function parse_systemctl_show