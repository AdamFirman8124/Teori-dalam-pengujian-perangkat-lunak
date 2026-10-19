

# Generated at 2022-06-13 06:21:44.166740
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

# Generated at 2022-06-13 06:21:50.828340
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )

    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:04.264081
# Unit test for function main
def test_main():
    import sys
    import os

    argv = ['']
    argv.extend([
        "name=sysvinit",
        "state=started",
        "enabled=yes"
    ])
    # Mock return value for module.fail_json
    def fail_json(msg, **kwargs):
        print(msg)
        sys.exit(1)
    # Mock return value for module.run_command
    def run_command(cmd, **kwargs):
        if cmd == "command -v service":
            return 0, "/usr/bin/service", ""
        if cmd == "command -v update-rc.d":
            return 0, "/usr/sbin/update-rc.d", ""
        if cmd == "command -v chkconfig":
            return 1, "", ""

# Generated at 2022-06-13 06:22:05.959803
# Unit test for function main
def test_main():
    pass


# import module snippets
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:09.509340
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    if not basic.HAS_PSUTIL:
        raise Exception('The `psutil` python module is not importable. Check the requirements.')
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:21.204631
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import ansible.module_utils.sysvinit
    import ansible.module_utils.service
    from ansible.module_utils.service import sysv_is_enabled, get_sysv_script, sysv_exists
    from ansible.module_utils.service_facts import  get_ps
    from ansible.module_utils.common._collections_compat import Mapping

    # run as __main__

# Generated at 2022-06-13 06:22:26.263952
# Unit test for function main
def test_main():
    import sys
    args = ['--name', 'test_name', '--state', 'test_state']
    if sys.argv[1:] == args:
        print("This code is called during unit tests.")
        return
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:35.052905
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

# Generated at 2022-06-13 06:22:46.601697
# Unit test for function main
def test_main():

    # Content of mocked module.params
    module_params = dict(
        name='apache2',
        state='stopped',
        enabled=True,
        sleep=2,
        pattern=False,
        arguments='',
        runlevels=None,
        daemonize=False,
    )

    # Content of results from mocked ansible module.
    result = dict(
        ansible_facts=dict(
            ansible_check_mode=False,
            ansible_diff_mode=False,
        ),
        changed=True,
        content=['This is a test'],
        **module_params
    )

    # Mock framework as per https://docs.ansible.com/ansible/devel/dev_guide/developing_modules_general.html#unit-testing
    # Test passes if executed successfully and not calling sys.

# Generated at 2022-06-13 06:22:57.553513
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required = True, type = 'str', aliases = ['service']),
            state = dict(choices = ['started', 'stopped', 'restarted', 'reloaded'], type = 'str'),
            enabled = dict(type = 'bool'),
            sleep = dict(type = 'int', default = 1),
            pattern = dict(type = 'str'),
            arguments = dict(type = 'str', aliases = ['args']),
            runlevels = dict(type = 'list', elements = 'str'),
            daemonize = dict(type = 'bool', default = False),
        ),
        supports_check_mode = True,
        required_one_of = [['state', 'enabled']],
    )

    module.exit_json(changed=False)



# Generated at 2022-06-13 06:23:54.878088
# Unit test for function main
def test_main():
    global rc
    global out
    global err
    global location
    global is_started
    global enablers
    global name
    global sleep_for
    global worked
    global script
    global action
    global enabled
    global runlevel_status
    global runlevels
    global pattern
    ###########################################################################
    global module

# Generated at 2022-06-13 06:24:01.758309
# Unit test for function main
def test_main():
    #import ansible_sysvinit
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

# Generated at 2022-06-13 06:24:13.174331
# Unit test for function main
def test_main():
    module = AnsibleModule(dict(
        name=dict(required=True, type='str', aliases=['service']),
        state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
        enabled=dict(type='bool'),
        sleep=dict(type='int', default=1),
        pattern=dict(type='str'),
        arguments=dict(type='str', aliases=['args']),
        runlevels=dict(type='list', elements='str'),
        daemonize=dict(type='bool', default=False),
    ), check_invalid_arguments=False, supports_check_mode=True, required_one_of=[['state', 'enabled']])

    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:18.311170
# Unit test for function main
def test_main():
    result = {}
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
    module.params['name'] = 'apache2'

# Generated at 2022-06-13 06:24:26.009212
# Unit test for function main
def test_main():
    import ansible.module_utils.service as service
    import ansible.module_utils.basic as basic
    from ansible.module_utils.action import AnsibleAction
    from ansible.module_utils.ansible_lint import AnsibleLintRule
    import sysvinit_spec
    import imp
    import os

    def dummy_exist():
        return True
    def dummy_script():
        return "/path/to/script"
    def dummy_enabled():
        return True
    def dummy_not_enabled():
        return False
    def dummy_fail_missing(module, condition, name):
        return True

    path = os.path.dirname(sysvinit_spec.__file__)

# Generated at 2022-06-13 06:24:36.417280
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str'),
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
main()

# Generated at 2022-06-13 06:24:37.846483
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:45.127342
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

    # Mock the choices for argument_spec

