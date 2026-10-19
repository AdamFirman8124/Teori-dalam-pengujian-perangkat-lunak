

# Generated at 2022-06-13 06:21:39.013158
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

    class AnsibleExitJson(Exception):
        pass

# Generated at 2022-06-13 06:21:50.375543
# Unit test for function main
def test_main():
    # The following variables will be defined during unit test
    name = 'testservice'
    action = 'testaction'
    enabled = 'testenabled'
    runlevels = 'testrunlevels'
    pattern = 'testpattern'
    sleep_for = 'testsleep'
    rc = 'testrc'
    out = 'testout'
    err = 'testerr'
    result = 'testresult'
    module = 'testmodule'
    script = 'testscript'
    paths = 'testpaths'
    binaries = 'testbinaries'
    runlevel_status = 'testrunlevel_status'
    location = 'testlocation'
    is_started = 'testis_started'
    worked = 'testworked'
    cmd = 'testcmd'
    cleanout = 'testcleanout'

# Generated at 2022-06-13 06:21:51.198941
# Unit test for function main
def test_main():

    module = AnsibleModul

# Generated at 2022-06-13 06:22:04.701053
# Unit test for function main
def test_main():
    """
    Test function main()
    """
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

# Generated at 2022-06-13 06:22:16.520819
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


# Generated at 2022-06-13 06:22:28.644516
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

# Generated at 2022-06-13 06:22:30.650181
# Unit test for function main
def test_main():
    pass

# import module snippets
from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:37.346819
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

# Generated at 2022-06-13 06:22:47.715223
# Unit test for function main
def test_main():
    #from ansible.modules.system.service import sysvinit_mod
    datum = {"state":{"result":{"cmd":"netstat -tunl","end":1449191175.34234,"failed":False,"rc":0,"start":1449191168.46831,"stdout":"Active Internet connections (only servers)","stdout_lines":["Active Internet connections (only servers)"]},"success":True},"changed":False}
    res = {"changed":False,"failed":False,"state":"stopped"}
    module = AnsibleModule(argument_spec={})
    #sysvinit_mod.sysvinit_mod(module, datum)
    del datum['state']['result']['stdout']
    sysvinit_mod.sysvinit_mod(module, datum)

# Generated at 2022-06-13 06:22:49.164687
# Unit test for function main
def test_main():
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:23:43.286503
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.service import sysv_is_enabled

    # Dummy init script
    script = '/tmp/ansible_sysvinit_test'
    with open(script, 'w') as f:
        f.write('#!/bin/sh\n\nexit 0')
    import os
    os.chmod(script, 0o755)

    # Dummy status output
    testout = '/tmp/ansible_sysvinit_testout'
    with open(testout, 'w') as f:
        f.write('This is a test')

    def remove_dummies():
        os.remove(script)
        os.remove(testout)

    # Fix module_utils paths since AnsibleModule is in cwd

# Generated at 2022-06-13 06:23:53.561486
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.service import sysv_is_enabled, get_sysv_script, sysv_exists, fail_if_missing, get_ps, daemonize

    def run_command_success(self, cmd, daemonize=False):
        return (0, 'Success', 'Success')

    def run_command_fail(self, cmd, daemonize=False):
        return (1, 'Failed', 'Failed')


# Generated at 2022-06-13 06:24:00.763722
# Unit test for function main
def test_main():
    """
    @return: nothing
    """
    from ansible.module_utils import basic
    from ansible.module_utils import service
    
    module_args = {}
    if module_args:
        #result = dict(
        #    changed=True,
        #    original_message='',
        #    message=''
        #)
        result = dict()

        basic._ANSIBLE_ARGS = to_bytes(json.dumps(dict(
            ANSIBLE_MODULE_ARGS=module_args,
            ANSIBLE_MODULE_CONSTANTS=dict(
                TEMP_DIR=['/tmp'],
                SUPPORTED_PLATFORMS=['posix'],
            ),
        )))

        #result = ServiceModule().run()
        basic._ANSIBLE_ARGS = to_bytes

# Generated at 2022-06-13 06:24:03.895258
# Unit test for function main
def test_main():
    # the following is the unittest for main()
    main()

if __name__ == "__main__":
    main()

