

# Generated at 2022-06-13 06:21:45.966209
# Unit test for function main

# Generated at 2022-06-13 06:21:56.693314
# Unit test for function main
def test_main():
    def daemonize_mock(module, cmd):
        return (0, '', '')

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
            daemonize=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )


# Generated at 2022-06-13 06:21:57.346619
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:01.410522
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={'name': dict(required=False, type='str'),
                                          'state': dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
                                          'enabled': dict(type='bool'),
                                          'sleep': dict(type='int', default=1),
                                          'pattern': dict(type='str'),
                                          'arguments': dict(type='str', aliases=['args']),
                                          'runlevels': dict(type='list', elements='str'),
                                          'daemonize': dict(type='bool', default=True),})
    rc = 0
    out = err = ''

# Generated at 2022-06-13 06:22:11.289751
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )


# Generated at 2022-06-13 06:22:12.793557
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:19.422136
# Unit test for function main
def test_main():
    cur_argv = sys.argv[1:]
    print("cur_argv is: %s\n" % cur_argv)
    assert True == True
    # assert 'ansible' == cur_argv[1]
    assert 'sysvinit' == cur_argv[2]
    assert 'name=sshd' == cur_argv[3]
    assert 'state=started' == cur_argv[4]


# Generated at 2022-06-13 06:22:30.650448
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
            daemonize=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )

    name = module.params['name']
    action = module.params['state']

# Generated at 2022-06-13 06:22:41.942569
# Unit test for function main
def test_main():
    import sys
    import ansible.module_utils.sysvinit_service_helper as mod
    mod.sysv_is_enabled = lambda x: True
    mod.sysv_exists = lambda x: True
    mod.get_sysv_script = lambda x: '/sbin/service'
    mod.get_ps = lambda x, y: True
    mod.fail_if_missing = lambda x, y, z: True

    class Target(object):
        def __init__(self, target):
            self.bin_path = lambda x: target
    class FakeModule(object):
        def __init__(self, rval, **kwargs):
            self.params = kwargs
            self.run_command = lambda x: (0, rval, '')

# Generated at 2022-06-13 06:22:52.699670
# Unit test for function main
def test_main():
    from ansible.module_utils.service import sysv_exists
    from ansible.module_utils.basic import AnsibleModule
    sysvinit_module = AnsibleModule({
        "name": "httpd",
        "daemonize": True,
        "state": "started",
        "enabled": True,
        "runlevels": [],
        "pattern": None,
        "arguments": None,
        "sleep": 1,
    }, no_log=True)
    assert(sysvinit_module.daemon_handle is None)

# Generated at 2022-06-13 06:24:30.740166
# Unit test for function main
def test_main():
    module = AnsibleModule({
        'name': 'apache2',
        'state': None,
        'enabled': None
        },
        check_mode=True,
        supports_check_mode=True
    )


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:40.758355
# Unit test for function main
def test_main():
    import sys
    import os
    import shutil
    import tempfile
    import subprocess

    sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
    # We can only test the module on Linux, because the behaviour of the
    # module is different on other Operating Systems
    if os.name != 'posix':
        return

    from ansible.module_utils.basic import AnsibleModule, get_exception

    # Creating a simple init script for the tests
    test_script = tempfile.NamedTemporaryFile(delete=False)

# Generated at 2022-06-13 06:24:52.662859
# Unit test for function main
def test_main():
    # Create the module object
    module = AnsibleModule(argument_spec = dict(
        enable=dict(type='bool'),
        service=dict(type='str', required=True),
        state=dict(type='str', choices=['started', 'stopped', 'restarted', 'reloaded'], default=None),
        sleep=dict(type='int', default=1),
        pattern=dict(type='str'),
        arguments=dict(type='str', aliases=['args']),
        runlevels=dict(type='list', elements='str'),
        daemonize=dict(type='bool', default=False)
    ))

    # Run the main function
    main()

    # For this test we should not have reached here
    assert False

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:53.756774
# Unit test for function main
def test_main():
    print("here")
    #assert True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:02.241246
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
            daemonize=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )


# Generated at 2022-06-13 06:25:11.512282
# Unit test for function main
def test_main():
    from ansible.module_utils.common.collections import ImmutableDict
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.service import get_sysv_script
    import sys
    import os
    import pytest

    if not sys.version_info.major == 2:
        pytest.skip("'sysvinit' only supports Python 2 right now")

    fixtures = os.path.join(os.path.dirname(__file__), 'fixtures', 'sysvinit')
    sys.modules['ansible.module_utils.basic'] = basic
    sys.modules['ansible.module_utils.service'] = sys
    os.environ['PATH'] = '/bin:/sbin:/usr/bin:/usr/sbin'

   

