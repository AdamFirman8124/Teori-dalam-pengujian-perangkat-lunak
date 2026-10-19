

# Generated at 2022-06-13 06:21:39.351909
# Unit test for function main
def test_main():
    test_case = dict(
        name="apache2",
        state=None,
        enabled=True,
        sleep=1,
        pattern=None,
        arguments=None,
        runlevels=None,
        daemonize=False,
    )


# Generated at 2022-06-13 06:21:50.585850
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
if __name__ == '__main__':
    main

# Generated at 2022-06-13 06:22:03.995901
# Unit test for function main
def test_main():
    module = AnsibleModule({
        'name': 'foo',
        'state': 'started',
        'enabled': True,
    })
    module.run_command = Mock(return_value=(0, 'stdout', 'stderr'))
    module.warn = Mock(return_value=None)
    module.exit_json = Mock(return_value=None)
    module.get_bin_path = Mock(return_value='/bin/foo')
    module.run_command = Mock(return_value=(0, 'stdout', 'stderr'))
    main()
    assert module.run_command.call_count == 2
    assert module.run_command.call_args_list[0][0][0] == 'update-rc.d foo enable'
    assert module.run_command.call_args_list

# Generated at 2022-06-13 06:22:12.891801
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

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:22:22.592338
# Unit test for function main
def test_main():
    # import needed modules and remove modules that break when imported on
    # windows systems
    from ansible.modules.system.service import main
    import pytest
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.service import sysv_is_enabled, get_sysv_script, sysv_exists, fail_if_missing, get_ps, daemonize
    import re
    import inspect

    # This tests assumes you have the program 'true', on windows systems
    # where this is not the case, this test will fail

# Generated at 2022-06-13 06:22:26.308993
# Unit test for function main
def test_main():
  argv=["sysvinit.py","-h"]
  main()

# Command line execution
if __name__ == '__main__':
    # Unit test for function main
    #test_main()
    main()

# Generated at 2022-06-13 06:22:31.044688
# Unit test for function main
def test_main():
    import sys
    from ansible.module_utils.basic import AnsibleModule

    sys.modules["ansible_module_sysvinit"] = AnsibleModule
    sys.modules["ansible_module_sysvinit"].sysv_exists = lambda self, name: True
    sys.modules["ansible_module_sysvinit"].sysv_is_enabled = lambda self, name: True
    sys.modules["ansible_module_sysvinit"].get_sysv_script =lambda self, name: "/etc/init.d/"

    import sysvinit
    sysvinit.main()

if __name__ == '__main__':
    # Unit test for function main
    test_main()

# Generated at 2022-06-13 06:22:35.793963
# Unit test for function main

# Generated at 2022-06-13 06:22:46.732722
# Unit test for function main
def test_main():
    test_sysd_script = 'test_sysd_script'
    test_binaries = { 'chkconfig': 'test_chkconfig',
                      'update-rc.d': 'test_update-rc.d',
                      'service': 'test_service' }
    test_runlevels = ['4','5']
    test_pattern = 'test_pattern'
    test_name = 'test_name'
    test_bin_response = 'test_bin_response'
    test_run_command_response = (1, 'test_out', 'test_err')
    test_run_command_service_status_response = (0, 'test_out', '')
    test_remove_verb_ed = 'stop'
    test_get_ps_response = True
    test_sleep_for = 1
    test_enabled

# Generated at 2022-06-13 06:22:57.689278
# Unit test for function main
def test_main():
    # ensure service exists, get script name
    fail_if_missing(module, sysv_exists(name), name)
    script = get_sysv_script(name)

    # locate binaries for service management
    paths = ['/sbin', '/usr/sbin', '/bin', '/usr/bin']
    binaries = ['chkconfig', 'update-rc.d', 'insserv', 'service']

    # Keeps track of the service status for various runlevels because we can
    # operate on multiple runlevels at once
    runlevel_status = {}

    location = {}
    for binary in binaries:
        location[binary] = module.get_bin_path(binary, opt_dirs=paths)

    # figure out enable status
    if runlevels:
        for rl in runlevels:
            runlevel_status.set

# Generated at 2022-06-13 06:23:55.313733
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

