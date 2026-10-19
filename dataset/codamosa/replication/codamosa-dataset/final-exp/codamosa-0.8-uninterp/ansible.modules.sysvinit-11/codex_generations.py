

# Generated at 2022-06-13 06:21:39.352936
# Unit test for function main
def test_main():
    with mock.patch('ansible.module_utils.basic.AnsibleModule') as mock_module:
        def mock_run_command(module, cmd):
            return (0, '', '')
        mock_module.run_command.side_effect = mock_run_command
        with mock.patch('ansible.module_utils.service.sysv_exists') as mock_sysv_exists:
            mock_sysv_exists.return_value = True
            with mock.patch('ansible.module_utils.service.get_sysv_script') as mock_get_sysv_script:
                mock_get_sysv_script.return_value = '/etc/init.d/foobar'

# Generated at 2022-06-13 06:21:50.574304
# Unit test for function main
def test_main():
    def mock_run_command(module, cmd):
        return (0, '', '')
    def mock_get_bin_path(module, binary, opt_dirs=None):
        return '/bin/' + binary
    class MockModule(object):
        def __init__(self):
            self.params = {
                'name': 'sysvinit_name',
                'state': 'sysvinit_state',
                'enabled': True,
                'sleep': 1,
                'pattern': None,
                'arguments': 'sysvinit_arguments',
                'runlevels': [],
                'daemonize': False
            }
            self.run_command = mock_run_command
            self.get_bin_path = mock_get_bin_path

# Generated at 2022-06-13 06:22:03.945575
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
    main()

# import module snippets
from ansible.module_utils.basic import *

