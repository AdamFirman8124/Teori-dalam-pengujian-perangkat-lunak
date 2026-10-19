

# Generated at 2022-06-13 06:21:39.395591
# Unit test for function main
def test_main():
    #import sys
    #from ansible.module_utils import basic
    #from ansible.module_utils.basic import AnsibleModule
    moduleArgs = {}
    moduleArgs.update(YAML_ARGS)

    module = AnsibleModule(
        argument_spec=moduleArgs,
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )

    module.exit_json(**main())



# Generated at 2022-06-13 06:21:40.944828
# Unit test for function main
def test_main():
    print('Test passed!')
    return True

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:21:50.815416
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

# Generated at 2022-06-13 06:22:04.264560
# Unit test for function main
def test_main():
    print("testing")
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

# Entry point for unit test

# Generated at 2022-06-13 06:22:13.078555
# Unit test for function main
def test_main():
    data = {
        'name': 'apache2',
        'state': '',
        'enabled': True
    }

# Generated at 2022-06-13 06:22:22.702718
# Unit test for function main
def test_main():
    # mocks
    class MockModule(object):
        def __init__(self, *args, **kwargs):
            self.params = kwargs

            self.check_mode = kwargs.get('check_mode', False)
            self.fail_json = self.exit_json = lambda **kwargs: kwargs

            self.warnings = []
            def warn(msg):
                self.warnings.append(msg)
                print(msg)
            self.warn = warn

        def get_bin_path(self, binary, opt_dirs=[]):
            return {'update-rc.d': '', 'chkconfig': '', 'service': ''}.get(binary, None)

        def run_command(self, command):
            if self.check_mode:
                return 0, "", ""

           

# Generated at 2022-06-13 06:22:23.677279
# Unit test for function main
def test_main():
    print('TEST MODULE')


# Generated at 2022-06-13 06:22:24.291805
# Unit test for function main
def test_main():
    assert 1 == 0

# Generated at 2022-06-13 06:22:27.612211
# Unit test for function main
def test_main():
    # Description: Unit test for function main
    # Import pdb; pdb.set_trace()
    # Return:
    pass


# Generated at 2022-06-13 06:22:35.611720
# Unit test for function main
def test_main():
    # mock module parameter and AnsibleModule instance
    module = AnsibleModule(name='sysvinit', state='restarted', enabled=True, daemonize=True, check_mode=True)

    def mock_run_command(cmd):
        return (0, 'ok', '')

    def mock_get_bin_path(binary, opt_dirs=None):
        return '/bin/' + binary

    def mock_sysexists(name):
        return True

    # NOTE: not using mock module as it doesn't work with a list of modules/imports
    module.run_command = mock_run_command
    module.get_bin_path = mock_get_bin_path
    module.sysexists = mock_sysexists

    result = main()
    assert result.get('status').get('restarted').get('changed')

# Generated at 2022-06-13 06:23:33.261239
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

# Generated at 2022-06-13 06:23:42.117190
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

# Generated at 2022-06-13 06:23:52.687385
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from sys import version_info
    if version_info[0] < 3:
        from StringIO import StringIO
    else:
        from io import StringIO


# Generated at 2022-06-13 06:24:00.091190
# Unit test for function main
def test_main():
    from ansible.module_utils.ansible_report_plugins.argspec import argspec
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.service import get_ps, daemonize
    import sys
    import os
    import unittest
    import re
    import io
    import sysvinit
    import tempfile, os
    import unittest.mock as mock

    class FakeModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
            self.check_mode = False
        def fail_json(self, **kwargs):
            raise Exception(kwargs)
        def exit_json(self, **kwargs):
            pass
        def get_bin_path(self):
            pass
            pass

# Generated at 2022-06-13 06:24:12.328275
# Unit test for function main
def test_main():
    path = os.path.dirname(os.path.realpath(__file__))
    data_path = os.path.join(path, '_data')

    class args:
        name = ''
        state = ''
        enabled = ''
        sleep = ''
        pattern = ''
        arguments = ''
        runlevels = ''
        daemonize = ''

    def get_bin_path(binary, opt_dirs=[]):
        return os.path.join(args.binary_path, binary)

    def run_command(cmd, daemonize=False):
        print(cmd)
        if cmd == 'service apache2 status':
            return (0, 'apache2 dead but pid file exists', '')

        _, output = commands.getstatusoutput(cmd)
        return (0, output, '')


# Generated at 2022-06-13 06:24:21.864552
# Unit test for function main
def test_main():
    # Mock module arguments
    module_args = {}
    module_args.update(dict(name='apache2'))
    module_args.update(dict(state='started'))
    module_args.update(dict(enabled=True))
    # Construct the parameter string in the format module expects
    # arguments = {}
    # for key, val in module_args.iteritems():
    #     if val is not None:
    #         arguments[key] = val
    # from ansible.module_utils.basic import AnsibleModule
    # module = AnsibleModule(
    #     argument_spec=dict(
    #         name=dict(required=True, type='str', aliases=['service']),
    #         state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),