# Generated at 2022-06-13 06:24:05.563830
# Unit test for function main
def test_main():
    from ansible.module_utils import basic
    test_module = basic.AnsibleModule(
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
    #test_module.exit

# Generated at 2022-06-13 06:24:07.371991
# Unit test for function main
def test_main():
    main()

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:17.580542
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

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:26.485394
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


# Generated at 2022-06-13 06:24:37.975146
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
    module.run_command = MagicMock(return_value=(0, '', ''))
   

# Generated at 2022-06-13 06:24:45.196284
# Unit test for function main
def test_main():
    result = dict(
        name='',
        changed=False,
        status={},
    )


# Generated at 2022-06-13 06:24:47.143241
# Unit test for function main
def test_main():
    # Validate that service is started
    main()


if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:24:58.505297
# Unit test for function main

# Generated at 2022-06-13 06:25:04.879502
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
    name = "apache2"
    action = "started"
    enabled = True
    runlevels

# Generated at 2022-06-13 06:27:05.238559
# Unit test for function main
def test_main():
    # Load the arguments from a dict so this can be easily re-used in other tests
    my_test_args = dict(
        name='test',
        state=None,
        enabled=None,
    )
    # Set up the test environment

# Generated at 2022-06-13 06:27:09.441745
# Unit test for function main
def test_main():
    from ansible.module_utils.basic import AnsibleModule
    module = AnsibleModule(
        argument_spec=dict(
        ),
        supports_check_mode=True
    )
    rc = main()
    assert rc

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:27:18.570013
# Unit test for function main
def test_main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=False, type='str', aliases=['service']),
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

# Generated at 2022-06-13 06:27:24.367838
# Unit test for function main
def test_main():
    result = dict(results="""
            {
                "attempts": 1,
                "changed": true,
                "name": "apache2",
                "status": {
                    "enabled": {
                        "changed": true,
                        "rc": 0,
                        "stderr": "",
                        "stdout": ""
                    },
                    "stopped": {
                        "changed": true,
                        "rc": 0,
                        "stderr": "",
                        "stdout": "Stopping web server: apache2.\n"
                    }
                }
            }
    """)


# Generated at 2022-06-13 06:27:35.173458
# Unit test for function main
def test_main():
    # Unit test import
    from ansible_collections.ansible.misc.tests.unit.modules.utils import set_module_args
    from ansible_collections.ansible.misc.tests.unit.modules.unit_test_utils.service_test_utils import check_args_test

    # check_args_test as set_module_args doesnt load argspec
    check_args_test(module_path, module_args, module_name)

    # Test 1
    module_args_test = """
    name: httpd
    state: stopped
    enabled: yes
    sleep: 1
    pattern: httpd
    daemonize: False
    """
    set_module_args(module_args_test)
    result = main()
    assert result["results"]["changed"] is False
    # Test 2
    module_

# Generated at 2022-06-13 06:27:50.680455
# Unit test for function main
def test_main():
    """ Test main function
    """
    import sys
    import os
    import argparse
    import tempfile
    import shutil
    import subprocess
    from ansible.module_utils import basic
    from ansible.module_utils.six import b
    from ansible.module_utils._text import to_bytes
    try:
        from ansible.module_utils import service
    except:
        from ansible_collections.community.general.plugins.modules.module_utils import service

    def makefile(path, content):
        """ Create a file at a given path and write content

        Args:
          path (str): file path
          content (str): content to write to file
        """
        fd, tf = tempfile.mkstemp()
        f = os.fdopen(fd, "w")
        f.write

# Generated at 2022-06-13 06:27:52.474264
# Unit test for function main
def test_main():
    pass

if __name__ == '__main__':
    main()

# Generated at 2022-06-13 06:28:00.867166
# Unit test for function main
def test_main():
    #print("In main")
    module = 'chkconfig'

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

# Generated at 2022-06-13 06:28:13.504422
# Unit test for function main
def test_main():
    test_params = {
        'name': 'sshd',
        'state': 'started',
        'enabled': False,
        'runlevels': ['5'],
    }
    test_sysvinit_is_enabled = True
    test_sysv_exists = True
    test_get_sysv_script = '/etc/init.d/sshd'

    # mock
    from ansible.module_utils.basic import AnsibleModule
    from ansible.module_utils.service import sysv_is_enabled, get_sysv_script, sysv_exists
    from ansible.module_utils import basic

    def test_sysv_is_enabled(name, runlevel=None):
        return test_sysvinit_is_enabled

    def test_get_sysv_script(name):
        return test_

# Generated at 2022-06-13 06:28:24.006913
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