# Generated at 2022-06-13 06:24:56.736934
# Unit test for function main
def test_main():
    '''
    sysvinit unit test function
    '''
    # Mock Function
    def mock_get_ps(mock_module, pattern):
        '''
        Fake get_ps function used in main()
        '''
        return True

    def mock_sysv_exists(service):
        '''
        Fake sysv_exists function used in main()
        '''
        return True

    def mock_sysv_is_enabled(service, runlevel=None):
        '''
        Fake sysv_is_enabled function used in main()
        '''
        return True

    def mock_get_sysv_script(service):
        '''
        Fake get_sysv_script function used in main()
        '''
        return True


# Generated at 2022-06-13 06:25:07.939170
# Unit test for function main
def test_main():
    # unit test
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
    )

    name = module.params['name']
    action = module.params['state']
    enabled = module.params['enabled']
    runlevels = module.params['runlevels']
    pattern = module.params['pattern']
    sleep_for = module

# Generated at 2022-06-13 06:27:06.933388
# Unit test for function main
def test_main():
    test_args = {
        'name': 'test_name',
        'pattern': 'test_pattern'
    }
    test_modules_args = {
        'check_mode': True,
        'run_command': 'ansible.module_utils.basic.run_command',
    }
    test_exit_args = {'rc':1, 'stdout':'test_stdout', 'stderr':'test_stderr'}
    test_run_command_res = (1, 'test_stdout', 'test_stderr')
    def run_command_mock(self, cmd, daemonize):
        return test_run_command_res

# Generated at 2022-06-13 06:27:17.438994
# Unit test for function main
def test_main():
    my_module = AnsibleModule(
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
    my_module.main()


# Generated at 2022-06-13 06:27:19.965940
# Unit test for function main
def test_main():
    args = dict(
        name="apache2",
        action="status"
    )

    with pytest.raises(SystemExit):
        main(args)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:32.560410
# Unit test for function main
def test_main():
    # Test dependencies
    from ansible.module_utils import basic
    global get_ps
    get_ps = basic.AnsibleModule.get_bin_path

    # Import and mock
    import os
    import sys
    import inspect
    import mock
    import ansible.module_utils.service as service
    global sysv_exists
    global sysv_is_enabled
    global get_sysv_script
    global fail_if_missing

    sys.modules['service'] = service

    # Reload module
    global main
    reload(sys.modules[__name__])
    main = sys.modules[__name__].main

    # Test 1 - Everything right

# Generated at 2022-06-13 06:27:39.633975
# Unit test for function main
def test_main():
   args = {}
   args['name'] = 'service'
   args['state'] = 'stopped'
   args['enabled'] = True
   args['sleep'] = 1
   args['pattern'] = None
   args['arguments'] = 'stop'
   args['runlevels'] = None
   args['daemonize'] = False
   args['check_mode'] = True
   args['diff_mode'] = False
   args['platform'] = 'posix'
   args['action'] = None
   args['stdout'] = True
   args['stdout_lines'] = True
   args['stderr'] = True
   args['stderr_lines'] = True
   args['rc'] = None
   args['warnings'] = False
   args['invocation'] = None
   args['no_log'] = False
   args

# Generated at 2022-06-13 06:27:46.572842
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.service import sysv_is_enabled, get_sysv_script, sysv_exists, fail_if_missing, get_ps, daemonize
    from ansible.module_utils._text import to_text
    from ansible.module_utils.action import ActionBase
    import json, os, shutil, tempfile

    # Add temp dir to path so fixtures can be copied to it
    test_dir = os.path.dirname(__file__)
    tmpdir = tempfile.mkdtemp()
    sys.path.append(tmpdir)

    # Make fixtures available
    shutil.copytree(os.path.join(test_dir, 'fixtures'),
                    os.path.join(tmpdir, 'fixtures'))


# Generated at 2022-06-13 06:27:47.550620
# Unit test for function main
def test_main():
    assert main() is None

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:59.290417
# Unit test for function main
def test_main():
    name = 'foo'
    runlevels = ['3', '5']
    script = '/etc/init.d/apache2'
    state= 'started'
    args = '.'
    location = {'chkconfig': '/sbin/chkconfig'}
    result = {
        'changed' : False,
        'name' : name,
        'status' : {},
        'results' : {
            'enabled' : {
                'changed' : False,
                'rc' : None,
                'stdout' : None,
                'stderr' : None
            }
        }
    }
    # test when enabled isn't in the runlevels
    assert result == main(name, state, False, runlevels, None, args, location)
    # test when enabled isn't in the runlevels and action is stop

# Generated at 2022-06-13 06:28:12.003180
# Unit test for function main
def test_main():
    import ansible.module_utils.service
    import ansible.module_utils.basic
    import ansible.module_utils.six
    import sys
    import os
    import mock
    module_args = {
        'name': 'foo',
        'state': 'restarted'
    }


# Generated at 2022-06-13 06:28:23.243707
# Unit test for function main
def test_main():
    test1_args = dict(
        state='started',
        enabled=True,
        sleep=1,
        pattern='nginx',
        arguments='',
        runlevels=['runlevel1'],
        daemonize=False
    )

    test1_output1 ={
      "attempts": 1,
      "changed": True,
      "name": "apache2",
      "status": {
        "enabled": {
            "changed": True,
            "rc": 0,
            "stdout": "",
            "stderr": ""
        },
        "stopped": {
            "changed": True,
            "rc": 0,
            "stdout": "Stopping web server: apache2.\n",
            "stderr": ""
        }
      }
    }

    test1_