# Generated at 2022-06-13 06:24:29.316013
# Unit test for function main
def test_main():
    import sys
    import AnsibleModule

    for arg in sys.argv:
        if "--test_main" in arg:
            test_args = dict(
              name="apache2",
              state="started",
              enabled=True,
              sleep=1,
              pattern="",
              arguments="",
              runlevels=[],
              daemonize=False,
            )
            module = AnsibleModule(argument_spec=test_args)
            main()


if __name__ == '__main__':
    main()
    # test_main()

# Generated at 2022-06-13 06:24:40.322135
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
    assert main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:52.270063
# Unit test for function main
def test_main():
    import sys
    from ansible.module_utils.basic import AnsibleModule

    test_args = [
        '-s',
        '-v',
        '-i', 'hosts',
        '--args', '-r', '--daemonize'
    ]

    sys.argv = [sys.argv[0]] + test_args


# Generated at 2022-06-13 06:24:56.794374
# Unit test for function main
def test_main():
    runMe = main
    name = "example"
    state = "started"
    enabled = True
    sleep = 1
    pattern = None
    arguments = None
    runlevels = ["3","5"]

    # example of mocking the module
    class MockModule(object):
        def __init__(self, **kwargs):
            self.params = kwargs
        def fail_json(self, **kwargs):
            assert False
        def get_bin_path(self, *args, **kwargs):
            assert False
        def run_command(self, *args, **kwargs):
            assert False
        def exit_json(self, **kwargs):
            # assert False
            pass
        def warn(self, **kwargs):
            # assert False
            pass

# Generated at 2022-06-13 06:26:54.105941
# Unit test for function main
def test_main():
    # unit tests
    import sys
    import json

    def check_results(module, x):
        results = json.loads(module.exit_json.__self__.result)
        if not results.get('changed') == x:
            sys.exit(1)

    main_args = ['service', 'state']

    module = AnsibleModule(argument_spec={})  # noqa
    module.params.update(dict(
        name='my_service',
        state='started',
        enabled=True,
        sleep=1,
        pattern='',
        arguments='',
        runlevels=['1', '2'],
        daemonize=False,
    ))

    import ansible_collections.notstdlib.moveitallout.tests.unit.compat.mock as mock

# Generated at 2022-06-13 06:27:04.439059
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec={
            'name': {'required': True, 'type': 'str'},
            'state': {'choices': ['started', 'stopped'], 'type': 'str'},
            'enabled': {'type': 'bool'},
        },

    )

    sysvinit_iut = SysvinitModule(module)
    rc, out, err = sysvinit_iut.main(module.params)

    assert rc == 0
    assert out == "Python"
    assert err == "Errors"

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:15.469496
# Unit test for function main
def test_main():
    """ Unit test for function main. """
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

# Generated at 2022-06-13 06:27:22.404966
# Unit test for function main
def test_main():
    # Test case object
    class AnsibleModuleMock(object):
        def __init__(self):
            self.params = {
                'name': 'apache2',
                'state': None,
                'enabled': None,
                'sleep': 1,
                'pattern': None,
                'runlevels': ['3'],
                'daemonize': False
            }
        # run_commands
        def run_command(self, cmd):
            if cmd == 'update-rc.d apache2 disable':
                return 0, '', ''
            elif cmd == 'update-rc.d apache2 enable 3':
                return 0, '', ''
            elif cmd == 'update-rc.d apache2 enable':
                return 0, '', ''

# Generated at 2022-06-13 06:27:34.059406
# Unit test for function main
def test_main():
    argv = [
        'service=testservice',
        'state=started',
        'enabled=yes',
        'runlevels=3,5',
        'daemonize=no',
    ]

    from ansible.module_utils.basic import AnsibleModule

# Generated at 2022-06-13 06:27:36.841540
# Unit test for function main
def test_main():

    # Test with service created and expected to be enabled (True)
    out = main()
    assert out['changed'] == True
    assert out['state'] == 'started'
    assert out['enabled'] == True


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:52.614208
# Unit test for function main
def test_main():

    # Mock module
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

    # Mock module parameters

# Generated at 2022-06-13 06:28:00.909138
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
    def runme(doit):
        args = module.params['arguments']

# Generated at 2022-06-13 06:28:13.506134
# Unit test for function main
def test_main():
    import json

    # AssertionError: 'foo' == {'foo': 'bar'} : False is not true
    # with pytest.raises(AssertionError) as pytest_wrapped_e:
    #     main()

    # assert pytest_wrapped_e.type == AssertionError

    # -------------------------------------------------------
    # add the missing params for main() to the test_module dict

    test_module = dict(
        name='test_module',
        state='test_module',
        enabled='test_module',
        sleep='test_module',
        pattern='test_module',
        arguments='test_module',
        runlevels='test_module',
        daemonize='test_module',
    )

    # -----------------------------------------------------------
    #
    #

# Generated at 2022-06-13 06:28:14.158142
# Unit test for function main
def test_main():
    pass