# Generated at 2022-06-13 06:25:22.257007
# Unit test for function main
def test_main():
    import tempfile
    import shutil
    import ansible.utils
    results = None
    with tempfile.TemporaryDirectory() as tmpdir:
        shutil.copyfile('/bin/sh', tmpdir+'/sh')
        shutil.copyfile('/bin/true', tmpdir+'/true')
        shutil.copyfile('/bin/false', tmpdir+'/false')
        module_args = {
            'name': 'sh',
            'state': 'started',
            'enabled': True
        }
        module_args['daemonize'] = False
        setattr(ansible.utils, '_ANSIBLE_ARGS', '')

# Generated at 2022-06-13 06:25:33.338063
# Unit test for function main
def test_main():
  module = AnsibleModule(
    argument_spec = dict(
      name = dict(required=True, type='str', aliases=['service']),
      state = dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
      enabled = dict(type='bool'),
      sleep = dict(type='int', default=1),
      pattern = dict(type='str'),
      arguments = dict(type='str', aliases=['args']),
      runlevels = dict(type='list', elements='str'),
      daemonize = dict(type='bool', default=False),
    ),
    supports_check_mode=True,
    required_one_of=[['state', 'enabled']],
  )


# Generated at 2022-06-13 06:25:39.514777
# Unit test for function main
def test_main():
  # Test arguments and expected return value.

  import pytest
  #from ansible.module_utils.basic import AnsibleModule
  #my_test_args = []
  #my_test_kwargs = {}
  #my_test_args, my_test_kwargs = None, None
  #my_test_result = main(my_test_args, my_test_kwargs)
  #print my_test_result
  #assert result == my_test_result
  pytest.skip("TODO: write your own tests")

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:46.441841
# Unit test for function main
def test_main():
  # mock inputs
  args = [
  "ansible-playbook",
  "/etc/ansible/roles/ansible.module_utils.service/tests/test_service.yml",
  "-i",
  "/etc/ansible/roles/ansible.module_utils.service/tests/inventory",
  "-vvv",
  "--connection=local",
  "--become",
  "--become-method=su",
  "--become-user=root",
  "--diff"
  ]


# Generated at 2022-06-13 06:27:39.560249
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
        argument_spec = dict(
            name = dict(required=True, type='str', aliases=['service']),
            state = dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled = dict(type='bool'),
            sleep = dict(type='int', default=1),
            pattern = dict(type='str'),
            arguments = dict(type='str', aliases=['args']),
            runlevels = dict(type='list', elements='str'),
            daemonize = dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )

    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:46.517223
# Unit test for function main
def test_main():
    import platform
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
            daemonize=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )
    module.main()
if __name__ == '__main__':
    main

# Generated at 2022-06-13 06:27:47.958024
# Unit test for function main
def test_main():
    main()
# entry point for the module.
# Acts as the main function for unit tests
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:58.453504
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
        ),
        supports_check_mode=True,
        required_one_of=[['state']],
    )
    sysvinit = Sysvinit(module)
    sysvinit.main()

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:11.410838
# Unit test for function main

# Generated at 2022-06-13 06:28:21.329276
# Unit test for function main
def test_main():
    mock_args = ['name=apache', 'state=started']
    mock_ansible = {"check_mode": False, "run_command": os.system}
    with patch.object(sys, 'argv', mock_args):
        with patch.object(AnsibleModule, 'run_command', return_value=(0, "", "")):
            with patch.object(AnsibleModule, '__init__', return_value=None) as mock_module:
                mock_module.params = {'name': 'apache'}
                mock_module.check_mode = False
                main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:31.742922
# Unit test for function main

# Generated at 2022-06-13 06:28:39.165195
# Unit test for function main
def test_main():
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    from action_plugins.actions import main
    # Dummy module
    class Dummy(object):
        def __init__(self):
            self.argument_spec = {}
            self.params = {}

# Generated at 2022-06-13 06:28:49.716731
# Unit test for function main
def test_main():
    data = {
        'arguments': '',
        'enabled': False,
        'name': 'sshd',
        'runlevels': ['3','5'],
        'state': '',
        'sleep': 2,
        'pattern': '',
    }


# Generated at 2022-06-13 06:28:59.429871
# Unit test for function main
def test_main():
    docopt = r'''
Usage:
    sysvinit <name> [--status | --start | --stop | --restart] [--test] [--sleep=<seconds>] [--pattern=<pattern>]
    sysvinit -h

Description:
    Actions to to manage sysv init services
    If no action is provided, status is assumed.

Options:
    --start            Start service
    --stop             Stop service
    --restart          Restart service
    --status           Query service state
    --sleep=<seconds>  Sleep for seconds between start and stop
    --pattern=<pat>    Use <pat> in place of name to determine service status
                        (e.g. to match process name because name is not acurate)
    -h, --help         show this message
    '''
    import doctest
    doctest.test