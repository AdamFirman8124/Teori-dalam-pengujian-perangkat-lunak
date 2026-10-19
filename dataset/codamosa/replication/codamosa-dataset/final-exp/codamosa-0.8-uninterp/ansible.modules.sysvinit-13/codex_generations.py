

# Generated at 2022-06-13 06:21:38.350544
# Unit test for function main
def test_main():
    assert True

# Collect all test cases in this file

# Generated at 2022-06-13 06:21:47.457182
# Unit test for function main
def test_main():
    param_json = r'''{
        "arguments": null,
        "changed": false,
        "daemonize": false,
        "enabled": null,
        "runlevels": null,
        "sleep": 1,
        "state": null,
        "status": {},
        "name": "testing"
    }'''
    from ansible.module_utils import basic
    from sys import argv
    from ansible.module_utils.service import get_sysv_script
    def mock_get_sysv_script(name):
        return "some/path/some_script"
    def mock_sysv_exists(name):
        return True
    def mock_sysv_is_enabled(name, runlevel):
        return True


# Generated at 2022-06-13 06:21:58.986530
# Unit test for function main
def test_main():
    import sys
    import os
    import json

    test_failures = []

    test_values = {
        'name': 'dummy',
        'state': 'started',
        'enabled': True,
        'sleep': 5,
        'pattern': 'dummy',
        'arguments': 'dummy',
        'runlevels': ['1', '5'],
        'daemonize': True
    }

    test_args = []
    for key in test_values:
        test_args.append("--%s=%s" % (key, test_values[key]))

    def test_out(rc, out, err):

        if not out:
            test_failures.append("Output missing")

        return (rc, out, err)


# Generated at 2022-06-13 06:22:09.883377
# Unit test for function main
def test_main():
    args = {"enabled": True, "name": "ser1", "state": "started",
    "sleep": 1, "arguments": "ser1", "runlevels": ["ser1"],
    "daemonize": False}
    module = AnsibleModule(argument_spec=dict(
        name=dict(required=True, type='str', aliases=['service']),
        state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
        enabled=dict(type='bool'),
        sleep=dict(type='int', default=1),
        pattern=dict(type='str'),
        arguments=dict(type='str', aliases=['args']),
        runlevels=dict(type='list', elements='str'),
        daemonize=dict(type='bool', default=False),
        ))

# Generated at 2022-06-13 06:22:21.461603
# Unit test for function main
def test_main():
    # Make sure we create a module
    module =  sys.modules[__name__]
    module.run_command = lambda x, check_rc=True: (0, 'stdout', 'stderr')
    module.fail_json = lambda x: sys.exit(1)
    module.exit_json = lambda x, **kw: sys.exit(0)
    module.get_bin_path = lambda x: '/bin/' + x
    module.check_mode = False
    # Make sure we have arguments to play with

# Generated at 2022-06-13 06:22:25.796283
# Unit test for function main
def test_main():
    test_args = {
        "name": "httpd",
        "state": "started",
    }
    _result = main(AnsibleModule(**test_args))

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:34.739230
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
    setattr(module, 'run_command', run_command)

# Generated at 2022-06-13 06:22:46.468522
# Unit test for function main
def test_main():
    test_args = {'name': 'foo', 'enabled': None, 'state': 'restarted', 'sleep': 1, 'pattern': None, 'arguments': None, 'runlevels': None, 'daemonize': False}
    if 'check_mode' in test_args.keys(): del test_args['check_mode']

# Generated at 2022-06-13 06:22:48.265053
# Unit test for function main
def test_main():
    args = dict(
        name="apache2",
        enabled=False,
    )
    assert main(args) == True


# Generated at 2022-06-13 06:22:51.811010
# Unit test for function main
def test_main():
    m = service.sysvinit("/var/empty/ansible")
    state = {
        "name": "ansible",
        "state": "started",
        "enabled": True
    }
    m.run(**state)

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:50.287222
# Unit test for function main
def test_main():
    argument_spec = dict(
        name=dict(required=True, type='str', aliases=['service']),
        state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
        enabled=dict(type='bool'),
        sleep=dict(type='int', default=1),
        pattern=dict(type='str'),
        arguments=dict(type='str', aliases=['args']),
        runlevels=dict(type='list', elements='str'),
        daemonize=dict(type='bool', default=False),
    )
    module_args = dict(name='apache2',enabled=True)
    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    runlevels = []

# Generated at 2022-06-13 06:23:58.218641
# Unit test for function main
def test_main():
    """Unit tests for module function main."""
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
    # TODO: Unit test without try/except/

