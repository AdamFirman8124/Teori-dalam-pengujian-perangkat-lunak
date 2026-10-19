

# Generated at 2022-06-13 06:21:36.105520
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils._text import to_bytes

    def fail_if_missing(module, *args, **kwargs):
        res = sysv_exists(*args, **kwargs)
        if not res:
            module.fail_json(msg="Service {} not found".format(*args))


    def get_ps_output(module):
        p = subprocess.Popen(['ps', '-A', '-o', 'args'], stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        if p.returncode != 0:
            print("Failed to get ps output with status code : {}".format(p.returncode))
            return []
        return

# Generated at 2022-06-13 06:21:45.037398
# Unit test for function main

# Generated at 2022-06-13 06:21:52.708731
# Unit test for function main
def test_main():
    dummy_args = ['/bin/ansible-playbook', '/path/to/playbook.yml']
    test_args = [{
        'name': 'test_name',
        'state': 'test_state',
        'enabled': 'test_enabled',
        'sleep': 'test_sleep',
        'pattern': 'test_pattern',
        'arguments': 'test_arguments',
        'runlevels': 'test_runlevels',
        'daemonize': 'test_daemonize',
    }]
    module = AnsibleModule(argument_spec={})
    module.exit_json = exit_json
    main()


# Generated at 2022-06-13 06:22:05.480108
# Unit test for function main
def test_main():

    module = AnsibleModule(
        argument_spec=dict(
            name=dict(type='str', aliases=['service']),
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

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:15.969694
# Unit test for function main
def test_main():
    """
    Unit test for action_main
    :return: void
    """
    import os
    import shutil
    import tempfile
    import sys
    from ansible.module_utils.service import *

    # Create temporary files
    tempdir = tempfile.mkdtemp(dir='/tmp')
    fa = open(os.path.join(tempdir, 'file1'), 'w+')
    fa.close()

    # Run the main function
    test_data = {
        'name': 'apache2',
        'state': 'started',
        'enabled': True
    }
    main(test_data)
    # Remove temporary files
    shutil.rmtree(tempdir)

# Generated at 2022-06-13 06:22:27.925013
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec = dict(
            name = dict(required=True, type='str'),
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

    name = module.params['name']
    action = module.params['state']
    enabled = module.params['enabled']

# Generated at 2022-06-13 06:22:35.823673
# Unit test for function main
def test_main():
    fake_stdin = FakeAnsibleModule(
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
    # Test with all params set

# Generated at 2022-06-13 06:22:46.723312
# Unit test for function main
def test_main():
    import json
    import argparse
    from ansible.module_utils import basic
    from ansible.module_utils.common.collections import ImmutableDict
    parser = argparse.ArgumentParser()
    parser.add_argument('--params', '--extra-vars', dest='params', action='store', help='JSON Parameters')
    parser.add_argument('--ansible-module-args', dest='ansible_module_args', action='store', help='JSON Parameters')
    args = parser.parse_args()
    all_params = json.loads(args.params)
    ansible_module_args = json.loads(args.ansible_module_args)
    ansible_module_args_dict = ImmutableDict(ansible_module_args)

# Generated at 2022-06-13 06:22:57.689800
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

# Generated at 2022-06-13 06:23:00.522865
# Unit test for function main
def test_main():
    # calling without required args will fail
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 0

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:53.152163
# Unit test for function main
def test_main():
    
    out = None
    rc = 0
    
    if runme:
        out = runme.main()
    elif runme_module:
        runme_module.main()
    else:
        rc = 1
    
    sys.exit(rc)

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 06:24:00.555274
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

# Generated at 2022-06-13 06:24:12.378361
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
            daemonize=dict(type='bool', default=False)
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:21.904358
# Unit test for function main
def test_main():

    # first, we try with three different versions of real init scripts.  we can't unit test
    # the real init scripts, of course, but at least this shows how to test with multiple
    # versions at once.

    # Note: the output of the init scripts are standardized and stored in the tests/output
    # directory.  If you modify the script, make sure to update the output.
    # Note2: the output is captured on stdout and stderr, since the (correct) output
    # needs to be read from stderr.  We modify the error output slightly to make it
    # useful in both Python 2 and 3.
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.service import sysv_is_enabled
    import os
    import shutil

    # We start by loading up our test data.

# Generated at 2022-06-13 06:24:32.828285
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


# Generated at 2022-06-13 06:24:41.368944
# Unit test for function main
def test_main():
    tests = ['{ "name": "foo", "state": "started", "enabled": yes }']
    results = [{"status": {"enabled": {"changed": False, "stderr": "", "stdout": ""}, "started": {"changed": False, "stderr": "", "stdout": ""}}, "attempts": 1, "changed": False, "name": "foo"}]

# Generated at 2022-06-13 06:24:53.249952
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
    res = main()

# import module snippets
from ansible.module_utils.basic import *

# Generated at 2022-06-13 06:24:56.693500
# Unit test for function main
def test_main():
    try:
        main()
    except SystemExit as inst:
        if inst.args[0] == 0:
            return
        raise

if __name__ == '__main__':
    test_main()

# Generated at 2022-06-13 06:25:03.823782
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

# Generated at 2022-06-13 06:25:12.523375
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.service import sysv_exists
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils._text import to_text
    import os

    try:
        os.mkfifo('/tmp/service_test')
    except:
        pass

    scriptname = '/tmp/service_test'

    def sysv_exists_mock(name):
        if name == 'service_test':
            return scriptname
        if name == 'service_test_no_script':
            return ''

    basic._ANSIBLE_ARGS = None

# Generated at 2022-06-13 06:27:12.622322
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

# Generated at 2022-06-13 06:27:20.854390
# Unit test for function main
def test_main():
    # Mock up sys.modules
    module_mock = {}
    if 'sys' in sys.modules:
        module_mock['sys'] = sys.modules['sys']
    module_mock['sys.modules'] = sys.modules
    module_mock['sys.modules']['ansible'] = MagicMock()
    module_mock['sys.modules']['ansible.module_utils'] = MagicMock()
    module_mock['sys.modules']['ansible.module_utils.basic'] = MagicMock()
    module_mock['sys.modules']['ansible.module_utils.basic'].AnsibleModule = MagicMock(return_value=Mock(ansible_module=True))

# Generated at 2022-06-13 06:27:32.910233
# Unit test for function main
def test_main():
    main()

# import module snippets
from ansible.module_utils.basic import *
main = AnsibleModule(
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

# Generated at 2022-06-13 06:27:41.735081
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

# Generated at 2022-06-13 06:27:55.226877
# Unit test for function main
def test_main():
    test_host = 'localhost'
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
    action = module

# Generated at 2022-06-13 06:28:08.352666
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

# Generated at 2022-06-13 06:28:20.717055
# Unit test for function main
def test_main():
    # Test module
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

# Generated at 2022-06-13 06:28:31.277320
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={
        'name': {'required': True, 'type': 'str', 'aliases': ['service']},
        'state': {'choices': ['started', 'stopped', 'restarted', 'reloaded'], 'type': 'str'},
        'enabled': {'type': 'bool'},
        'sleep': {'type': 'int', 'default': 1},
        'pattern': {'type': 'str'},
        'arguments': {'type': 'str', 'aliases': ['args']},
        'runlevels': {'type': 'list', 'elements': 'str'},
        'daemonize': {'type': 'bool', 'default': False},
    }
    )

    module.check_mode = False
    module.params = {}

# Generated at 2022-06-13 06:28:45.232142
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

    import sys, os

# Generated at 2022-06-13 06:28:52.819056
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.service import sysv_is_enabled, get_sysv_script, sysv_exists, fail_if_missing, get_ps, daemonize