# Generated at 2022-06-13 06:24:06.997684
# Unit test for function main
def test_main():
    module = AnsibleModule(argument_spec={}, supports_check_mode=True)
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:17.275991
# Unit test for function main
def test_main():

    ###################### Test default locations for binaries ########################
    def test_default_binaries():
        module = AnsibleModule(argument_spec=dict(name=dict(required=True, type='str', aliases=['service']), state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str')), supports_check_mode=True, required_one_of=[['state', 'enabled']])
        # locate binaries for service management
        paths = ['/sbin', '/usr/sbin', '/bin', '/usr/bin']
        binaries = ['/sbin/chkconfig', '/usr/sbin/update-rc.d', '/usr/lib/insserv/insserv', '/usr/sbin/service']
        location = {}

# Generated at 2022-06-13 06:24:18.580126
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:26.182666
# Unit test for function main
def test_main():
    result = {}
    result.setdefault('name', 'apache')
    result.setdefault('status', {})
    result['status'].setdefault('enabled', {})
    result['status']['enabled'].setdefault('changed', 'True')
    result['status']['enabled'].setdefault('rc', '2')
    result['status']['enabled'].setdefault('stdout', 'apache')
    result['status']['enabled'].setdefault('stderr', 'False')
    result['status']['enabled'].setdefault('runlevels', '3')
    result.setdefault('status', {})
    result['status'].setdefault('reloaded', {})
    result['status']['reloaded'].setdefault('changed', 'True')
    result['status']['reloaded'].set

# Generated at 2022-06-13 06:24:37.758399
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    import os

# Generated at 2022-06-13 06:24:39.168516
# Unit test for function main
def test_main():
    pass


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:26:31.316440
# Unit test for function main
def test_main():
    # Test args
    test_arg_module = sys.modules[__name__]
    test_arg_module.params = {"name": "sshd", "state": "reloaded", "enabled": False, "sleep": 0}
    test_arg_module.exit_json = exit_json
    test_arg_module.fail_json = fail_json
    test_arg_module.run_command = run_command
    test_arg_module.module = argparse.ArgumentParser(description='Test description')
    test_arg_module.sys.modules['ansible_module_utils.basic'] = ansible_module_utils.basic
    test_arg_module.sys.modules['ansible_module_utils.service'] = ansible_module_utils.service

# Generated at 2022-06-13 06:26:43.514391
# Unit test for function main
def test_main():
    test_params = dict(
        name='apache2',
        state='started',
        enabled='yes',
        sleep=1,
        pattern=None,
        arguments=None,
        runlevels=None,
        daemonize=None,
    )
    module = AnsibleModule(**test_params)
    result = main()
    assert result['status']['enabled']['changed'] == False
    assert result['status']['enabled']['rc'] == None
    assert result['status']['enabled']['stdout'] == None
    assert result['status']['enabled']['stderr'] == None
    assert result['status']['started']['changed'] == False
    assert result['status']['started']['rc'] == None

# Generated at 2022-06-13 06:26:54.095194
# Unit test for function main
def test_main():

    name = "apache2"
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str', aliases=['service']),
            state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str', default='started'),
            enabled=dict(type='bool', default=True),
            sleep=dict(type='int', default=1),
            pattern=dict(type='str'),
            arguments=dict(type='str', aliases=['args']),
            runlevels=dict(type='list', elements='str'),
            daemonize=dict(type='bool', default=False),
        ),
        supports_check_mode=True,
        required_one_of=[['state', 'enabled']],
    )

    # ensure service exists, get

# Generated at 2022-06-13 06:27:02.249820
# Unit test for function main
def test_main():

    # Make sure we use actions that are not None and not the same
    action = 'stopped'
    name = 'syslog-ng'
    pattern = 'syslog-ng'
    enabled = True

    sysvinit_args = dict(
        action=action,
        name=name,
        pattern=pattern,
        enabled=enabled,
    )

    with patch('ansible_collections_general.unix.plugins.modules.sysvinit.AnsibleModule') as module:
        module.params = sysvinit_args
        main()
        assert module.exit_json.called_with(**{'action': action, 'name': name, 'pattern': pattern, 'enabled': enabled})

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:11.785059
# Unit test for function main
def test_main():
    argv = [
        'service',
        'name=httpd',
        'state=started',
        'enabled=True',
        'sleep=1',
        'pattern=httpd',
        'arguments=None',
        'runlevels=[3,5]',
        'daemonize=False',
    ]

    from ansible.module_utils._text import to_bytes
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.six.moves import StringIO

    stdout_bak, sys.stdout = sys.stdout, StringIO()
    sys.argv = [to_bytes(i, encoding='utf8') for i in argv]


# Generated at 2022-06-13 06:27:20.020045
# Unit test for function main
def test_main():
    import sys

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
    import sys
    import pytest

# Generated at 2022-06-13 06:27:32.570388
# Unit test for function main
def test_main():
    test_cases = [
        dict(
            module_args={
                "name": "iptables",
                "enabled": True,
                "runlevels": [ '3', '5' ],
            },
            skip=False,
        ),
    ]

    # Test the module

# Generated at 2022-06-13 06:27:38.374579
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
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:53.173640
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
        required_one_of=[['state', 'enabled']],
    )
    class MockModule(object):
        def __init__(self, *args, **kwargs):
            self.params = kw

# Generated at 2022-06-13 06:27:57.075192
# Unit test for function main
def test_main():
    module_args = dict(
        name=dict(required=True, type='str', aliases=['service']),
        state=dict(choices=['started', 'stopped', 'restarted', 'reloaded'], type='str'),
        enabled=dict(type='bool'),
        sleep=dict(type='int', default=1),
        pattern=dict(type='str'),
        arguments=dict(type='str', aliases=['args']),
        runlevels=dict(type='list', elements='str'),
        daemonize=dict(type='bool', default=False),
        )
    main()
if __name__ == '__main__':
    main()