# Generated at 2022-06-13 06:22:16.476590
# Unit test for function main
def test_main():
    # Set return values for test
    module = AnsibleModule(
        argument_spec=dict(
            state=dict(choices=['started', 'stopped', 'restarted'], type='str'),
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
    # Set values for test
    module.params['name'] = 'nginx'
    module.params['enabled'] = 'true'

# Generated at 2022-06-13 06:22:23.926209
# Unit test for function main
def test_main():
    # First test - good service
    a_good_service = dict(
        name="saf",
        state="started",
        enabled=True,
        sleep=1,
        pattern=None,
        arguments=None,
        runlevels=None,
        daemonize=False)
    result = main(a_good_service)
    assert result['status']['started']['changed'] == False
    assert result['status']['enabled']['changed'] == True
    # Second test - bad service
    a_bad_service = dict(
        name="safg",
        state="started",
        enabled=True,
        sleep=1,
        pattern=None,
        arguments=None,
        runlevels=None,
        daemonize=False)
    result = main(a_bad_service)

# Generated at 2022-06-13 06:22:34.106810
# Unit test for function main

# Generated at 2022-06-13 06:22:42.552496
# Unit test for function main
def test_main():
    class AnsibleModule(object):

        def __init__(self):
            self.check_mode = False
            self.service = 'apache'
            self.arguments = {'name': 'apache'}
            self.params = {}


# Generated at 2022-06-13 06:22:53.175859
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
    module.params['name'] = 'postgresql-9.3'

# Generated at 2022-06-13 06:23:04.358501
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

# Generated at 2022-06-13 06:23:06.223448
# Unit test for function main
def test_main():
    main()


###########################################################################

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:01.360626
# Unit test for function main
def test_main():
    test_module = AnsibleModule(
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


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:08.913188
# Unit test for function main
def test_main():
    module_class = AnsibleModule
    module_args = {
        "name": "apache2",
        "daemonize": True,
        "state": "started",
        "enabled": True
    }
    module_instance = AnsibleModule(module_args, module_class)

    sysvinit_instance = sysv(module_instance)

    assert sysvinit_instance.get_sysv_script("apache2") == "/etc/init.d/apache2"


# Generated at 2022-06-13 06:24:14.487201
# Unit test for function main
def test_main():

    # Checks for SysV service
    assert get_sysv_script("apache2") == "/etc/init.d/apache2"

    # Regexp to match service names
    regexp_service_name = re.compile(r'\[[  ]?\d*\]\s{1,2}(?P<name>\w+).*$')

    # Regexp to match runlevels and service names
    regexp_insserv = re.compile(r'^insserv:\s+warning:\s+service\s+(?P<name>\w+)\w+')

    # Regexp to match daemon names in ps
    regexp_ps_params = re.compile(r'^(?P<name>\w+)(?:\.|\s|\[|$)')

    #

# Generated at 2022-06-13 06:24:23.318635
# Unit test for function main
def test_main():
    ActionBase.set_defaults(dict(daemonize=False))
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
    main()



# Generated at 2022-06-13 06:24:35.526854
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
    module.exit_json = lambda **kwargs: kwargs


# Generated at 2022-06-13 06:24:43.793139
# Unit test for function main
def test_main():
    script = '''
        import sys
        import os
        import traceback
        sys.path.insert(0, os.path.join(os.path.dirname(sys.argv[0]), 'ansible'))
        from ansible.module_utils.basic import AnsibleModule
        from ansible.module_utils.action import main
        try:
            result = main()
            print result
            sys.exit(0)
        except Exception as e:
            print "FAILED"
            print "{0}: {1}".format(e.__class__.__name__, e)
            tb = traceback.format_exc()
            print tb
            sys.exit(1)
        '''

# Generated at 2022-06-13 06:24:46.909663
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={},
                           supports_check_mode=True)
    assert main() == None

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:56.473830
# Unit test for function main
def test_main():
    test_dir = os.path.dirname(__file__)
    data_dir = os.path.join(test_dir, '..', 'data')
    data_file = os.path.join(data_dir, 'sysv.data')
    data = json.load(open(data_file))
    results = []
    for data_set in data:
        module = AnsibleModule(argument_spec=data_set[0])
        result = main()
        results.append({'input': data_set[0], 'result': result})
    return results

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:07.661095
# Unit test for function main

# Generated at 2022-06-13 06:25:14.656568
# Unit test for function main
def test_main():
    name = 'apache2'
    state = 'started'
    enabled = True
    runlevels = [3,5]
    pattern = ''
    sleep_for = 0
    rc = 0
    out = err = ''


# Generated at 2022-06-13 06:27:09.620568
# Unit test for function main
def test_main():

    test_fields = {
        "name": "ansible",
        "state": "started",
        "enabled": "yes"
    }

    results = {
        'name': 'ansible',
        'changed': True,
        'status': {}
    }


# Generated at 2022-06-13 06:27:18.993838
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from json import dumps, loads

    module_args = {
        'name': 'apache2',
        'state': 'started',
        'enabled': True
    }


# Generated at 2022-06-13 06:27:25.176860
# Unit test for function main
def test_main():

    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule

    import os

    # test the return values and error handling.
    # This init script doesn't exist so the actions should all fail

# Generated at 2022-06-13 06:27:30.021466
# Unit test for function main
def test_main():
    # Import sysvinit module and mock the module arguments
    sysvinit_m = __import__('ansible.modules.system.sysvinit', fromlist=['ansible', 'modules', 'system'])
    sysvinit_m.params = {
      "state": "started",
      "name": "apache2",
      "enabled": "yes",
    }
    # Mock module object
    sysvinit_m.AnsibleModule = MagicMock()
    sysvinit_m.AnsibleModule.return_value = MagicMock(
        run_command=MagicMock(return_value=(0, '', '')),
        check_mode=False,
        exit_json=MagicMock(),
        fail_json=MagicMock())
    # Mock module 'os' module

# Generated at 2022-06-13 06:27:32.019562
# Unit test for function main
def test_main():
    assert True == True
# entry point
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:39.288683
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
    assert main is not None

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:42.616832
# Unit test for function main
def test_main():

    with pytest.raises(SystemExit) as pytest_wrapped_e:
        main()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:48.497712
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

    main()

# import module snippets
from ansible.module_utils.basic import *
main

# Generated at 2022-06-13 06:27:59.418933
# Unit test for function main
def test_main():
    import os
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

# Generated at 2022-06-13 06:28:03.978785
# Unit test for function main
def test_main():

    # func requires: name, state, enabled, runlevels, pattern, sleep, rc, out, err

    assert None == None


if __name__ == '__main__':
    main()