# Generated at 2022-06-13 06:24:09.584075
# Unit test for function main
def test_main():

    import unittest
    import sys
    import re

    # add fake path for imports
    sys.path.insert(0,'/usr/local/lib/python3.6/dist-packages/ansible/module_utils')
    from ansible.module_utils.basic import *

    # Non-LSB defaults for testing
    defaults = {
        "chkconfig": [
            "--list"
        ],
        "update-rc.d": [
            "--list"
        ]
    }

    # mocked data returned in check_mode

# Generated at 2022-06-13 06:24:19.567886
# Unit test for function main
def test_main():
    input_args = dict(
            name='foo',
            state='started',
            enabled=False,
            sleep=1,
            pattern=None,
            arguments=None,
            runlevels=None,
            daemonize=False
            )


# Generated at 2022-06-13 06:24:29.260012
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

    ###########################################################################
    # BEGIN: Disable

    # Assign test case variables

# Generated at 2022-06-13 06:24:40.321485
# Unit test for function main
def test_main():
    import sys
    import os
    import json

    testArgs = {
        'name': 'ntp',
        'state': 'started',
        'enabled': True,
        'sleep': 2,
        'pattern': None,
        'arguments': '',
        'runlevels': ['3', '5'],
    }
    with open(os.devnull, "w") as devnull:
        with open("/tmp/test.json", 'w') as results:
            sys.stdout = results
            try:
                main()
            except SystemExit:
                pass
            except:
                raise

            sys.stdout = devnull

    with open("/tmp/test.json", 'r') as tmpFile:
        tmpJson = json.loads(tmpFile.read())


# Generated at 2022-06-13 06:24:52.281091
# Unit test for function main
def test_main():
    import json
    import os
    import sys
    import unittest

    # import the module here
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))
    import ansible.module_utils.basic as basic
    sys.path.append(os.path.join(os.path.dirname(basic.__file__), '../../'))
    import ansible.modules.system.sysvinit as sysvinit

    # This is the current module object we are using
    module = sysvinit



# Generated at 2022-06-13 06:25:01.490470
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

    class MockModule(object):
        def __init__(self):
            return


# Generated at 2022-06-13 06:25:03.791263
# Unit test for function main
def test_main():
    output = main()
    assert output != 'Failed to reload service: apache2'

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:25:12.503516
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

    # run function
    main()

if __name__ == '__main__':
    main

# Generated at 2022-06-13 06:27:15.338646
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
    )
    name = 'sshd'
    action = 'started'
    enabled = True
    runlevels = None
    pattern = None
    sleep_for = 1
    rc = 0

# Generated at 2022-06-13 06:27:22.681905
# Unit test for function main
def test_main():
    # Testing module with arguments and options
    module = AnsibleModule(
        argument_spec = dict(
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

    # Fail the module if script for service not found

# Generated at 2022-06-13 06:27:24.333322
# Unit test for function main
def test_main():
    return 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:35.171100
# Unit test for function main
def test_main():

    mod = AnsibleModule(
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
    try:
        main()
    except AnsibleError as e:
        mod.fail_json

# Generated at 2022-06-13 06:27:50.679461
# Unit test for function main
def test_main():
    function_name = 'main'
    REQUIRED_PARAMS = ['name']
    OPTIONAL_ONE_OF = [['state', 'enabled']]

# Generated at 2022-06-13 06:28:00.100890
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
            enabled=dict(type='bool'),
            sleep=dict(type='int', default=1),
            arguments=dict(type='str', aliases=['args']),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )

    name = module.params['name']
    action = module.params['state']
    enabled = module.params['enabled']
    sleep_for = module.params['sleep']
    rc = 0
    out = err = ''

# Generated at 2022-06-13 06:28:03.208484
# Unit test for function main
def test_main():
    # FIXME: Error case(s)
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:14.882865
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


# Generated at 2022-06-13 06:28:24.702404
# Unit test for function main
def test_main():
    args = dict(
        name=dict(required=True, type='str', aliases=['service']),
        state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
        enabled=dict(type='bool'),
        sleep=dict(type='int', default=1),
        pattern=dict(type='str'),
        arguments=dict(type='str', aliases=['args']),
        runlevels=dict(type='list', elements='str'),
        daemonize=dict(type='bool', default=False),
    )
    module = AnsibleModule(
        argument_spec=args,
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )
    main()
if __name__ == '__main__':
    main

# Generated at 2022-06-13 06:28:34.540960
# Unit test for function main
def test_main():
    out = None
    err = None
    rc = None
    argv = None
    argv = ["/usr/bin/ansible-test",
           "--debug",
           "--platform",
           "posix",
           "/usr/lib/python3.7/site-packages/ansible/modules/system/sysvinit.py"]

    try:
        out = StringIO()
        sys.stdout = out

        err = StringIO()
        sys.stderr = err

        rc = sysvinit.main()
        sys.stdout.getvalue()
        sys.stderr.getvalue()
    finally:
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    return (rc, out, err)